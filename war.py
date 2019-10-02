from cards import *
from playsound import playsound

def game():
    count = 0
    gameDeck = Deck()
    p1_name = input("Player 1, what's your name? ")
    p2_name = input("Player 2, what's your name? ")
    p1 = Player(p1_name)
    p2 = Player(p2_name)
    deal(p1,p2,gameDeck)
    # while(len(p1.deck) != 0) & (len(p2.deck) != 0) :
    for x in range(30):
        new_battle = input("\nHit Enter For Battle")
        playsound('clang.wav')
        print(f"Battle Winner: {turn(p1,p2)}")
        count += 1
    print(f"\n{p1.name} has {len(p1.deck)} cards")
    print(f"\n{p2.name} has {len(p2.deck)} cards")
    if len(p1.deck)>len(p2.deck) :
        print(f"\nCongrats {p1.name}, you've won the war")
    else:
        print(f"\nCongrats {p2.name}, you've won the war")


def deal(p1,p2,gameDeck):
    for x in range(26):
        p1.deck.append(gameDeck.deck[x])
        p2.deck.append(gameDeck.deck[x+26])

def turn(p1,p2):
    print(f"\n{p1.name}'s card is the {p1.deck[len(p1.deck)-1].getCard()}\n")
    print(f"{p2.name}'s card is the {p2.deck[len(p2.deck)-1].getCard()}\n")
    if (p1.deck[len(p1.deck)-1].value>p2.deck[len(p2.deck)-1].value):
        Winner(p1,p2,1, False)
        return p1.name
    elif (p2.deck[len(p2.deck)-1].value>p1.deck[len(p1.deck)-1].value) :
        Winner(p2,p1,1, False)
        return p2.name
    else :
        return megaBattle(p1,p2)
    

def add_to_bottom(p,card):
    p.deck.append(0)
    for x in range(len(p.deck)-1,0,-1):
        p.deck[x] = p.deck[x-1]
    p.deck[0] = card

def megaBattle(p1,p2):
    p1_card = p1.deck[len(p1.deck)-1].value
    p2_card = p2.deck[len(p2.deck)-1].value
    depth = 1
    while (p1_card == p2_card) :
        depth += 4
        p1_card = p1.deck[len(p1.deck)-depth].value
        p2_card = p2.deck[len(p2.deck)-depth].value
    if (p1_card > p2_card):
        print(p1.name+" has won "+str(depth)+" cards in MegaBattle")
        print("Commandeered Cards:")
        Winner(p1,p2,depth, True) 
        return p1.name
    else :
        print(p2.name+" has won "+str(depth)+" cards in MegaBattle")
        print("Commandeered Cards:")
        Winner(p2,p1,depth, True)
        return p2.name

def Winner(winner, loser, depth, mega):
    for x in range(depth):
        card = loser.deck.pop()
        if mega:
            print(f"\t \t \t{card.getCard()}")
        add_to_bottom(winner, card)
        add_to_bottom(winner, winner.deck.pop())


game()