'''
Created on May 1, 2015

@author: John Deyrup
'''
from operator import attrgetter
from random import shuffle
from deck import Deck
#Board class shows players and community cards
class Board:
    
    #Constructs variables in board object, you cannot create a board without players
    def __init__(self, players):
        self.deck = Deck()
        self.players = players
        self.community_cards = []
        self.pot = 0
        self.shuffle_player_order()
    
    def shuffle_player_order(self):
        shuffle(self.players)
    
    #Deals out two cards to each player, each player is deal a card and then each player is dealt another card again    
    def deal_cards(self):
        for i in range(2):
            for player in self.players:
                player.cards += [self.deck.deal_card()]    
    
                        
    #Adds the flop to the board
    def add_flop(self):
        pass
    
    #Add the turn to the board
    def add_turn(self):
        pass
    
    #Adds the river to the board
    def add_river(self):
        pass
    
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
        self.pot -= amount
    
    #Return bid from pot to player's money
    def return_bid(self, player):
        player.money += player.bid
        self.pot -= player.bid
        player.bid -= player.bid
        
    #Rotates player position moving the last person to the first position and everyone else down one position
    def rotate_position(self, players):
        return [players.pop(-1)] + players
            
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