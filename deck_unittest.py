'''
Created on May 1, 2015

@author: arilab
'''
import unittest
from deck import Deck

class TestPokerSimulator(unittest.TestCase):
    
    
    def test_deal_card(self):
        new_deck = Deck()
        self.assertEqual(new_deck.deck[0],new_deck.deal_card())
        
    def test_deck_length_after_deal(self):
        new_deck = Deck()
        new_deck.deal_card()
        self.assertEqual(len(new_deck.deck),51)
        
    def test_flop_length(self):
        new_deck = Deck()
        self.assertEqual(len(new_deck.do_flop()),3)
        
    def test_flop_cards(self):
        new_deck = Deck()
        self.assertEqual(new_deck.deck[1:4],new_deck.do_flop())
        
    def test_post_flop_deck_length(self):
        new_deck = Deck()
        new_deck.do_flop()
        self.assertEqual(len(new_deck.deck),48)
        
    def test_flop_river_turn(self):
        new_deck = Deck()
        expected_cards = [new_deck.deck[i] for i in [1,2,3,5,7]]
        output = new_deck.do_flop() + [new_deck.do_turn()] + [new_deck.do_turn()]
        self.assertEqual(expected_cards, output)