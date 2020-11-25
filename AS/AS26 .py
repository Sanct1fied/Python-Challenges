with open("silly code.txt","r") as whole_file:
   for line in whole_file:
        res = len("silly code.txt".split())
        chars = len(line)
        av = chars/res

print(av)
if av<10:
    print("this passage is easy to read")
elif av>10:
    print("this passage is hard to read")
