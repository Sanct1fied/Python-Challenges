import random
phrase = ["pizza", "running","gaming","singing", "food", "hotdog"]

num = random.randint(100,999)
f = open("silly code.txt", "w")
f.write(str(num) + random.choice(phrase))

f.close()
