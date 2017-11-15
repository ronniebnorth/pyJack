class Scoreboard:
    def __init__(self):
        self.playerWins = 0
        self.playerLoss = 0
        self.playerTies = 0
    def incrementPlayerWins(self, points):
        self.playerWins += points
    def incrementPlayerLoss(self):
        self.playerLoss += 1
    def incrementPlayerTies(self):
        self.playerTies += 1
    def getPlayerWins(self):
        return self.playerWins
    def getPlayerLoss(self):
        return self.playerLoss
    def getPlayerTies(self):
        return self.playerTies
    def getWinPercentage(self):
        return self.playerWins / (self.playerWins + self.playerLoss) * 100