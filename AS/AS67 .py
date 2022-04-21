import random
import time

all_cards = ['michel jordan','Ifrostbolt','Sanctified mind','Shaxx','Mesi','Rnldo','Vd','Apple','James Lebron (CHINA)','kit tzen kim','fatty','nando']
available_cards = ['michel jordan','Ifrostbolt','Sanctified mind','Shaxx','Mesi','Rnldo','Vd','Apple','James Lebron (CHINA)','kit tzen kim','fatty','nando']
scoring_values = [99,1,50,69,10,7,26,9,100,24,1,79]


name1 = input("what is player 1's name?:")
player1_cards = []
for i in range(5):
    card = random.choice(available_cards)
    player1_cards.append(card)
    available_cards.remove(card)

print(available_cards)



name2 = input("what is player 2's name?:")
player2_cards = []
for i in range(5):
    card = random.choice(available_cards)
    player2_cards.append(card)
    available_cards.remove(card)

print(name1 , ", your cards are:", player1_cards)
time.sleep(5)
for i in range(10):
    print('\n')
print(name2 , ", your cards are :" , player2_cards)
for i in range(10):
    print('\n')

card1 = int(input('player 1, pick a card (1-5)'))
ind = all_cards.index(player1_cards[card1-1])
player1_atk = scoring_values[ind]
print(player1_atk)

for i in range(10):
    print("\n")

card2 = int(input('player 2, pick a card (1-5)'))
ind = all_cards.index(player2_cards[card2-1])
player2_atk = scoring_values[ind]
print(player2_atk)

if player2_atk >= player1_atk:
    print("player 2 wins the round!")
    player2_points =+ 1
else:
    print("player 1 wins the round!")
    player1_points =+ 1
