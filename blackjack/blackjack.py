import random
import time
# diamonds, hearts, spades, clubs = 0, 1, 2, 3

class card: # an object with a rank value and suit value, stored as strings

    value = 0
    name = "placeholder"

    def __init__(self, rank, suit):
        self.value = rank
        if rank > 10:
            self.value = 10

        #rank and suit switcher library thing
        ranks = {
            1:'A',
            2:'2',
            3:'3',
            4:'4',
            5:'5',
            6:'6',
            7:'7',
            8:'8',
            9:'9',
            10:'10',
            11:'J',
            12:'Q',
            13:'K'
        }
        suits = {
            0:'♦',
            1:'♥',
            2:'♠',
            3:'♣'
        }
        self.name = ranks.get(rank, 'error') + suits.get(suit, 'error')
#to do, multiple decks
class deck:
    cards = []
    shuffled = False

    def __init__(self, shuffle): #makes the deck. if shuffle is true, it will shuffle the deck
        for i in range(0, 4):
            for j in range(1, 14):
                self.cards.append(card(j, i))
        if(shuffle):
            random.shuffle(self.cards)
            self.shuffled = True

    def drawCard(self): #removes the "top" card from the deck, and returns it
        temp = self.cards.pop(len(self.cards)-1)
        if len(self.cards) == 0: #if the deck is exhausted, make a new one.
            print('shuffling the deck...')
            time.sleep(1)
            for i in range(0, 4):
                for j in range(1, 14):
                    self.cards.append(card(j, i))
            if(self.shuffled):
                random.shuffle(self.cards)
        return temp

    def length(self):
        return len(self.cards)

    def remove(self, name): #removes the card with name c
        for card in self.cards:
            if card.name == name:
                self.cards.remove(card)
                break

    def __str__(self): # returns all the cards seperated by commas
        output = ""
        for card in self.cards:
            output += "{}, ".format(card.name)
        return output

#blackjacks give -1
def total(cards): #adds up the sum of a hand
    aces = 0
    total = 0

    for a in cards:
        if a.value == 1:
            aces += 1
        else:
            total += a.value
    #if there are two cards and they add to 21 it's a blackjack
    if aces == 1 and total == 10 and len(cards) == 2:
        return -1
    #add 1 for each ace, then add 10 until there are no more aces or the total hits 12
    total += aces
    for i in range(0, aces):
        if total < 12:
            total += 10
    return total

def printScreen(dealerHand, playerHand, playerTurn): ##returns a string for what the screen should show

    pTotal = str(total(playerHand))
    if pTotal == '-1':
        pTotal = 'Blackjack!'

    outputString = '\n' * 100 + "                    Blackjack by JP\nDealer:"
    if(playerTurn):
        outputString +=  '▮▮' + dealerHand[1].name + "\n Total: ?" + "\n\nYou:"
    else:
        for card in dealerHand:
            outputString += card.name
        outputString += "\n Total: " + str(total(dealerHand)) + "\n\nYou:"
    for card in playerHand:
        outputString += card.name
    outputString += "\n Total: " + pTotal
    if(playerTurn):
        outputString += "\n Hit or Stay?"
    return outputString

def playerWon(dealerHand, playerHand): #find out who won
    if total(playerHand) > 21:
        return False
    elif total(dealerHand) > 21:
        return True
    elif total(dealerHand) == -1 and total(playerHand) != -1:
        return False
    else:
        return  total(playerHand) == -1 or total(playerHand) > total(dealerHand)

if __name__ == "__main__":
    deck = deck(True)
    while(True):
        dealerHand = [] #both players hands are lists of the card object
        for i in range(0, 2):
            dealerHand.append(deck.drawCard())
        playerHand = []
        for i in range(0, 2):
            playerHand.append(deck.drawCard())

        playerTurn = True; ## when false, it's now the dealer's turn

        while(playerTurn):
            #takes and processes the player's input
            move = input(printScreen(dealerHand, playerHand, playerTurn))
            if move.lower() == 'hit':
                playerHand.append(deck.drawCard())
            if move.lower() == 'stay':
                playerTurn = False
            if total(playerHand) > 21:
                print(printScreen(dealerHand, playerHand, playerTurn))
                print('busted!')
                playerTurn = False

        if total(playerHand) > 21: #don't have dealer play if the player bustedd
            playerTurn = True

        while(not playerTurn):
            time.sleep(2)
            print(printScreen(dealerHand, playerHand, playerTurn))
            #hit if below 17, stand if 17 or more
            if total(dealerHand) < 17:
                dealerHand.append(deck.drawCard())
            else:
                playerTurn = True
            if total(dealerHand) > 21:

                print('busted!')
                playerTurn = True
        time.sleep(2)
        if playerWon(dealerHand, playerHand):
            print('you won!')
            time.sleep(2)
        else:
            print('you lost')
            time.sleep(2)
