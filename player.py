'''
Created on May 1, 2015

@author: arilab
'''
#Player has position from the dealer, cash, cards, a current bid, and whether they are still playing the hand
class Player:
    
    #Constructs variables in player object
    def __init__(self, name, money):
        self.money = money
        self.cards = []
        self.bid = 0
        self.is_in_hand = False
        self.name = name
        self.hand_value = 0
        
    def get_player_input(self,prompt):
        player_input = input(prompt)
        return player_input
            
    def get_valid_input(self):
        valid_response = 'CALL', 'CHECK', 'FOLD', 'RAISE'
        player_response = self.get_player_input("%s: Please enter call, check, fold, or raise" % self.name).upper()
        while player_response not in valid_response:
            player_response = self.get_player_input("I am sorry you did not enter a valid action, please type call, check, fold, or raise").upper()
        else:
            return player_response
    
    #Returns all stats
    def get_stats(self):
        stats = [self.name, self.bid, self.money, self.is_in_hand]
        for card in self.cards:
            stats.append(card.get_properties())
        return stats