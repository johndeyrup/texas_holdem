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


                 
#Create group of players 
player_one = Player('P1', 100)
player_two = Player('P2', 100)

#Creates your board, with players and a starting blind size
board = Board([player_one, player_two], 10)
board.players_join_round()
board.deduct_blinds()
board.deal_cards()
board.betting_round()
for player in board.players:
    print(player.get_stats())
# board.betting_round(board.players)
# #If there is ever one person in the betting round, the hand ends and the player gets his bid back, plus the bid of any player less than or equal to his bid
#     #Betting starts with the first player and ends with last player(big blind)
#     #Each player can raise, call, check, or fold
#     #If at the end of the round everyone's bets are the same the betting ends and the play advances to flop, river, turn, respectively
#     #The last person always get to raise, call, etc even if all the blinds are equal
#     #There is an exception to these rules when there are two players
#     #If there are two players the big blind bets last on the first round but after the first round the small blind bets last
#     def bettings(self):
#         number_players = len(self.get_players_playing())
#         if(number_players == 1):
#             self.assign_winnings()
#         elif(number_players == 2):
#             self.two_player_betting()
#         elif(number_players > 2):
#             self.normal_betting
#         else:
#             print('unknown players')
#     
#     def normal_betting(self):
#         for player in self.players:
#             self.player_decision()
#     
#     def player_decision(self):
#         
#     def two_player_betting(self):
#         pass
# board.deck.do_flop()

