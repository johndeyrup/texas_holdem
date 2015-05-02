
'''
Created on Apr 23, 2015

@author: arilab
'''
# import unittest
# from p_simulator import *
#  
# class TestPokerSimulator(unittest.TestCase):
#      
#     #Winner: first parameter gets up to the amount he put in, but not more than the loser's bid
#     def test_get_highest_valid_bid(self):
#         self.assertEqual(bid_greater_equal(4,3),3)
#         self.assertEqual(bid_greater_equal(3,4),3)
#         self.assertEqual(bid_greater_equal(3,3),3)
#          
#          
#     def test_take_winings(self):
#         board_test = Board([Player('bob',1,40,[],40,True), Player('brob',2,0,[],50,True)], [], 90)
#         winner = board_test.get_players()[0]
#         loser = board_test.get_players()[1]
#         amount = bid_greater_equal(winner.get_bid(), loser.get_bid())
#         self.assertEqual(amount,40)
#         update_winnings(board_test, winner, loser, amount)
#         self.assertEqual(winner.get_money(), 80)
#         self.assertEqual(board_test.get_pot(), 50)
#         self.assertEqual(loser.get_bid(),10)
#      
#     def test_assign_winnings(self):
#         assign_winnings([Player('bob',1,40,[],40,True), Player('brob',2,0,[],50,True)])
#          
# if __name__ == '__main__':
#     unittest.main()                                                 