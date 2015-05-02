'''
Created on May 1, 2015

@author: arilab
'''
from card import Card
from random import shuffle

class Deck:
    
    def __init__(self):
        self.deck = []
        self.create_deck()
        self.shuffle_deck()
        
    def create_deck(self):
        card_numbers = [x for x in range(2,15)]
        card_suits = ['Heart', 'Spade', 'Diamond', 'Club']
        for number in card_numbers:
            for suit in card_suits:
                self.deck.append(Card(suit, number))
                
    def shuffle_deck(self):
        shuffle(self.deck)
    
    def deal_card(self):
        return self.deck.pop(0)
    
    def burn_card(self):
        self.deck.pop(0)
        
    #Burn a card and return the next three cards
    def do_flop(self):
        self.burn_card()
        return [self.deal_card() for i in range(3)]
    
    #Both the river and the turn do the same thing so will be called same method
    def do_turn(self):
        self.burn_card()
        return self.deal_card()