name = input("what is your child's name?:")
checking = [char for char in name]
vowelcount = 0
double = 0
naughty = 0
for i in checking:
    if i in ["a","e","i","o","u"]:
        vowelcount = vowelcount+1

for l in range(len(checking)-1):
    if checking[l] == checking[l+1]:
        double = double+1
    elif checking[l] in ["a"] and checking[l+1] in ["b"]:
        naughty = naughty+1
    elif checking[l] in ["c"] and checking[l+1] in ["d"]:
        naughty = naughty+1
    elif checking[l] in ["p"] and checking[l+1] in ["q"]:
        naughty = naughty+1
    elif checking[l] in ["x"] and checking[l+1] in ["y"]:
        naughty = naughty+1

if vowelcount>2 and double>0 and naughty<1:
    print("this child is on the nice list")
else:
    print("this child is very naughty")
