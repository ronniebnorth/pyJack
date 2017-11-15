from random import shuffle

class Deck:
    
    def __init__(self,numDecks):
        self.cards = []
        for i in range(4 * numDecks):
            self.cards.extend([11,2,3,4,5,6,7,8,9,10,10,10,10])
        self.startCount = len(self.cards)
        shuffle(self.cards)
        
    def getStartCount(self):
        return self.startCount
    
    def getCount(self):
        return len(self.cards)
    
    def getCard(self):
        return self.cards.pop()

