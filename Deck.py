# A class that represents the deck the game uses

from Card import Card as Card
from random import randint

class Deck:
    def __init__(self): # Create the starting deck
        self.suits = ["hearts", "diamonds", "spades", "clubs"]
        self.deck = [Card(value, suit) for value in range(1,14) for suit in self.suits]
    
    def shuffle(self): # Restore the deck to starting point
        self.deck = [Card(value, suit) for value in range(1,14) for suit in self.suits]

    def dealCard(self): # Deals a random card from the deck
        num = randint(0, len(self.deck)-1)
        tempCard = self.deck[num]
        del self.deck[num] # Remove the card from the deck

        #print(tempCard.value, tempCard.suit)
        return tempCard # Returns the dealt card
        
