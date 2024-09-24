import random

NUMCARDS = 52
RANKNAME = ("Ace", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Jack", "Queen", "King")

SUITNAME = ("clubs", "hearts", "spades", "diamonds")
HANDS = ("deck", "player", "computer")

DECK = 0
PLAYER = 1
COMPUTER = 2

def main():
    cardDB = initCards()

    for i in range(5):
        assignCard(cardDB, PLAYER)
        assignCard(cardDB, COMPUTER)

    showDB(cardDB)
    print()
    showHand(cardDB, PLAYER)
    showHand(cardDB, COMPUTER)
def initCards():
    cardDB = []
    for i in range(NUMCARDS):
        cardDB.append(0)
    return cardDB

def showDB(cardDB):
    for cardNum, location in enumerate(cardDB):
        print (f"{cardNum:3}: {getCardName(cardNum):25} {HANDS[location]}")
        
        
def getCardName(cardNum):
    suit = cardNum // 13
    rank = cardNum % 13
    cardName = (f"{RANKNAME[rank]} of {SUITNAME[suit]}" )
    return cardName

def assignCard(cardDB, hand):
    cardNum = random.randrange(NUMCARDS)
    if cardDB[cardNum] == 0:
        cardDB[cardNum] = hand
    else
        #make it try again, don't know how though
    
def showHand(cardDB, hand):
    print(f"Cards in {HANDS[hand]} hand")
    for cardNum, location in enumerate(cardDB):
        if location == hand:
            print (f"   {getCardName(cardNum)}")
    
    
    
    
main()
    