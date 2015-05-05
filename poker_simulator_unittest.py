
'''
Created on Apr 23, 2015

@author: arilab
'''
import unittest
<<<<<<< HEAD
from p_simulator import valid_response

class TestPokerSimulator(unittest.TestCase):
        
    def test_responses(self):
        expected_response = 'CALL', 'CHECK', 'FOLD', 'RAISE'
        for response in expected_response:
            self.assertEqual(valid_response(response), True)
        self.assertEqual(valid_response('call'), True)
        self.assertEqual(valid_response('CaLl'), True)
        self.assertEqual(valid_response('Cal1'), False)
=======
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
>>>>>>> origin/master
        
if __name__ == '__main__':
    unittest.main()                                                 