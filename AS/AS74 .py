A = int(input("what is the first input? (1 or 0):"))
B = int(input("what is the second input? (1 or 0):"))
X = 0

def nandgate():
    if A == 0 and B == 0:
        X = 1
    if A == 1 and B == 0:
        X = 1
    if A == 0 and B == 1:
        X = 1
    if A == 1 and B == 1:
        X = 0

    return X

def andgate():
    x1 = nandgate()
    x2 = nandgate()
    print(x1,x2)

andgate()