# 
# # #Creates a group of players and gives them a starting hand
# # def create_players(num_players, buy_in):
# #     starting_position = [x for x in range(num_players)]
# #     shuffle(starting_position)
# #     player_names = ['Alex', 'Bob', 'George', 'Susan', 'Sarah', 'Alexis', 'Marie']
# #     list_players = []
# #     for i in range(num_players):
# #         card_list = [my_deck[i]] + [my_deck[i+num_players]]
# #         list_players.append(Player(player_names[i], starting_position[i],buy_in, card_list, 0, True))
# #     return list_players
# 
# #Updates player positions after a round
# def update_player_positions(list_players):
#     for player in list_players:
#         player.position = player.position+1
#         if player.position == len(list_players):
#             player.position = 0
#     return list_players
# 
# # #Creates the board position caused by the flop, the turn and the river
# # #Show the cards on the flop
# # def perform_flop(deck_position):
# #     board_state.community_cards = my_deck[deck_position+1:deck_position+4]
# # #     print("\nFlop")
# # #     for card in board_state.community_cards:
# # #         print(card.get_properties())
# # 
# # #Show the cards on the turn    
# # def perform_turn(deck_position):
# #     board_state.community_cards = board_state.community_cards + [my_deck[deck_position+1]]
# # #     print("\nTurn")
# # #     for card in board_state.community_cards:
# # #         print(card.get_properties())
# # 
# # #Show the cards on the river    
# # def perform_river(deck_position):
# #     board_state.community_cards = board_state.community_cards + [my_deck[deck_position+1]]
# # #     print("\nRiver")
# # #     for card in board_state.community_cards:
# # #         print(card.get_properties())
#         
# #Update boards pot size by bet amount        
# def update_pot(bet):
#     board_state.pot += bet
# 
# #Player bets an amount onto the board    
# def player_bet(player, bet):
#     if(bet > player.money):
#         update_pot(player.money)
#         player.bid += player.money
#         player.money -= player.money
#     else:
#         player.bid += bet
#         player.money -= bet
#         update_pot(bet)
# #Prints all cards in a hand
# def print_cards(hand):
#     for card in hand:
#         print(card.get_properties())
# #Removes the blinds from the big blind and the small blind and adds them to the board state    
# def deduct_blinds(player_list, blind_size):
#     for player in players_in_hand(player_list):
#         if(player.get_position() == 0):
#             player_bet(player, blind_size)
#         elif(player.get_position() == 1):
#             player_bet(player, blind_size*2)
#             
# #Returns all the players still in the hand
# def players_in_hand(player_list):
#     player_in_hand = [player for player in player_list if player.get_in_hand() == True]
#     return player_in_hand
# 
# #Sorts players into bidding order
# def bidding_order(player_list):
#     bidding_order = sorted(player_list, key=attrgetter('position'))
#     if len(bidding_order) > 2:
#         bidding_order = bidding_order[2:] + bidding_order[0:2]
#     return bidding_order
# 
# #Sorts cards from highest to lowest
# def sort_by_number(cards):
#     cards = sorted(cards, key=attrgetter('number'), reverse=True)
#     return cards
# 
# #Determines best hand for player
# def find_best_hand(player, community_cards):
#     card_pool = player.get_cards()+community_cards
#     player_hand_value = 0
#     best_hand = []
# #     for card in card_pool:
# #         print(card.get_properties(), end =", ")
#     if get_flush(card_pool) != None:
#         if(get_straight(get_flush(card_pool)) != None):
#             player_hand_value = 9+get_straight(get_flush(card_pool))[0].get_number()/100
#             best_hand = get_straight(get_flush(card_pool))
#         else:
#             player_hand_value = 6+get_card_value(get_flush(card_pool)[:5])
#             best_hand = get_flush(card_pool)[:5]
#     elif get_four_kind(card_pool) != None:
#         extra_card = get_highest_card([card for card in card_pool if card.get_number() != get_four_kind(card_pool)[0].get_number()])
#         player_hand_value = 8+get_four_kind(card_pool)[0].get_number()/100+extra_card.get_number()/10000
#         best_hand = get_four_kind(card_pool)+[extra_card]
#     elif get_full_house(card_pool) != None:
#         player_hand_value = 7+get_full_house(card_pool)[0].get_number()/100+get_full_house(card_pool)[-1].get_number()/10000
#         best_hand = get_full_house(card_pool)
#     elif get_straight(card_pool) != None:
#         player_hand_value = 5+get_straight(card_pool)[0].get_number()/100
#         best_hand = get_straight(card_pool)
#     elif get_three_kind(card_pool) != None:
#         extra_cards = sort_by_number([card for card in card_pool if card.get_number() != get_three_kind(card_pool)[0].get_number()])[:2]
#         player_hand_value = 4+get_three_kind(card_pool)[0].get_number()/100+extra_cards[0].get_number()/10000+extra_cards[1].get_number()/1000000
#         best_hand = get_three_kind(card_pool)+extra_cards
#     elif get_two_pair(card_pool) != None:
#         not_in_two_pair = [card for card in card_pool if card not in get_two_pair(card_pool)]
#         player_hand_value = 3+get_two_pair(card_pool)[0].get_number()/100+get_two_pair(card_pool)[-1].get_number()/10000+get_highest_card(not_in_two_pair).get_number()/1000000
#         best_hand = get_two_pair(card_pool)+[get_highest_card(not_in_two_pair)]
#     elif get_two_kind(card_pool) != None:
#         extra_cards = sort_by_number([card for card in card_pool if card.get_number() != get_two_kind(card_pool)[0].get_number()])[:3]
#         player_hand_value = 2+get_two_kind(card_pool)[0].get_number()/100+extra_cards[0].get_number()/10000+extra_cards[1].get_number()/1000000+extra_cards[2].get_number()/100000000
#         best_hand = get_two_kind(card_pool)+extra_cards
#     else:
#         extra_cards = sort_by_number(card_pool)[:5]
#         player_hand_value = 1+get_card_value(extra_cards)
#         best_hand = extra_cards
#     return player_hand_value, best_hand
#       
# def get_card_value(hand):
#     total_hand_value = 0
#     increment = 100
#     for card in hand:
#         total_hand_value += card.get_number()/increment
#         increment *= 100
#     return total_hand_value 
# 
#      
# def get_highest_card(cards):
#     highest_card = cards[0]
#     for card in cards[1:]:
#         if card.get_number() > highest_card.get_number():
#             highest_card = card
#     return highest_card
# 
# def get_two_kind(cards):
#     tally_cards = Counter([card.get_number() for card in cards])
#     list_of_twos = []
#     for number in tally_cards:
#         if tally_cards[number] == 2:
#             list_of_twos = ([card for card in cards if card.get_number()==number])
#     if len(list_of_twos) > 0:
#         return list_of_twos
# 
# def sort_pair(pair_groups):
#     highest_pair = pair_groups[0]
#     second_pair = pair_groups[1]
#     if highest_pair[0].get_number() < second_pair[0].get_number():
#         temp = highest_pair
#         highest_pair = second_pair
#         second_pair = temp
#     return highest_pair+second_pair
#         
# def get_two_pair(cards):
#     tally_cards = Counter([card.get_number() for card in cards])
#     list_of_twos = []
#     output = None
#     for number in tally_cards:
#         if tally_cards[number] == 2:
#             list_of_twos.append([card for card in cards if card.get_number()==number])
#     if len(list_of_twos) == 2:
#         output = sort_pair(list_of_twos)
#     elif len(list_of_twos) == 3:
#         first_element = list_of_twos[0]
#         second_element = list_of_twos[1]
#         third_element = list_of_twos[2]
#         f_num = first_element[0].get_number()
#         s_num = second_element[0].get_number()
#         t_num = third_element[0].get_number()
#         if(f_num < s_num and f_num < t_num):
#             output = sort_pair(list_of_twos[1:])
#         elif(s_num < f_num and s_num <t_num):
#             output = sort_pair(list_of_twos[0::2])
#         else:
#             output = sort_pair(list_of_twos[:2])
#     return output
# 
# def get_three_kind(cards):
#     #Tallies up all the numbers in a set of cards
#     numbers = Counter([card.get_number() for card in cards])
#     three_kind_list = []
#     for number in numbers:
#         if(numbers[number] == 3):
#             three_kind_list += [card for card in cards if card.get_number() == number]
#     if len(three_kind_list) > 0:
#         return three_kind_list
# 
# def get_straight(cards):
#     sorted_cards = sort_by_number(cards)
#     if sorted_cards[0].get_number() == 14:
#         sorted_cards.append(sorted_cards[0])
#     for i in range(len(sorted_cards)-4):
#         previous_position = sorted_cards[i]
#         straight_list = [previous_position]
#         for j in range(i+1, len(sorted_cards)):
#             if(previous_position.get_number() - 1 ==sorted_cards[j].get_number()):
#                 straight_list.append(sorted_cards[j])
#                 if(sorted_cards[j].get_number() == 2):
#                     if(sorted_cards[0].get_number()==14):
#                         straight_list.append(sorted_cards[0])
#                         break
#                 previous_position = sorted_cards[j]                    
#             elif(previous_position.get_number()==sorted_cards[j].get_number()):
#                 if(sorted_cards[j] == 2):
#                     if(sorted_cards[0].get_number()==14):
#                         straight_list.append(sorted_cards[0])
#                         break
#             else:
#                 straight_list = []
#                 break
#         if(len(straight_list) >= 5):
#             return(straight_list)
#             break
#         
# #Gets all cards that are part of a flush and returns them in sorted order
# def get_flush(cards):
#     suits = [card.get_suit() for card in cards]
#     flush_type = None
#     for elem in Counter(suits):
#         if Counter(suits)[elem] > 4:
#             flush_type = elem
#             flush = sort_by_number([card for card in cards if card.get_suit() == flush_type])
#             return flush
# 
# def get_full_house(cards):
#     threes = get_three_kind(cards)
#     if threes != None:
#         if len(threes) == 6:
#             if(threes[0].get_number() > threes[5].get_number()):
#                 return threes[0:3] + threes[3:5]
#             else:
#                 return threes[3:]+threes[0:2]
#         elif len(threes) == 3:
#             non_three_kind = [card for card in cards if card.get_number() != threes[0].get_number()]
#             if(get_two_pair(non_three_kind) != None):
#                 return threes+get_two_pair(non_three_kind)[0:2]
#             elif(get_two_kind(non_three_kind) != None):
#                 return threes+get_two_kind(non_three_kind)
#         
# #Checks the hand for four of a kind and returns it
# def get_four_kind(cards):
#     numbers = [card.get_number() for card in cards]
#     four_kind = ""
#     for number in Counter(numbers):
#         if Counter(numbers)[number] == 4:
#             four_kind = number
#             set_of_four = [card for card in cards if card.get_number() == four_kind]
#             return set_of_four         
# 
# #Gets player rankings based on their hands
# def get_player_ranking(players):
#     player_rankings = sorted(players, key=attrgetter('hand_value'), reverse=True)
#     player_rankings = [player for player in player_rankings if player.get_in_hand() == True]
#     return player_rankings
# 
# def bid_greater_equal(player_one, player_two):
#     if(player_one >= player_two):
#         return player_two
#     else:
#         return player_one
#     
# def update_winnings(board, winner, loser, amount):
#     #Subtract the amount from the pot
#     board.update_pot(-amount)
#     #Subtract the amount from the losers bid, the winner's bid will be updated after he has received everyone else's bid
#     loser.update_bid(-amount)
#     #Add the amount to winner's money
#     winner.update_money(amount)
#     
# #updates pot and player bids
# def distribute_pot(board, winner, loser):
#     winner_bid = winner.get_bid()
#     loser_bid = loser.get_bid()
#     amount = bid_greater_equal(winner_bid, loser_bid)
#     update_winnings(board,winner,loser,amount)
#     
# def assign_winnings(players):
#     win_list = get_player_ranking(players)
#     for winner in win_list:
# #         tied_players = [player for player in players if player.get_hand_value == winner.get_hand_value()]
# #         if len(tied_players > 1):
# #             pass       
#         winnerbid = winner.get_bid()
#         lose_list = [player for player in players if player.get_bid() > 0 and player!=winner]
#         for loser in lose_list:
#             distribute_pot(board_state,winner,loser)
#         board_state.update_pot(-winnerbid)
#         winner.update_money(winnerbid)
#         winner.update_bid(-winnerbid)
#         board_state.get_board_stats()
#     player_left = [player for player in players if player.get_bid() > 0]
#     if(len(player_left)>0):
#         for clean_up_player in player_left:
#             bid = clean_up_player.get_bid()
#             clean_up_player.update_bid(-bid)
#             clean_up_player.update_money(bid)
#             board_state.update_pot(-bid)
# 
# 
# #Check, if your bid is not equal to the highest bid print error message
# def player_check(highest_bid, player_bid):
#     if(player_bid != highest_bid):
#         print("I am sorry your bid must be equal to the highest bid")
#         return True
#      
# #Get players action
# def get_player_decision(player):
#     player_action = input("Player %s, do you want to bet, call, check, or fold? " % (player.get_position())).lower()
#     if(player_action == 'fold'):
#         player.is_in_hand = False
#     elif(player_action == 'call'):
#         amount_to_check = board_state.get_highest_bid() - player.bid
#         player_bet(player, amount_to_check)
#     elif(player_action == 'bet'):
#         bet_amount = int(input("Enter your bet amount "))
#         if(bet_amount+player.get_bid() < board_state.get_highest_bid() and bet_amount < player.get_money()):
#             print('I am sorry %s is an invalid bid amount, please bet at least %s' % (bet_amount, board_state.get_highest_bid()-player.get_bid()))
#             get_player_decision(player)
#         else:
#             player_bet(player, bet_amount)
#     elif(player_action == 'check'):
#         if(player_check(board_state.get_highest_bid(), player.bid)):
#             get_player_decision(player)
#     else:
#         print("I am sorry I do not recognize this action")
#         get_player_decision(player)
#         
# #Returns an input based on 
# #Play a round of betting, the round of betting starts with the person to the left of the big blind having the option to raise, check, or fold
# #This continues around the circle until everyone else has had the chance to raise check or fold
# #If the big blind checks then the betting ends. If the big blind raises the betting continues until the big blind checks
# #If the big blind folds the previous person (small blind) is the last person to bet and so forth       
# def do_betting_round(player_list, betting_round):
#     for player in player_list:
#         if len(board_state.get_players_playing()) == 1:
#                 print('betting round win')
#                 assign_winnings(player_list)
#                 break
#         if betting_round !=1 and board_state.get_all_bids_equal():
#                 print('all players have same bet, proceed to next round')
#                 break
#         elif player.get_in_hand() == True:
#                 get_player_decision(player)
# 
# #Bid again if all the bids are not equal
# def continue_bidding(player_list):
#     board_state.get_board_stats()
#     betting_round_num = 1
#     if betting_round_num == 1 and len(board_state.get_players_playing()) > 1:
#         do_betting_round(player_list, betting_round_num)
#         betting_round_num += 1
#     else:
#         print("You need at least two players to play")
#     if betting_round_num > 1 and len(board_state.get_players_playing()) > 1:
#         while(not board_state.get_all_bids_equal() and len(board_state.get_players_playing()) > 1):
#             do_betting_round(player_list, betting_round_num)
#             betting_round_num += 1
#     if len(board_state.get_players_playing())==1:
#         assign_winnings(player_list) 
# 
# 
# #Add players to the board
# board_state = Board(create_players(5, 100), 0, 0)
# print("Pot size: $%s " % board_state.get_pot())
# #Deduct the blinds
# deduct_blinds(board_state.get_players(),10)
# 
# #Do bidding until you have one player still in or the last person still in calls/checks
# continue_bidding(bidding_order(board_state.get_players()))
# if(len(board_state.get_players_playing()) > 1):
#     perform_flop(2*len(board_state.get_players()))
#     print_cards(board_state.get_community_cards())
#     continue_bidding(bidding_order(board_state.get_players()))
#      
# if(len(board_state.get_players_playing()) > 1):
#     perform_turn(2*len(board_state.get_players())+4)
#     print_cards(board_state.get_community_cards())
#     continue_bidding(bidding_order(board_state.get_players()))
#  
# if(len(board_state.get_players_playing()) > 1):    
#     perform_river(2*len(board_state.get_players())+6)
#     print_cards(board_state.get_community_cards())
#     continue_bidding(bidding_order(board_state.get_players()))
#     for player in board_state.get_players_playing():
#         hand_value, best_hand = find_best_hand(player, board_state.get_community_cards())
#         player.update_hand_value(hand_value)
#         print("Player %s: %s" % (player.get_position(),player.get_hand_value()))
#         print_cards(best_hand)
#     assign_winnings(board_state.get_players())
#     
# # update_player_position(board_state.get_players())