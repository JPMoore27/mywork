import matplotlib.pyplot as plt

#both arrays have 0 repeated 26 times, once for each letter in the alphabet

letterCounts = []
for i in range(26):
    letterCounts.append(0)

letterCountsNoR = []
for i in range(26):
    letterCountsNoR.append(0)

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


with open("5letterwords.txt") as words:
    for word in words:
        word = word.strip()
        for letter in word:
            letterCounts[letters.index(letter)] += 1 #counting how often each letter occurs
        for i in range(len(letters)):
            if letters[i] in word:
                letterCountsNoR[i] += 1 #counting in how many words that word occurs in




plt.hist(letterCounts, bins = 8)
plt.title("Frequencies of Letters")
plt.xlabel("Occurences")
plt.ylabel("Number of Letters")
plt.show()

#sorting the letters by occurences
sortedLetters = []
for i in range(26):
    sortedLetters.append(None)
sortedCounts = sorted(letterCounts)
for i in range(26):
    sortedLetters[i] = letters[letterCounts.index(sortedCounts[i])]
    
    
plt.bar(sortedLetters, sortedCounts)
plt.title("Letter vs. Number of Occurences in 5 Letter Words")
plt.xlabel("Letter")
plt.ylabel("Occurences")
plt.show()    

sortedLettersNoR = []
for i in range(26):
    sortedLettersNoR.append(None)
sortedCountsNoR = sorted(letterCountsNoR)
for i in range(26):
    sortedLettersNoR[i] = letters[letterCountsNoR.index(sortedCountsNoR[i])]

plt.bar(sortedLettersNoR, sortedCountsNoR)
plt.title("Letter vs. Number of 5 Letter Words it Occurs In")
plt.xlabel("Letter")
plt.ylabel("Words")
plt.show()




diffs = [] #the difference between the two counting letters based on the word
for i in range(26):
    diffs.append((letterCounts[i] - letterCountsNoR[i]) / letterCounts[i])
    

#This graph shows which letters are the biggest "winners" and "losers" in the different counting systems
plt.bar(letters, diffs)
plt.title("Letter vs Occurences - Words it Occurs In")
plt.xlabel("Letter")
plt.ylabel("Occurences - Words")
plt.show()


plt.scatter(range(1, 27), letterCounts)
plt.title("Position in Alphabet vs Frequency in 5 Letter Words")
plt.xlabel("Position in Alphabet")
plt.ylabel("Frequency in 5 Letter Words")
plt.show()



