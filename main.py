import random
import handcheck
deck = []
player1cards = []
player2cards = []
board = []
players = []

class Card:
    def __init__(self, name, value, suit):
        self.name = name
        self.value = value
        self.suit = suit
    def __repr__(self):
        return str(self.name+self.suit)
class Deck:
    def __init__(self):
        self.order = []
        self.suits = ['h', 's', 'd', 'c']
        self.names = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13,
             'A': 14}
        for n in self.names:
            for s in self.suits:
                self.order.append(Card(n, self.names[n], s))
    def shuffle(self):
        random.shuffle(self.order)
    def deal(self):
        for x in range(0,2):
            player1.holecards.append(self.order.pop(0))
            player2.holecards.append(self.order.pop(0))
    #for fun palimy karte przed wylozeniem flopa, turna i rivera tak jak sie robi na live gierkach
        self.order.pop(0)
        board.append(self.order.pop(0))
        board.append(self.order.pop(0))
        board.append(self.order.pop(0))
        self.order.pop(0)
        board.append(self.order.pop(0))
        self.order.pop(0)
        board.append(self.order.pop(0))
class Player:
    def __init__(self):
        self.holecards = []
        self.names = []
        self.values = []
        self.suits = []
        self.flushCards = []
        self.flushnames = []
        self.straightCards = set()
        self.pairvalue = 0
        self.twopairvalues = []
        self.tripsvalue = 0
        self.straightvalue = 0
        self.boatvalues = []
        self.quadvalue = 0
        self.handDetails = []
        self.bigScore = 0
        self.smallScore = 0
        players.append(self)
    def convert(self):
        self.values = []
        self.hand = self.holecards + board
        for x in range(0,len(self.hand)):
            self.names.append(str(self.hand[x].name))
            self.suits.append(str(self.hand[x].suit))
        for y in self.names:
            self.values.append(talia.names[y])
        self.values.sort(reverse=True)
        self.twopairvalues.sort(reverse=True)
        for x in self.flushCards:
            self.flushnames.append(x.name)
        return self.hand
    def checkScore(self):
        bigScore = handcheck.wynik(self)
        return bigScore
    def checkSmallScore(self):
        if self.checkScore() == 9:
            self.smallScore = self.handDetails[0]
        elif self.checkScore() == 8:
            self.smallScore = self.handDetails[0] * 10000 + self.handDetails[4]
        elif self.checkScore() == 7:
            self.smallScore = self.handDetails[0] * 10000 + self.handDetails[4]
        elif self.checkScore() == 6:
            self.smallScore = self.handDetails[0].value * 10000 + self.handDetails[1].value * 1000 + self.handDetails[2].value * 100 + self.handDetails[3].value * 10 + self.handDetails[4].value
        elif self.checkScore() == 5:
            self.smallScore = self.handDetails
        elif self.checkScore() == 4:
            self.smallScore = self.handDetails[0] * 10000 + self.handDetails[3] + self.handDetails[4]
        elif self.checkScore() == 3:
            self.smallScore = self.handDetails[0] * 10000 + self.handDetails[2] * 1000 + self.handDetails[4]
        elif self.checkScore() == 2:
            self.smallScore = self.handDetails[0] * 10000 + self.handDetails[2] * 1000 + self.handDetails[3] * 10 + self.handDetails[4]
        elif self.checkScore() == 1:
            self.smallScore = self.handDetails[0] * 10000 + self.handDetails[1] * 1000 + self.handDetails[2] * 100 + self.handDetails[3] * 10 + self.handDetails[4]
        return self.smallScore






player1 = Player()
player2 = Player()
talia = Deck()
talia.shuffle()
#print(talia.order)
#talia.deal()
#for x in range(1,3):
#    karta = input("Podej karte gracza 1: ")
#    obiektKarta = Card(karta[0],talia.names[karta[0]],karta[-1])
#    player1.holecards.append(obiektKarta)
#for x in range(1,3):
#    karta = input("Podej karte gracza 2: ")
#    obiektKarta = Card(karta[0],talia.names[karta[0]],karta[-1])
#    player2.holecards.append(obiektKarta)
board.append(Card('8',8,'d'))
board.append(Card('9',9,'c'))
board.append(Card('7',7,'d'))
board.append(Card('T',10,'d'))
board.append(Card('K',13,'s'))
player1.holecards.append((Card('A',14,'c')))
player1.holecards.append((Card('Q',12,'s')))
player2.holecards.append((Card('6',6,'h')))
player2.holecards.append((Card('K',13,'d')))




print("Board:",board)
print("Player 1's cards:",player1.holecards)
print("Player 2's cards:",player2.holecards)

player1.convert()
player2.convert()
print("Player 1 has",handcheck.handToName(player1))
print("Player 2 has",handcheck.handToName(player2))

handcheck.handDetails(player1)
handcheck.handDetails(player2)


print("----------WYNIK:----------")

if player1.checkScore() > player2.checkScore():
    print("Gracz nr 1 wygrywa talon na kurwe i balon!")
elif player1.checkScore() < player2.checkScore():
    print("Gracz nr 2 wygrywa talon na kurwe i balon!")
elif player1.checkScore() == player2.checkScore():
    if player1.checkSmallScore() > player2.checkSmallScore():
        print("Gracz nr 1 wygrywa talon na kurwe i balon!")
    elif player1.checkSmallScore() < player2.checkSmallScore():
        print("Gracz nr 2 wygrywa talon na kurwe i balon!")
    elif player1.checkSmallScore() == player2.checkSmallScore():
        print("REMIS")
    else:
        print("ERROR")
else:
    print("ERROR")


print("----------GLUPOTKI DLA MNIE DO TESTOW----------")
print("P1 Big score:",player1.checkScore())
print("P1 Small score:",player1.checkSmallScore())
print("P1 exact hand:",player1.handDetails)

print("P2 Big score:",player2.checkScore())
print("P2 Small score:",player2.checkSmallScore())
print("P2 exact hand:",player2.handDetails)




#print("---------JESZCZE WIECEJ GLUPOT DLA MNIE----------")
#print("P1 Big score:",player1.checkScore())
#print("P1 Small score:",player1.checkSmallScore())

#print("P2 Big score:",player2.checkScore())
#print("P2 Small score:",player2.checkSmallScore())

#print("p1 hand:",player1.hand)
#print("p1 values:",player1.values)
#print("p1 straightcards:",player1.straightCards)

#print("p1 flushcards:",player1.flushCards)
#print("p1 2pvalues",player1.twopairvalues)
#print("p1 str8 highcard",player1.straightvalue)
#print("P1 exact hand:",player1.handDetails)

#print("p2 hand:",player2.hand)
#print("p2 values:",player2.values)
#print("p2 straightcards:",player2.straightCards)

#print("p2 flushcards:",player2.flushCards)
#print("p2 2pvalues",player2.twopairvalues)
#print("p2 str8 highcard",player2.straightvalue)
#print("p2 exact hand:",player2.handDetails)

