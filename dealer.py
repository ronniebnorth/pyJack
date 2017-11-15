class Dealer:
    def __init__(self):
        self.points = 0
        self.blackjack = False
    def getPoints(self):
        return self.points
    def hasBlackjack(self):
        return self.blackjack
    def addPoints(self, points):
        self.points = points
        