
'''
Created on Apr 23, 2015

@author: arilab
'''
import unittest
from player import Player
import p_simulator

class TestPokerSimulator(unittest.TestCase):
        
    def test_two(self):
        self.assertEqual(2,2)
        
    def test_player_input(self):
        self.player = Player('bob', 100)
        print(self.player.money)
        
    def test_p_sim(self):
        self.assertEqual(p_simulator.get_input('hi'), 'hi')
        
if __name__ == '__main__':
    unittest.main()                                                 