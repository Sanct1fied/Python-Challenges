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


for i in range(length*26):
    characters = [char for char in word]
    anagram = []
    new_word = []
    for i in range(length):
        new_char = random.choice(characters)
        characters.remove(new_char)
        new_word.append(new_char)

        if new_word in possible_combinations:
            length = length + 1
            pass
        elif new_word == characters:
            length= length + 1
            pass
        else:
            anagram = new_word

        for i in range(length):
            anagram =  + anagram[i]
        print(anagram)

        if anagram in my_words:
            print(anagram)


