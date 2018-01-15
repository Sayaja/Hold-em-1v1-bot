# A class that represents a players hand. It also containts the possible actions a player can take

from Deck import Deck as Deck
from Card import Card as Card
from Board import Board as Board

class Hand:
    def __init__(self, deck, chips): # Creates the starting hand
        card1 = deck.dealCard()
        card2 = deck.dealCard()
        self.hand = [card1, card2]
        self.chips = chips
        self.currentBet = 0

    def bet(self): # Make a bet
        while:
            tempBet = int(input("How much do you want to bet? "))
            if tempBet < self.chips:
                self.chips = self.chips - tempBet
                break
            else:
                print("Too high bet.")
                pass

            return tempBet

    def fold(self): # Pass the turn
        print("Player folded.")
        action = "fold"
        return action

    def check(self): # Check the turn
        print("Player checked.")
        action = "check"
        return action

    def call(self, pot): # Call on the current pot
        if (pot-self.currentBet) < self.chips:
            print("Player called.")
            tempCall = pot - self.currentBet
            self.currentBet = self.currentBet + tempCall
            self.chips = self.chips - tempCall
            return tempCall
        else:
            print("Player is all in.")
            tempCall = self.chips
            self.currentBet = self.currentBet + tempCall
            self.chips = self.chips - tempCall
            return tempCall
            
    def newHand(self, deck):
        card1 = deck.dealCard()
        card2 = deck.dealCard()
        self.hand = [card1, card2] # New cards











        
