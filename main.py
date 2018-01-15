# This runs the game

from random import randint

from Deck import Deck as Deck
from Card import Card as Card
from Board import Board as Board
from Hand import Hand as Hand

def main():
    bigBlind = 10
    smallBlind = 5
    deck = Deck() # Initiate the deck
    hand1 = Hand(deck, 100) # Initiate the hands for both players. 100 in starting chips
    hand2 = Hand(deck, 100)
    board = Board(deck) # Initiate the board
    
    num = randint(0,1) # Decide who starts as dealer
    if num == 0:
        dealer = hand1
    else:
        dealer = hand2

    if dealer == hand1: # hand1 is the dealer
        hand1.chips = hand1.chips - bigBlind
        hand2.chips = hand2.chips - smallBlind
    else: # hand2 is the dealer
        hand1.chips = hand1.chips - smallBlind
        hand2.chips = hand2.chips - bigBlind
    board.pot = bigBlind + smallBlind # The starting pot with the blinds

    board.showBoard() # Print the board and current pot
##    if dealer == hand1:
##        print("Hand 1 action.")
##    else:
##        print("Hand 2 action.")
##    action = input("Input your action (check, call, fold, bet): ")
##    if action == "check":
##        
        


main()
