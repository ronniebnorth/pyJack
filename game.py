from player import Player
from deck import Deck
from scoreboard import Scoreboard
from util import *

class Game:
    
    def __init__(self, numPlayers, numDecks):
        self.players = self.createPlayers(numPlayers)
        self.numDecks = numDecks
        self.deck = Deck(numDecks)
        self.scoreboard = Scoreboard()

    def createPlayers(self, numPlayers):
        players = []
        for i in range(numPlayers):
            players.append(Player())
        players.append(Player("dealer"))
        return players

    def getWinPercentage(self):
        return self.scoreboard.getWinPercentage()
    
    def deal(self):
        if(self.deck.getCount() < (self.deck.getStartCount() / 2)):
            self.deck = Deck(self.numDecks)
            
        for i in range(2):
            for player in self.players:
                player.addPoints(self.deck.getCard())
                
    def score(self):
        dealerPoints = getDealerPoints(self.players)
        dealerBlackjack = getDealerBlackjack(self.players)
        
        for player in getPlayers(self.players):
            score = 1
            if(player.hasBlackjack):
                score = 1.5
                
            points = player.getPoints()
            
            if(points > 21):
                points = 0
                
            if(dealerBlackjack):
                if(not player.hasBlackjack()):
                    points = 0    
                
            if(points > dealerPoints):
                self.scoreboard.incrementPlayerWins(score)
                
            elif(points == dealerPoints and player.hasBlackjack()):
                self.scoreboard.incrementPlayerWins(score)
                
            elif(points < dealerPoints or points == 0):
                self.scoreboard.incrementPlayerLoss()
                
            else:
                self.scoreboard.incrementPlayerTies()
    
    def resetPlayers(self):
        for player in self.players:
            player.reset()
            
    def processPlayers(self):
        upcard = getUpcard(self.players)
        for player in self.players:
            move = 'xxx'
            while move:
                move = player.getMove(upcard)
                if(move == "HIT" or move == "DOUBLE"):
                    player.addPoints(self.deck.getCard())
                
    
