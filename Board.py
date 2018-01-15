# A class the keeps track of the board state including the pot

from Card import Card as Card
from Deck import Deck as Deck

class Board:
    def __init__(self, deck): # Creates the board with 3 card objects dealt from the deck and the blinds
        card1 = deck.dealCard()
        card2 = deck.dealCard()
        card3 = deck.dealCard()
        self.board = [card1, card2, card3] # This is the flop
        self.pot = 0

    def addCard(self, deck): # Place a random card on the board
        tempCard = deck.dealCard()
        self.board.append(tempCard)

    def addBet(self, bet): # Add a bet to the pot
        self.pot = self.pot + bet

    def showBoard(self):
        for card in self.board:
            print(str(card.value) + card.suit + " ")
        print("The pot: " + str(self.pot))

    def newFlop(self, pot, deck):
        card1 = deck.dealCard()
        card2 = deck.dealCard()
        card3 = deck.dealCard()
        self.board = [card1, card2, card3] # The new flop
        self.pot = 0
    
