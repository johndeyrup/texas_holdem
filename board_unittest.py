'''
Created on May 1, 2015

@author: arilab
'''
import unittest
from board import Board
from player import Player

class Test(unittest.TestCase):
            
    def test_board_shuffle(self):
        new_board = Board([1,2,3,4,5],10)
        new_board.shuffle_player_order()
        self.assertNotEqual([1,2,3,4,5],new_board.players,'not shuffled')
    
    def setUp(self):
        self.board = Board([Player("Play_one", 100), Player("Player_two",100)],10)
        self.multi_board = Board([Player("Play_one", 100), Player("Player_two",100), 
                                  Player('Player_three',100), Player('Player_four',100)],10)
            
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
        self.assertEqual(self.board.rotate_position([1,2]), [2,1])
        self.assertEqual(self.board.rotate_position([1,2,3]),[3,1,2])
        
    def test_flop(self):
        expected = self.board.deck.deck[1:4]
        self.board.add_flop()
        self.assertEqual(expected, self.board.community_cards, 'expected: %s \n community cards: %s' % 
                         ([card.get_properties() for card in expected], 
                          [card.get_properties() for card in self.board.community_cards]))
    
    def test_flop_turn_river(self):
        first_eight_cards = self.board.deck.deck[:8]
        expected = self.board.deck.deck[1:4] + [self.board.deck.deck[5]]+ [self.board.deck.deck[7]]
        self.board.add_flop()
        self.board.add_turn()
        self.board.add_river()
        self.assertEqual(expected,self.board.community_cards, '\n expected: %s \n community cards: %s \n deck draw: %s' %
                         ([card.get_properties() for card in expected],
                         [card.get_properties() for card in self.board.community_cards],
                         [card.get_properties() for card in first_eight_cards]))
        
    def test_deduct_blinds(self):
        self.board.deduct_blinds()
        #Second to last player has the big blind
        self.assertEqual(self.board.players[-2].bid, 10)
        self.assertEqual(self.board.players[-1].bid, 20)
        
    def test_deduct_blinds_all_money(self):
        #Blind bigger than players money
        self.board.blind = 110
        self.board.deduct_blinds()
        self.assertEqual(self.board.players[-2].bid, 100)
        
    def test_highest_bid(self):
        self.board.deduct_blinds()
        self.assertEqual(self.board.get_highest_bid(), 20, 'highest bid %s' % self.board.get_highest_bid())
        
    def test_all_bids_equal(self):
        self.assertFalse(self.board.all_bids_equal([1,2,3,4]))
        self.assertTrue(self.board.all_bids_equal([1,1,1,1,1]))
        
    def test_get_biggest_bid_between_players(self):
        self.board.deduct_blinds()
        self.board.get_greatest_bid(self.board.players[0].bid, self.board.players[1].bid)
        
    def test_win_by_fold(self):
        self.board.deduct_blinds()
        self.board.players[0].is_in_hand = False
        self.board.players[1].is_in_hand = True
        self.board.win_by_fold()
        self.assertEqual(self.board.players[0].bid,0)
        self.assertEqual(self.board.players[1].bid, 0)
        self.assertEqual(self.board.pot, 0)
        self.assertEqual(self.board.players[0].money, 90)
        self.assertEqual(self.board.players[1].money, 110)
    
    def test_multi_board(self):
        self.multi_board.players[0].is_in_hand = False
        self.multi_board.players[1].is_in_hand = True
        self.multi_board.players[2].is_in_hand = False
        self.multi_board.players[3].is_in_hand = False
        self.multi_board.players[0].bid = 10
        self.multi_board.players[1].bid = 20
        self.multi_board.players[2].bid = 30
        self.multi_board.players[3].bid = 20
        self.multi_board.pot = 80
        self.multi_board.win_by_fold()
        for player in self.multi_board.players:
            self.assertEqual(player.bid, 0, 'Player: %s, player money: %s' % (player.name, player.bid))
        self.assertEqual(self.multi_board.players[0].money,100) 
        self.assertEqual(self.multi_board.players[1].money,170)     
        self.assertEqual(self.multi_board.players[2].money, 110)
        self.assertEqual(self.multi_board.players[3].money, 100)
        self.assertEqual(self.multi_board.pot,0)
        
    def test_sort_player_ranking(self):
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
        test_board = Board(players, 10)
        test_board.pot = 50
        ranked_players = test_board.sort_player_rankings(test_board.players)
        test_board.assign_hand_win(ranked_players)
        self.assertEqual(p5.money, 170)
        self.assertEqual(test_board.pot, 0)
        for player in test_board.players:
            self.assertEqual(player.bid, 0)
            
    def test_bids_unequal(self):
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
        p1.bid = 10
        p2.bid = 20
        p3.bid = 40
        p4.bid = 15
        p5.bid = 30
        test_board = Board(players, 10)
        test_board.pot = 50
        ranked_players = test_board.sort_player_rankings(test_board.players)
        test_board.assign_hand_win(ranked_players)
        self.assertEqual(p5.money, 225)
        self.assertEqual(p3.money,110)
        self.assertEqual(test_board.pot, 0)
        for player in test_board.players:
            self.assertEqual(player.bid, 0)
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()