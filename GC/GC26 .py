phrase = ("how much wood would a wood chuck chuck if a wood chuck could chuck wood")
print(phrase)
type1 = str(input("please type the phrase above:"))
type2 = str(input("please type the phrase above again:"))


if type1 and type2 == phrase:
    print("you passed!")
elif type1 == phrase and type2 != phrase:
    print("you only got 1 right: fail")
elif type2 == phrase and type1 != phrase:
    print("you only got 1 right: fail")
else:
    print("you got both wrong: GO HOME YOU FAILURE")
