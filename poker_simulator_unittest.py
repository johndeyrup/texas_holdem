
'''
Created on Apr 23, 2015

@author: arilab
'''
import unittest
from p_simulator import valid_response

class TestPokerSimulator(unittest.TestCase):
        
    def test_responses(self):
        expected_response = 'CALL', 'CHECK', 'FOLD', 'RAISE'
        for response in expected_response:
            self.assertEqual(valid_response(response), True)
        self.assertEqual(valid_response('call'), True)
        self.assertEqual(valid_response('CaLl'), True)
        self.assertEqual(valid_response('Cal1'), False)
        
if __name__ == '__main__':
    unittest.main()                                                 