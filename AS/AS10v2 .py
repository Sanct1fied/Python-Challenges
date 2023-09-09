my_names = []
nice_list = []
naughtly_list = []
numberofnice = 0
numberofnaughty = 0

with open("names.txt","r") as whole_file:
    for i in whole_file:
        i = i.rstrip("\n")
        my_names.append(i)

length = len(my_names)

for k in range(length):
    checking = [char for char in my_names[k]]
    vowelcount = 0
    double = 0
    naughty = 0
    for i in checking:
        if i in ["a", "e", "i", "o", "u"]:
            vowelcount = vowelcount + 1

    for l in range(len(checking) - 1):
        if checking[l] == checking[l + 1]:
            double = double + 1
        elif checking[l] in ["a"] and checking[l + 1] in ["b"]:
            naughty = naughty + 1
        elif checking[l] in ["c"] and checking[l + 1] in ["d"]:
            naughty = naughty + 1
        elif checking[l] in ["p"] and checking[l + 1] in ["q"]:
            naughty = naughty + 1
        elif checking[l] in ["x"] and checking[l + 1] in ["y"]:
            naughty = naughty + 1

    if vowelcount>2 and double>0 and naughty<1:
        nice_list.append(my_names[k])
        numberofnice += 1
    else:
        naughtly_list.append(my_names[k])
        numberofnaughty += 1


print(nice_list)
print(naughtly_list)
print(numberofnice)
print(numberofnaughty)
