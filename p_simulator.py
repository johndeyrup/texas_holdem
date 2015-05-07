'''
Created on Apr 8, 2015
Simulates AI and game state of Texas Hold' Em
@author: John Deyrup
'''
# from random import shuffle
# from operator import attrgetter
# from collections import Counter
from player import Player       
from board import Board
import hand_evaluator
from card import Card
from operator import attrgetter

def print_out_board(description):
    print(description)
    for card in board.community_cards:
        print(card.get_properties())
    for player in board.players:
        print(player.get_stats())
    print("Pot:", board.pot)
    
def enough_players():
    if len(board.players_in_hand()) > 1:
        return True
                
            
            
                     
#Create group of players 
player_one = Player('P1', 100)
player_two = Player('P2', 100)
 
#Creates your board, with players and a starting blind size
board = Board([player_one, player_two], 10)
# print_out_board('Players added to board')
# board.players_join_round()
# print_out_board('Players join round')
# board.deduct_blinds()
# print_out_board('Blinds are added to pot')
# board.deal_cards()
# print_out_board("cards are dealt")
# board.betting_round()
# if enough_players():
#     print_out_board("Players bet")
#     board.add_flop()
#     print_out_board('Flop')
#     board.betting_round()
#     print_out_board('Post flop betting results')
#     if enough_players():
#         board.add_river()
#         print_out_board('River')
#         board.betting_round()
#         print_out_board('Post river betting results')
#         if enough_players():
#             board.add_turn()
#             print_out_board('Turn')
#             board.betting_round()
#             print_out_board('Post turn betting results')
#             if enough_players():
#                 for player in board.players_in_hand():
#                     player.hand_value, best_hand = hand_evaluator.find_best_hand(player.cards, board.community_cards)
#                     print(player.hand_value)
#                     print(list(map(Card.get_properties,best_hand)))
# 
#                 