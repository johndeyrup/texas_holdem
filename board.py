'''
Created on May 1, 2015

@author: John Deyrup
'''
from operator import attrgetter
from random import shuffle
from deck import Deck
from player import Player
from itertools import groupby
#Board class shows players and community cards
class Board:
    
    #Constructs variables in board object, you cannot create a board without players
    def __init__(self, players, blind_size):
        self.deck = Deck()
        self.players = players
        self.community_cards = []
        self.pot = 0
        self.blind = blind_size
        self.shuffle_player_order()
    
    def shuffle_player_order(self):
        shuffle(self.players)
    
    def deduct_blinds(self):
        small_blind = self.blind
        big_blind = self.blind*2
        self.try_bid(self.players[-2], small_blind)
        self.try_bid(self.players[-1], big_blind)

    #Deals out two cards to each player, each player is deal a card and then each player is dealt another card again    
    def deal_cards(self):
        for i in range(2):
            for player in self.players:
                player.cards += [self.deck.deal_card()]    
                            
    #Adds the flop to the board
    def add_flop(self):
        self.community_cards = self.deck.do_flop()
    
    #Add the turn to the board
    def add_turn(self):
        self.community_cards.append(self.deck.do_turn())
    
    #Adds the river to the board
    def add_river(self):
        self.community_cards.append(self.deck.do_turn())
    
    #Add a players bid to the pot, if the bid is greater than the player's current money add the player's money
    def do_bid(self, player, amount):
        player.money -= amount
        player.bid += amount
        self.pot += amount
        
    #You cannot bid more money than you have so bid up to money in player
    def try_bid(self, player, amount):
        if player.money < amount:
            self.do_bid(player, player.money)
        else:
            self.do_bid(player, amount)        
             
    #Gives player winnings and subtracts that amount from the board
    def assign_winnings(self, player, amount):
        player.money += amount
        
    def assign_loss(self, player, amount):
        player.bid -= amount
        self.pot -= amount
    
    #Return bid from pot to player's money
    def return_bid(self, player):
        player.money += player.bid
        self.pot -= player.bid
        player.bid -= player.bid
        
    #Rotates player position moving the last person to the first position and everyone else down one position
    def rotate_position(self, players):
        return [players.pop(-1)] + players
    
    def get_highest_bid(self):
        return max([player.bid for player in self.players])
    
    def all_bids_equal(self,bids):
        if len(set(bids)) == 1:
            return True
        else:
            return False
        
    def get_greatest_bid(self,player_one_bid, player_two_bid):
        if(player_one_bid >= player_two_bid):
            return player_two_bid
        else:
            return player_one_bid
    
    def players_in_hand(self):
        return [player for player in self.players if player.is_in_hand == True]
    
    def betting_decision(self,player):
        player_response = player.get_valid_input()
        if player_response == 'FOLD':
            player.is_in_hand = False
        elif player_response == 'CALL':
            self.try_bid(player, self.get_highest_bid()-player.bid)
        elif player_response == 'CHECK':
            if player.bid < self.get_highest_bid():
                print('You must bid at least the highest bid to check')
                self.betting_decision(player)
        elif player_response == 'RAISE':
            self.try_raise(player)
            
    def try_raise(self, player):
        try:
            raise_amount = int(player.get_player_input("Enter the amount you would like to raise"))
            if raise_amount + player.bid < self.get_highest_bid():
                print('You must enter at least the highest bid %s' % self.get_highest_bid())
                self.try_raise(player)
            else:
                self.try_bid(player, raise_amount)
        except:
            print('Please enter a valid integer input; i.e., 1,2,3,4')
            self.try_raise(player)
            
    def sort_player_rankings(self, players):
        '''
        Sorts players from highest hand value to lowest then groups identical hand values
        '''
        sorted_players = sorted(players,key=attrgetter('hand_value'),reverse=True)
        grouped_players = groupby(sorted_players, lambda x:x.hand_value)
        final_list = []
        for val, player_group in grouped_players:
            temp_list = []
            for player in player_group:
                temp_list.append(player)
            final_list.append(temp_list)
        return final_list
            
    def win_by_fold(self):
        losers = [player for player in self.players if player.is_in_hand == False and player.bid > 0]
        winner = self.players_in_hand()[0]
        for loser in losers:
            amount = self.get_greatest_bid(winner.bid, loser.bid)
            self.assign_winnings(winner,amount)
            self.assign_loss(loser, amount)
            self.return_bid(loser)
        self.return_bid(winner)
        
    def distribute_tie_winnings(self, sub_group):
        sorted_players = sorted(sub_group, key=attrgetter('bid'))
        for player in sorted_players:
            amount_to_split = 0
            losers = [player for player in self.players if player.bid > 0 and player not in sorted_players]
            for loser in losers:
                amount = self.get_greatest_bid(player.bid, loser.bid)
                self.assign_loss(loser, amount)
                amount_to_split += amount
            players_to_split = sorted_players[sorted_players.index(player):]
            self.return_partial_bid(sorted_players)
            self.split_money(players_to_split, amount_to_split)

    def split_money(self, subgroup, amount):
        split_amount = amount / len(subgroup)
        if amount % len(subgroup) == 0:
            for player in subgroup:
                player.money += split_amount
        else:
            for i in range(len(subgroup)):
                if i < amount%len(subgroup):
                    subgroup[i].money += int(split_amount) + 1
                else:
                    subgroup[i].money += int(split_amount)
                
    def return_partial_bid(self, subgroup):
        #Every player with money still in the subgroup 
        sub_group = [player for player in subgroup if player.bid > 0]
        #The minimum bid still remaining this is the current player in this for loop
        if sub_group != []:
            min_bid = min([player.bid for player in sub_group])
            for player in sub_group:
                player.bid -= min_bid
                player.money += min_bid
                self.pot -= min_bid
            
    def assign_hand_win(self,players):           
        '''
        Assigns money to each player until there is no money in the pot
        '''
        ranked_players = self.sort_player_rankings(players)
        for player_group in ranked_players:
            if self.pot > 0: 
                group_size = len(player_group)
                if(group_size > 1):
                    self.distribute_tie_winnings(player_group)   
                else:
                    winner = player_group[0]
                    for loser in self.get_losers(winner):
                        amount = self.get_greatest_bid(winner.bid, loser.bid)
                        self.assign_winnings(winner,amount)
                        self.assign_loss(loser, amount)
                    self.return_bid(winner)
    
    def get_losers(self, winner):
        losers = [player for player in self.players if player.bid>0 and player != winner]
        return losers
    
    def additional_bidding_rounds(self):
        '''
        Each player makes a bet until all bets are or there is one player
        '''
        while self.all_bids_equal([player.bid for player in self.players_in_hand()]) == False:
            for player in self.players_in_hand():
                if len(self.players_in_hand())==1:
                    self.win_by_fold()
                self.betting_decision(player)
                if self.all_bids_equal([player.bid for player in self.players_in_hand()]) == True:
                    break      
    
    #Do betting round until all people have the same bet or there is only one player left
    def betting_round(self):
        '''
        Betting continues until all bets are equal or there is one player
        '''
        #Every player gets to bet on the first round
        for player in self.players_in_hand():
            if len(self.players_in_hand())==1 :
                self.win_by_fold()     
            else:
                self.betting_decision(player)
        #Every other round of bidding       
        if self.all_bids_equal([player.bid for player in self.players_in_hand()]) == False:
            self.additional_bidding_rounds()
            
    #If the player has money have them join the round            
    def players_join_round(self):
        for player in self.players:
            if player.money > 0:
                player.is_in_hand = True
            
