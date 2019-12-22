# This runs the game

from random import randint

from Deck import Deck as Deck
from Card import Card as Card
from Board import Board as Board
from Hand import Hand as Hand

def main():
    board = Board(10, 5) # Initiate the board

    board.showBoard() # Print the board and current pot
##    if dealer == hand1:
##        print("Hand 1 action.")
##    else:
##        print("Hand 2 action.")
##    action = input("Input your action (check, call, fold, bet): ")
##    if action == "check":
##        
        


main()
