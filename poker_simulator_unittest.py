
'''
Created on Apr 23, 2015

@author: arilab
'''
import unittest
import p_simulator

class TestPokerSimulator(unittest.TestCase):
    
    def test_input(self):
        self.assertEqual(p_simulator.get_player_input('test'),'test')
        
    def test_two(self):
        self.assertEqual(1,2)
        
if __name__ == '__main__':
    unittest.main()                                                 