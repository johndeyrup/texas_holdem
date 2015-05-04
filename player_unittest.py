'''
Created on May 4, 2015

@author: arilab
'''
import unittest
from unittest import mock
from player import Player


class Test(unittest.TestCase):


    def test_vald_response(self):
        player = Player('Player1',100)
        with mock.patch('builtins.input', side_effect=['fold', 'FOlD', 'FOLD', 'caLL', 'check', 'raise']):
            self.assertEqual(player.get_valid_input(),'FOLD')
            self.assertEqual(player.get_valid_input(),'FOLD')
            self.assertEqual(player.get_valid_input(),'FOLD')
            self.assertEqual(player.get_valid_input(),'CALL')
            self.assertEqual(player.get_valid_input(),'CHECK')
            self.assertEqual(player.get_valid_input(), 'RAISE')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()