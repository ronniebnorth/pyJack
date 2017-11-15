from util import *

class Player:
    playerCount = 0
    
    def __init__(self,type="player"):
        Player.playerCount += 1
        self.id = Player.playerCount
        self.type = type
        self.points = 0
        self.upcard = 0
        self.aces = 0
        self.blackjack = False
        self.canSplit = False
        self.doubled = False

    def addPoints(self, points):
        print("adding points " + str(points))
        
        if(self.points != 0 and self.type == 'dealer'):
            self.upcard = points
        if(points == self.points):
            self.canSplit = True
        if(points == 11):
            self.aces += 1
        self.points += points
        if(self.points > 21):
            self.points = 12
            self.aces -= 1
    
    def setPoints(self, points):
        self.points = points
        
    def getMove(self, upcard):
        if(self.doubled):
            return False
        if(self.type == "dealer"):
            if(self.points < 17):
                return 'HIT'
            else:
                return False
        
        if(upcard == 11):
            upcard = 1
            
        strat = getHardStrat(self.points-1, upcard-1)
        print("strat = " + str(strat) + "  points = " + str(self.points) + "  upcard = " + str(upcard))
        
        if(strat == '0' or strat == '3'):
            return 'HITs'
        else:
            return False
    
    def reset(self):
        self.points = 0
        self.upcard = 0
        self.aces = 0
        self.blackjack = False
        self.canSplit = False
        self.doubled = False
        
    def getCount(self):
        return Player.playerCount
    
    def getUpcard(self):
        return self.upcard
    
    def getType(self):
        return self.type
    
    def getPoints(self):
        return self.points
    
    def hasBlackjack(self):
        return self.blackjack
    
    def canSplit(self):
        return self.canSplit
    
    def hasDoubled(self):
        return self.doubled
        
    def setBlackjack(self, v):
        self.blackjack = v
        
    def setCanSplit(self, v):
        self.canSplit = v
        
    def setDoubled(self, v):
        self.doubled = v
        
    def removeAce(self):
        self.aces -= 1
 