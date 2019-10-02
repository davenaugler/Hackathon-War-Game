import random
SUITS = ["Hearts", "Diamonds", "Spades", "Clubs", ]
VALUES = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
          "Eight", "Nine", "Ten", "Jack", "Queen", "King"]


class Card:
    def __init__(self, suite, name, value):
        self.suite = suite
        self.value = value
        self.name = name
    
    def getCard(self):
        return "["+self.name+" of "+self.suite+"]"


class Deck:
    def __init__(self):
        self.deck = []
        self.reset()

    def printDeck(self):
        for i in range(0, 52):
            print(f"{self.deck[i].name} of {self.deck[i].suite}")

    def deal(self):
        ran = random.randint(0, (len(self.deck)-1))
        return self.deck.pop(ran)

    def shuffle(self):
        for i in range(0, 10000):
            for j in range(0, len(self.deck)):
                randomI = random.randint(0, (len(self.deck)-1))
                temp = self.deck[j]
                self.deck[j] = self.deck[randomI]
                self.deck[randomI] = temp

    def reset(self):
        self.deck = []
        for i in range(0, 4):
            for j in range(0, 13):
                self.deck.append(Card(SUITS[i], VALUES[j], j+1))
        self.shuffle()

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = []

    def printDeck(self):
        for c in self.deck:
            print(f"[{c.name} {c.suite}]")


    

    