'''
Created on May 7, 2015

@author: arilab
'''
from operator import attrgetter
from collections import Counter
import functools
#Sorts cards from highest to lowest

card_primes = [2,3,5,7,11,13,17,19,23,29,31,37,41]
straights = [card_primes[x:x+5] for x in range(len(card_primes)-4)]
#Lowest straight
unique_straights = [41*2*3*5*7]
for straight in straights:
    unique_straights.append(functools.reduce(lambda x,y: x*y, straight))
    
    
def sort_by_number(cards):
    cards = sorted(cards, key=attrgetter('number'), reverse=True)
    return cards

#Determines best hand for player
def find_best_hand(player_cards, community_cards):
    card_pool = player_cards+community_cards
    player_hand_value = 0
    best_hand = []
    if get_flush(card_pool) != None:
        if(straight_value(get_flush(card_pool)) != None):
            player_hand_value = 9+straight_value(get_flush(card_pool))/10
            best_hand = get_straight(get_flush(card_pool))
        else:
            player_hand_value = 6+get_card_value(get_flush(card_pool)[:5])
            best_hand = get_flush(card_pool)[:5]
    elif get_four_kind(card_pool) != None:
        extra_card = get_highest_card([card for card in card_pool if card.get_number() != get_four_kind(card_pool)[0].get_number()])
        player_hand_value = 8+get_four_kind(card_pool)[0].get_number()/100+extra_card.get_number()/10000
        best_hand = get_four_kind(card_pool)+[extra_card]
    elif get_full_house(card_pool) != None:
        player_hand_value = 7+get_full_house(card_pool)[0].get_number()/100+get_full_house(card_pool)[-1].get_number()/10000
        best_hand = get_full_house(card_pool)
    elif get_straight(card_pool) != None:
        player_hand_value = 5+straight_value(card_pool)/10
        best_hand = get_straight(card_pool)
    elif get_three_kind(card_pool) != None:
        extra_cards = sort_by_number([card for card in card_pool if card.get_number() != get_three_kind(card_pool)[0].get_number()])[:2]
        player_hand_value = 4+get_three_kind(card_pool)[0].get_number()/100+extra_cards[0].get_number()/10000+extra_cards[1].get_number()/1000000
        best_hand = get_three_kind(card_pool)+extra_cards
    elif get_two_pair(card_pool) != None:
        not_in_two_pair = [card for card in card_pool if card not in get_two_pair(card_pool)]
        player_hand_value = 3+get_two_pair(card_pool)[0].get_number()/100+get_two_pair(card_pool)[-1].get_number()/10000+get_highest_card(not_in_two_pair).get_number()/1000000
        best_hand = get_two_pair(card_pool)+[get_highest_card(not_in_two_pair)]
    elif get_two_kind(card_pool) != None:
        extra_cards = sort_by_number([card for card in card_pool if card.get_number() != get_two_kind(card_pool)[0].get_number()])[:3]
        player_hand_value = 2+get_two_kind(card_pool)[0].get_number()/100+extra_cards[0].get_number()/10000+extra_cards[1].get_number()/1000000+extra_cards[2].get_number()/100000000
        best_hand = get_two_kind(card_pool)+extra_cards
    else:
        extra_cards = sort_by_number(card_pool)[:5]
        player_hand_value = 1+get_card_value(extra_cards)
        best_hand = extra_cards
    return player_hand_value, best_hand
       
def get_card_value(hand):
    total_hand_value = 0
    increment = 100
    for card in hand:
        total_hand_value += card.get_number()/increment
        increment *= 100
    return total_hand_value 
 
      
def get_highest_card(cards):
    highest_card = cards[0]
    for card in cards[1:]:
        if card.get_number() > highest_card.get_number():
            highest_card = card
    return highest_card
 
def get_two_kind(cards):
    tally_cards = Counter([card.get_number() for card in cards])
    list_of_twos = []
    for number in tally_cards:
        if tally_cards[number] == 2:
            list_of_twos = ([card for card in cards if card.get_number()==number])
    if len(list_of_twos) > 0:
        return list_of_twos
 
def sort_pair(pair_groups):
    highest_pair = pair_groups[0]
    second_pair = pair_groups[1]
    if highest_pair[0].get_number() < second_pair[0].get_number():
        temp = highest_pair
        highest_pair = second_pair
        second_pair = temp
    return highest_pair+second_pair
         
def get_two_pair(cards):
    tally_cards = Counter([card.get_number() for card in cards])
    list_of_twos = []
    output = None
    for number in tally_cards:
        if tally_cards[number] == 2:
            list_of_twos.append([card for card in cards if card.get_number()==number])
    if len(list_of_twos) == 2:
        output = sort_pair(list_of_twos)
    elif len(list_of_twos) == 3:
        first_element = list_of_twos[0]
        second_element = list_of_twos[1]
        third_element = list_of_twos[2]
        f_num = first_element[0].get_number()
        s_num = second_element[0].get_number()
        t_num = third_element[0].get_number()
        if(f_num < s_num and f_num < t_num):
            output = sort_pair(list_of_twos[1:])
        elif(s_num < f_num and s_num <t_num):
            output = sort_pair(list_of_twos[0::2])
        else:
            output = sort_pair(list_of_twos[:2])
    return output
 
def get_three_kind(cards):
    #Tallies up all the numbers in a set of cards
    numbers = Counter([card.get_number() for card in cards])
    three_kind_list = []
    for number in numbers:
        if(numbers[number] == 3):
            three_kind_list += [card for card in cards if card.get_number() == number]
    if len(three_kind_list) > 0:
        return three_kind_list
 
def get_straight(cards):
    converted_cards = [card_primes[card.number-2] for card in cards]
    converted_card_product = functools.reduce(lambda x,y: x*y, converted_cards)
    for straight in unique_straights[::-1]:
        if converted_card_product % straight == 0:
            unique_numbers = []
            final_list = []
            for card in cards:
                if straight % card_primes[card.number-2] == 0 and card.number not in unique_numbers:
                    final_list.append(card)
                    unique_numbers.append(card.number)
            return final_list
            break
        
def straight_value(cards):
    converted_cards = [card_primes[card.number-2] for card in cards]
    converted_card_product = functools.reduce(lambda x,y: x*y, converted_cards)
    for straight in unique_straights[::-1]:
        if converted_card_product % straight == 0:
            return unique_straights.index(straight)
         
#Gets all cards that are part of a flush and returns them in sorted order
def get_flush(cards):
    suits = [card.get_suit() for card in cards]
    flush_type = None
    for elem in Counter(suits):
        if Counter(suits)[elem] > 4:
            flush_type = elem
            flush = sort_by_number([card for card in cards if card.get_suit() == flush_type])
            return flush
 
def get_full_house(cards):
    threes = get_three_kind(cards)
    if threes != None:
        if len(threes) == 6:
            if(threes[0].get_number() > threes[5].get_number()):
                return threes[0:3] + threes[3:5]
            else:
                return threes[3:]+threes[0:2]
        elif len(threes) == 3:
            non_three_kind = [card for card in cards if card.get_number() != threes[0].get_number()]
            if(get_two_pair(non_three_kind) != None):
                return threes+get_two_pair(non_three_kind)[0:2]
            elif(get_two_kind(non_three_kind) != None):
                return threes+get_two_kind(non_three_kind)
         
#Checks the hand for four of a kind and returns it
def get_four_kind(cards):
    numbers = [card.get_number() for card in cards]
    four_kind = ""
    for number in Counter(numbers):
        if Counter(numbers)[number] == 4:
            four_kind = number
            set_of_four = [card for card in cards if card.get_number() == four_kind]
            return set_of_four