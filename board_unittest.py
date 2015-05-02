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
    
    def setUp(self):
        self.board = Board([Player("Play_one", 100), Player("Player_two",100)])
            
    def test_dealt_two_cards(self):
        self.board.deal_cards()
        for player in self.board.players:
            self.assertEqual(len(player.cards), 2, '%s doesn\'t have two cards' % player.name)
        
    def test_cards_dealt_correct(self):
        #This is a little ridiculous
        expected_cards = [[self.board.deck.deck[0],self.board.deck.deck[2]],[self.board.deck.deck[1],self.board.deck.deck[3]]]
        self.board.deal_cards()
        position = 0
        for player in self.board.players:
            self.assertEqual(player.cards, expected_cards[position], 'Cards not dealt properly')
            position += 1
        
    
    def test_do_bid_pot_size(self):
        for player in self.board.players:
            self.assertEqual(player.bid, 0)
            self.board.do_bid(player, 10)
            self.assertEqual(player.bid, 10)
        self.assertEqual(self.board.pot, len(self.board.players)*10, 'pot size not equal to players bid')
    
    #Check if pot size, player money, and player bid are updated correctly if bid is more than player money     
    def test_bid_greater_than_money(self):
        for player in self.board.players:
            self.board.try_bid(player, 110)
            self.assertEqual(player.bid, 100)
            self.assertEqual(player.money,0)
        self.assertEqual(self.board.pot, 200)

    def test_bid_equal_to_money(self):
        for player in self.board.players:
            self.board.try_bid(player, 100)
            self.assertEqual(player.bid,100)
            self.assertEqual(player.money, 0)
        self.assertEqual(self.board.pot, 200)
    
    def test_return_bid(self):
        for player in self.board.players:
            self.board.try_bid(player, 10)
        for player in self.board.players:
            previous_pot = self.board.pot
            self.board.return_bid(player)
            self.assertEqual(player.bid,0)
            self.assertEqual(player.money, 100)
            self.assertEqual(self.board.pot, previous_pot-10)
            
    def test_rotate_players(self):
        self.assertEqual(self.board.rotate_position([1,2,3,4,5]), [5,1,2,3,4])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()