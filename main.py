from game import Game

NUM_PLAYERS = 1
NUM_DECKS = 8
NUM_ROUNDS = 1000

g = Game(NUM_PLAYERS, NUM_DECKS)

for i in range(NUM_ROUNDS):
    g.deal()
    g.processPlayers()
    g.scorePlayers()
    g.resetPlayers()
    
print(str(g.getWinPercentage()))


    

    



    

