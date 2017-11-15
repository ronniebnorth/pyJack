from game import Game
from player import Player
from deck import Deck
from util import *

NUM_PLAYERS = 1
NUM_DECKS = 8
NUM_ROUNDS = 100

g = Game(NUM_PLAYERS, NUM_DECKS)

for i in range(NUM_ROUNDS):
    g.deal()
    g.processPlayers()
    g.score()
    g.resetPlayers()
    
print(str(g.getWinPercentage()))


    

    



    

