import random

with open("A216.txt","r") as whole_file:
    wordlist = []
    word = input("what is your word?")
    length = len(word)
    characters = [char for char in word]
    new_word = []


    for i in range(length*26):
        for i in range(length):
            new_char = random.choice(characters)
            characters.remove(new_char)
            new_word.append(new_char)
            if new_word == characters:
                length=1
                pass
            else:
                anagram = new_word
                
        if anagram in 
