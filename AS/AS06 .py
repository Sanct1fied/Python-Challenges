vowel = ["a","e","i","o","u","A","E","I","O","U"]
word = str(input("what is your word?:"))
integer = 0
word2 = [char for char in word]
num = len(word2)
for i in range(num):
    if word2[i] in vowel:
        integer = integer+1

print(integer)
