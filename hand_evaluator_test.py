'''
Created on May 7, 2015

@author: arilab
'''
import unittest
import hand_evaluator
from card import Card
import itertools


class Test(unittest.TestCase):
    
    def setUp(self):
        self.straight_flush = [Card('heart', 2), Card('heart', 3), Card('heart', 4), Card('heart', 5), Card('heart', 6)]
        self.four_kind = [Card('heart', 3), Card('diamond', 3), Card('spade', 3), Card('club', 3), Card('heart', 2)]
        self.full_house = [Card('heart', 3), Card('diamond', 3), Card('spade', 3), Card('club', 2), Card('heart', 2)]
        self.flush = [Card('heart', 2), Card('heart', 3), Card('heart', 4), Card('heart', 5), Card('heart', 9)]
        self.straight = [Card('heart', 2), Card('heart', 3), Card('heart', 4), Card('heart', 5), Card('spade', 6)]
        self.three_kind = [Card('heart', 3), Card('diamond', 3), Card('spade', 3), Card('club', 2), Card('heart', 14)]
        self.two_pair = [Card('heart', 3), Card('diamond', 14), Card('spade', 3), Card('club', 2), Card('heart', 2)]
        self.one_pair = [Card('heart', 3), Card('diamond', 14), Card('spade', 3), Card('club', 12), Card('heart', 2)]
        self.high_card = [Card('heart', 8), Card('diamond', 14), Card('spade', 3), Card('club', 12), Card('heart', 2)]


    def test_sort_by_number(self):
        expected_high_card = [14,12,8,3,2]
        ranked_observed = [card.number for card in hand_evaluator.sort_by_number(self.high_card)]
        #One way to check if two lists are equal
        for x,y in zip(expected_high_card,ranked_observed):
            self.assertEqual(x,y, 'rank for %s and %s is incorrected' % (x,y))
        #Another way to check if two lists are equal
#         four_kind_rank = [3,3,3,3,2]
#         four_kind_observed = [card.number for card in hand_evaluator.sort_by_number(self.four_kind)]
#         print(list(map(self.assertEqual,four_kind_rank,four_kind_observed)))
        #A thrid way to check if two lists are equal
        straight_rank = [6,5,4,3,2]
        straight_observed = [card.number for card in hand_evaluator.sort_by_number(self.straight)]
        self.assertEqual(straight_rank, straight_observed)
        
    def test_get_card_value(self):
        expected = .1412080302
        sorted_hand = hand_evaluator.sort_by_number(self.high_card)
        self.assertAlmostEqual(hand_evaluator.get_card_value(sorted_hand), expected)
        
        one_pair_truncated_expected = .140303
        sorted_one_pair = hand_evaluator.sort_by_number(self.one_pair[0:3])
        self.assertAlmostEqual(hand_evaluator.get_card_value(sorted_one_pair),one_pair_truncated_expected)
        
    def test_straight(self):
        self.straight_ace_low = [Card('heart', 2), Card('heart', 3), Card('heart', 4), Card('heart', 5), Card('spade', 14), Card('diamond', 14), Card('diamond', 14)]
        self.multiple_straights = [Card('heart', 8), Card('heart', 3), Card('heart', 4), Card('heart', 5), Card('spade', 6), Card('diamond', 7), Card('diamond', 8)]
        self.assertEqual(hand_evaluator.straight_value(self.straight),1)
        self.assertEqual(hand_evaluator.straight_value(self.straight_ace_low),0)
        self.assertEqual(hand_evaluator.straight_value(self.multiple_straights),3)
        
    def test_best_hand_value(self):
        value, cards = hand_evaluator.find_best_hand([Card('heart', 14), Card('spade', 14)], self.straight_flush)
        self.assertEqual(value, 9.1)
        value, cards = hand_evaluator.find_best_hand([Card('heart', 14), Card('spade', 14)], self.four_kind)
        self.assertEqual(value, 8.0314)
        value, cards = hand_evaluator.find_best_hand([Card('heart', 14), Card('spade', 14)], self.full_house)
        self.assertAlmostEqual(value, 7.0314)
        value, cards = hand_evaluator.find_best_hand([Card('heart', 13), Card('spade', 14)], self.flush)
        self.assertAlmostEqual(value, 6.1309050403)
        value, cards = hand_evaluator.find_best_hand([Card('diamond', 14), Card('spade', 14)],self.straight)
        self.assertEqual(value, 5.1)
        value, cards = hand_evaluator.find_best_hand([Card('heart', 13), Card('spade', 12)], self.three_kind)
        self.assertAlmostEqual(value, 4.031413)
        value, cards = hand_evaluator.find_best_hand([Card('heart', 14), Card('spade', 12)], self.two_pair)
        self.assertAlmostEqual(value, 3.140312)
        value, cards = hand_evaluator.find_best_hand([Card('heart', 13), Card('spade', 8)], self.one_pair)
        self.assertAlmostEqual(value, 2.03141312)
        value, cards = hand_evaluator.find_best_hand([Card('heart', 13), Card('spade', 9)], self.high_card)
        self.assertAlmostEqual(value, 1.1413120908)     

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_']
    unittest.main()