word = str(input("what is the word you want translated?:"))

length = len(word)
characters = [char for char in word]
final = []
for i in characters:
    if i not in ["a","e","i","o","u"]:
        newword = i+"o"+i
        final.append(newword)
    else:
        final.append(i)

print(*final,sep="")
