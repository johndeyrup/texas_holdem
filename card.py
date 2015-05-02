'''
Created on May 1, 2015

@author: arilab
'''

#Card class has properties suit and number
class Card:
    
    #Constructs variables in card object
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    
    #Returns suit
    def get_suit(self):
        return self.suit
    
    #Return number
    def get_number(self):
        return self.number
    
    #Returns number and suit
    def get_properties(self):
        return self.number, self.suit