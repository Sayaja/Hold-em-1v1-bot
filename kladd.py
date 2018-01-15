from random import randint
from Deck import Deck as Deck

d = Deck()
b = d
b.dealCard()
print(len(b.deck))
print(len(d.deck))

