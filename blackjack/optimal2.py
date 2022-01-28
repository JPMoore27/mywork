import random
from copy import deepcopy

class card: #stores the value of the card. We don't care about the suit

    value = -1

    def __init__(self, value): # accepts 10 or the capital letter for face cards. accepts 1 or A for ace
        try:
            self.value = int(value)
        except ValueError:
            letter2Value = {"J" : 10, "Q" : 10, "K" : 10, "A" : 1}
            self.value = letter2Value[value]

    def __str__(self):
        return str(self.value)

class deck: #contains a list of cards

    cards = []

    def __init__(self, num=1, cards=[]): #num = number of decks, cards = a unique list of cards
        self.cards = deepcopy(cards)
        if not self.cards:
            for i in range(1, 11): #this loop makes aces-10s
                for j in range(4 * num):
                    self.cards.append(card(i))
            for i in range(4*3*num): #this loop makes jacks-kings
                self.cards.append(card(10))

    def __str__(self): #returns a string of values with spaces in between
        output = ""
        for card in self.cards:
            output += str(card) + " "
        return output

    def shuffle(self): #shuffles the deck
        random.shuffle(self.cards)

    def remove(self, seenCard): #takes in a card, removes the first equivalent card in the deck
        for card in self.cards:
            if card.value == seenCard.value:
                self.cards.remove(card)
                return

    def drawCard(self): #removes the top card from the deck and returns it
        return self.cards.pop(len(self.cards)-1)

    def simDealer(self, playerTotal, dealerTotal): # takes in player's total and the dealer's revealed card, returns the odds of victory
        numWin = 0
        numLose = 0
        for i in range(len(cards)):
            dealerTotal += cards[i].value #"draw" a card to be the dealer's second
            if dealerTotal > 21: #over 21, busted, player wins
                numWin += 1
            elif dealerTotal + cards[i].value >= 17: #17 or over, stands, player wins if the dealer is lower than the player
                numWin += int(dealerTotal < playerTotal)
                numLose += int(dealerTotal >= playerTotal)
            else: #below 17, hit till it's not
                #to get every possibility, iterate through every card in the deck
                for j in range(len(cards)):
                    if j == i:
                        continue #skip the case where the index is the same as the dealer's second card
                    tempDTotal = dealerTotal + cards[j].value
                    usedIndices = [i, j]
                    while TempDTotal < 17:
                        for i in range 






class hand:

    cards = []

    def __str__(self): #returns a string of values with spaces in between
        output = ""
        for card in self.cards:
            output += str(card) + " "
        return output

    def calcTotal(self):
        total = 0
        numAs = 0
        for card in self.cards: #adds up all non ace values
            if card.value == 1:
                numAs += 1
            else:
                total += card.value
        #handle aces, which give 1 or 11
        total += numAs
        for i in range(numAs):
            if total + 10 <= 21:
                total += 10
        return total

    def addCard(self, card):
        self.cards.append(card)





if __name__ == "__main__":
    d = deck()
    d2 = deck(1, deck.cards)
    d.shuffle()
    d2.shuffle()
    print(d2)
    print(d)
