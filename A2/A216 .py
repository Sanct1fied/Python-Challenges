#currently works fine for up to 7 letter words, 8 letters or more are a WIP

import random
my_words = []

with open("A216.txt","r") as whole_file:
    for i in whole_file:
        i = i.rstrip("\n")
        my_words.append(i)



wordlist = []
word = input("what is your word?")
length = len(word)
possible_combinations = []


def acquiringallpossiblecombinations(word):
    allpossiblecombinations = []
    wordy = [char for char in word] #split the word into its letters
    threedigits = [] #placeholder
    onedigit = []    #placeholder
    for p in range(9999990): #bare with me
        wordy = [char for char in word] #temp variable to keep split word intact
        for l in range(len(wordy)):
            onedigit = random.choice(wordy) #picks a random letter
            wordy.remove(onedigit) #removes that letter from the temp variable so it cant be chosen again
            threedigits.append(onedigit) #adds that to a placeholder word

        if ''.join(threedigits) in allpossiblecombinations: #checks if we have already randomly generated that word
            pass #pass if we have
        else:
            threedigits = ''.join(threedigits)  #adds it if we havent
            allpossiblecombinations.append(threedigits)
        threedigits = [] #empty it again so we can use it in the next loop
    return allpossiblecombinations

checking = acquiringallpossiblecombinations(word) #return from the function


for v in range(len(checking)):
    if checking[v] in my_words: #checking if its a real word
        print(checking[v])         #prints it if it is
