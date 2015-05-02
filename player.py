'''
Created on May 1, 2015

@author: arilab
'''
#Player has position from the dealer, cash, cards, a current bid, and whether they are still playing the hand
class Player:
    
    #Constructs variables in player object
    def __init__(self, name, money):
        self.position = None
        self.money = money
        self.cards = []
        self.bid = 0
        self.is_in_hand = False
        self.name = name
        self.hand_value = 0
        
    #Return position from the dealer, the dealer is 0, and to the left is 1, and so forth
    def get_position(self):
        return self.position
    
    #Returns how much money a player has
    def get_money(self):
        return self.money
    
    #Returns cards in players hand
    def get_cards(self):
        return self.cards
    
    #Returns bid
    def get_bid(self):
        return self.bid
    
    #Returns true if the player has not folded
    def get_in_hand(self):
        return self.is_in_hand
    
    #Returns all stats
    def get_stats(self):
        stats = [self.name, self.bid, self.money, self.position, self.is_in_hand]
        for card in self.cards:
            stats.append(card.get_properties())
        return stats
    
    #Returns a player's hand value, hands are ranked 1-9 with straight flush as 9 and a high card as 1
    #Additional cards are stored in the value so four 8s plus and an ace would be 8.0804
    def get_hand_value(self):
        return self.hand_value
    
    #Updates player bid
    def update_bid(self, bid_amount):
        self.bid += bid_amount
        
    #Updates player money
    def update_money(self, amount):
        self.money += amount
        
    #Updates player hand value, used to determine hand rankings
    def update_hand_value(self, value):
        self.hand_value = value