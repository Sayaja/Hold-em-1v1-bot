# A class the keeps track of the board state, including: pot, blinds, dealer, cards, player turn, hands, deck

from random import randint

from Card import Card as Card
from Deck import Deck as Deck
from Hand import Hand as Hand

class Board:
    def __init__(self, bigBlind, smallBlind): # Creates the board with 3 card objects dealt from the deck and the blinds
        self.deck = Deck() # Initiate the deck
        self.hand1 = Hand(self.deck, 100) # Initiate the hands for both players. 100 in starting chips
        self.hand2 = Hand(self.deck, 100)
        self.cards = [self.deck.dealCard(), self.deck.dealCard(), self.deck.dealCard()] # This is the flop
        self.bigBlind = bigBlind
        self.smallBlind = smallBlind
        self.pot = self.bigBlind + self.smallBlind

        num = randint(0,1) # Decide who starts as dealer
        if num == 0:
            self.dealer = "hand1"
        else:
            self.dealer = "hand2"

    def addCard(self): # Place a random card on the board
        tempCard = self.deck.dealCard()
        self.cards.append(tempCard)

    def addBet(self, bet): # Add a bet to the pot
        self.pot += bet

    def showBoard(self):
        for card in self.cards:
            print(str(card.value) + " " + card.suit)
        print("The pot: " + str(self.pot))

    def newFlop(self):
        self.deck.shuffle

        if self.dealer == "hand1":
            self.dealer = "hand2"
            self.hand1.chips -= self.smallBlind
            self.hand2.chips -= self.bigBlind
        else:
            self.dealer = "hand1"
            self.hand1.chips -= self.bigBlind
            self.hand2.chips -= self.smallBlind

        self.cards = [self.deck.dealCard(), self.deck.dealCard(), self.deck.dealCard()] # The new flop
        self.pot = self.bigBlind + self.smallBlind
    
