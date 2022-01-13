import random

all_cards = ["michel jordan","Ifrostbolt","Sanctified mind","Shaxx","Mesi","Rnldo","Vd","Apple"]
available_cards = ["michel jordan","Ifrostbolt","Sanctified mind","Shaxx","Mesi","Rnldo","Vd","Apple"]
scoring_values = [99,1,50,69,10,7,26,9]


name1 = input("what is player 1's name?:")
player1_cards = []
for i in range(5):
    player1_cards.append(random.choice(all_cards))

for i in range(len(all_cards)):
    if all_cards[i] in player1_cards:
        available_cards.remove(available_cards[i])  #error here
print(available_cards)



name2 = input("what is player 2's name?:")
player2_cards = []
for i in range(5):
    player2_cards.append(random.choice(available_cards))


print(player1_cards,player2_cards)
