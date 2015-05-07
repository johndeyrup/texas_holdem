
'''
Created on Apr 23, 2015

@author: arilab
'''
import unittest
from player import Player
import p_simulator as psim

class TestPokerSimulator(unittest.TestCase):
    
    def test_one(self):
        p1 = Player('p1',100)
        p2 = Player('p2', 100)
        p3 = Player('p3', 100)
        p4 = Player('p4', 100)
        p5 = Player('p5', 120)
        p1.hand_value = 10
        p2.hand_value = 8.1
        p3.hand_value = 8.2
        p4.hand_value = 11
        p5.hand_value = 12
        players = [p1,p2,p3,p4,p5]
        for player in players:
            player.bid = 10
        sorted_players = psim.sort_player_rankings(players)
#         for player in sorted_players:
#             print(player[0].get_stats())
        psim.assign_hand_win(sorted_players)
        
        
        
#         for k,g in psim.sort_player_rankings(players):
#             print(k)
#             sorted_list.append(list(g))
#         for group in sorted_list:
#             for player in group:
#                 print(group)
#                 print(player.hand_value)
#         for player in psim.sort_player_rankings(players):
#             print(player.get_stats())
        
    
        
if __name__ == '__main__':
    unittest.main()                                                 