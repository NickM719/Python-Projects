import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
play = input("Pick a number from 1-10: ")
botplay = random.choice(list)
if int(play) == botplay:
    print("Correct")
else:
    print("Incorrect")