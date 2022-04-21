import random
Affirmative= ["it is certain","without a doubt","Yes, definitely","Most likely.","outook good","yes."]
non_commital = ["cannot predict now","Reply hazy, try again","ask again later","better not tell you now","concentrate and ask again"]
negative = ["my reply is no","don't count on it","my sources say no","outlook not so good","very doubtful"]

while True:
    Shake = input("what is your question?")
    possible_answers = random.choice([Affirmative,non_commital,negative])
    print(possible_answers)
    answer = random.randint(0,5)

    print(''.join(possible_answers[answer]))
    play_again = input("do you wish to ask the magic 8 ball another question?")
    if play_again in ["no"]:
        break
