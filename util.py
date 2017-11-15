from deck import Deck



def getDealer(players):
    for player in players:
        if(player.getType() == 'dealer'):
            return player

def getPlayers(players):
    newPlayers = []
    for player in players:
        if(player.getType() != 'dealer'):
            newPlayers.append(player)
    return newPlayers

def getDealerPoints(players):
    for player in players:
        if(player.getType() == 'dealer'):
            return player.getPoints()

def getDealerBlackjack(players):
    for player in players:
        if(player.getType() == 'dealer'):
            return player.hasBlackjack()
        
def getUpcard(players):
    for player in players:
        if(player.getType() == 'dealer'):
            return player.getUpcard()

def getHardStrat(points, upcard):
    hardStrat = [
        [9,9,9,9,9,9,9,9,9,9],
        [9,9,9,9,9,9,9,9,9,9],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,3,3,3,3,0,0,0,0],
        [0,3,3,3,3,3,3,3,3,0],
        [0,3,3,3,3,3,3,3,3,3],
        [0,0,0,1,1,1,0,0,0,0],
        [0,1,1,1,1,1,0,0,0,0],
        [0,1,1,1,1,1,0,0,0,0],
        [0,1,1,1,1,1,0,0,0,0],
        [0,1,1,1,1,1,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1]    
    ]
    return hardStrat[points][upcard];
