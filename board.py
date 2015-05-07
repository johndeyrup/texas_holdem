'''
Created on May 1, 2015

@author: John Deyrup
'''
from operator import attrgetter
from random import shuffle
from deck import Deck
from player import Player
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
            
    def win_by_fold(self):
        losers = [player for player in self.players if player.is_in_hand == False and player.bid > 0]
        winner = self.players_in_hand()[0]
        for loser in losers:
            amount = self.get_greatest_bid(winner.bid, loser.bid)
            self.assign_winnings(winner,amount)
            self.assign_loss(loser, amount)
            self.return_bid(loser)
        self.return_bid(winner)
    
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
            
    
            
            
#     #Returns all the player on the board    
#     def get_players(self):
#         return self.players
#     
#     #Returns all the community cards visible
#     def get_community_cards(self):
#         return self.community_cards   
#     
#     #Returns pot
#     def get_pot(self):
#         return self.pot
#     
#     #Returns the highest bid on the board
#     def get_highest_bid(self):
#         highest_bid = (sorted(self.players, key=attrgetter('bid')))[-1].get_bid()
#         return highest_bid
#     
#     #Returns True if all bids are equal
#     def get_all_bids_equal(self):
#         player_bids = [player.get_bid() for player in self.players if player.get_in_hand() == True]
#         if len(set(player_bids)) == 1:
#             return True
#         else:
#             return False
#     
#     #Returns all players in hand
#     def get_players_playing(self):
#         return [player for player in self.players if player.is_in_hand == True]
#     
# #     #Check if there are two players in hand
# #     def two_players_remaining(self):
# #         if(len(get_players_playing())==2):
# #             return True
# #         else:
# #             return False          
# #     
# #     #Check if there is one player in hand
# #     def one_player_remaining(self):
# #         if(len(get_players_playing())==1):
# #             return True
# #         else:
# #             return False        
#     
#     #Return board stats
#     def get_board_stats(self):
#         print("Pot size: $%s" % self.pot)
#         stats_list = ["Name: ", "Bid: ", "Money: $", "Position: ", "Still playing: ", "Card 1: ", "Card 2: "]
#         for player in self.players:
#             combined_list = [stats_list[i]+str(player.get_stats()[i]) for i in range(len(stats_list))]
#             print(combined_list)
#             
#     #Updates pot
#     def update_pot(self, value):
#         self.pot += value 