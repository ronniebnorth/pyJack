class Player:
    playerCount = 0
    
    def __init__(self,type="player"):
        Player.playerCount += 1
        self.id = Player.playerCount
        self.type = type
        self.points = 0
        self.aces = 0
        self.blackjack = False
        self.canSplit = False
        self.doubled = False

    def addPoints(self, points):
        print("adding points to " + self.type + "  " + str(points))
            
        if(points == 11):
            self.aces += 1
            
        self.points += points
        
        if(self.points > 21 and self.aces > 1):
            self.points -= 10
            self.aces -= 1
    
    def setPoints(self, points):
        self.points = points
        
    def getMove(self, upcard):
        
        if(self.points > 21):
            return False
        
        if(self.doubled):
            return False
        
        if(self.type == "dealer"):
            if(self.points < 17):
                return 'HIT'
            else:
                return False
        
        if(upcard == 11):
            upcard = 1
         
        rw = self.points
        strat = 0
        if(self.aces > 0):
            rw -= 10
            strat = self.getSoftStrat(rw-1, upcard-1)
        else:
            strat = self.getHardStrat(rw-1, upcard-1)
            
        print("strat = " + str(strat) + "  points = " + str(self.points) + "  upcard = " + str(upcard))
        
        if(strat == 0 or strat == 3):
            print("hitting")
            return 'HIT'
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
        
    def getHardStrat(self, points, upcard):
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
        return hardStrat[points][upcard]

    def getSoftStrat(self, points, upcard):
        softStrat = [
            [9,9,9,9,9,9,9,9,9,9],
            [0,0,0,0,0,3,0,0,0,0],
            [0,0,0,0,3,3,0,0,0,0],
            [0,0,0,0,3,3,0,0,0,0],
            [0,0,0,3,3,3,0,0,0,0],
            [0,0,0,3,3,3,0,0,0,0],
            [0,0,3,3,3,3,0,0,0,0],
            [0,1,3,3,3,3,1,1,0,0],
            [1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1],
            [9,9,9,9,9,9,9,9,9,9],
            [9,9,9,9,9,9,9,9,9,9],
            [9,9,9,9,9,9,9,9,9,9],
            [9,9,9,9,9,9,9,9,9,9],
            [9,9,9,9,9,9,9,9,9,9],
            [9,9,9,9,9,9,9,9,9,9],
            [9,9,9,9,9,9,9,9,9,9],
            [9,9,9,9,9,9,9,9,9,9],
            [9,9,9,9,9,9,9,9,9,9],
            [0,0,0,0,0,0,0,0,0,0]
        ]
        return softStrat[points][upcard]
