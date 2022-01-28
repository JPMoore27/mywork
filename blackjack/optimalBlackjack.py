from blackjack import card, deck, total, playerWon

'''
general plan:
go through every possible scenario. find out if hitting would increase or decrease the odds of winning
measure that change with what Im calling "change in odds" which equals:
(the number of scenarios in which the player's total will go past the dealers simulated total) - (the number of scenarios the player would bust)
if the change in odds is positive, hit, if not, stand (I'm not accounting for the other options right now)
To find these scenarios, I will iterate through every value that could be in the dealers hand, then every value the player can draw, weighting both for how often that value occurs
then, Ill simulate every possible dealer hand that can be played. Ill try to avoid repeats, but that may be more trouble than its worth of it runs fast enough already
'''


#these functions help with turning inputs into what the card and deck classes like
def fixCard(cardString): #turns the card inputted into the format with the symbols
    suitKey = {
        "D":'♦',
        "H":'♥',
        "S":'♠',
        "C":'♣'
    }
    try:
        return cardString[0] + suitKey[cardString[1]]
    except KeyError:
        print("Error: invalid format. Make sure to use two characters, the second being D, H, S, or C")

def makeCardTpl(cardString): # returns a tuple to go into the card class __init__ function
    valueKey = {
        "A":1,
        "J":11,
        "Q":12,
        "K":13
    }
    try:
        value = int(cardString[0]) #will still work with a 1 instead of an A for an ace
    except ValueError:
        if cardString[0] in valueKey:
            value = valueKey[cardString[0]]
        else:
            print("Invalid value. Make sure the value is a number from 2-9, or an A, J, Q, or K")
            return
    suitToInt = {
        "D":0,
        "H":1,
        "S":2,
        "C":3
    }
    return value,



if __name__ == "__main__":
    deckSim = deck(False)
    dealerHand = []
    dealersCard = True
    while True:
        seenCard = input("Welcome to JP's blackjack cheating software. Please enter in the cards you've seen one by one, then \"done,\"\nor type \"help\" for help, or \"stop\" to stop\n")
        if seenCard.lower() == "stop":
            break
        if seenCard.lower() == "help":
            print("enter the cards using the value then suit, so\nQueen of Hearts: QH\nSeven of Clubs: 7C\nif you mess it up, the computer will do nothing without telling you. Sorry bout that.")
            continue
        if seenCard.lower() == "done":
            print(deckSim)
        else:
            deckSim.remove(seenCard)
            dealerHand.append(seenCard)
