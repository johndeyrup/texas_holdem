'''
Created on May 1, 2015

@author: arilab
'''
import unittest
from board import Board
from player import Player

class Test(unittest.TestCase):

    def test_board_shuffle(self):
        new_board = Board([1,2,3,4,5])
        new_board.shuffle_player_order()
        self.assertNotEqual([1,2,3,4,5],new_board.players,'not shuffled')
        
    def test_dealt_two_cards(self):
        new_board = Board([Player("Play_one", 100), Player("Player_two",100)])
        new_board.deal_cards()
        for player in new_board.players:
            self.assertEqual(len(player.cards), 2, '%s doesn\'t have two cards' % player.name)
        
    def test_cards_dealt_correct(self):
        new_board = Board([Player("Play_one", 100), Player("Player_two",100)])
        #This is a little ridiculous
        expected_cards = [[new_board.deck.deck[0],new_board.deck.deck[2]],[new_board.deck.deck[1],new_board.deck.deck[3]]]
        new_board.deal_cards()
        position = 0
        for player in new_board.players:
            print(player.cards)
            self.assertEqual(player.cards, expected_cards[position], 'Cards not dealt properly')
            position += 1
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()