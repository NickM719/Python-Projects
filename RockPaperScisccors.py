import random
import time
playagain = "Yes"
list = ["1", "2", "3"]
while playagain == "Yes":
    botplay = random.choice(list)
    print("Rock,")
    time.sleep(0.5)
    print("Paper,")
    time.sleep(0.5)
    print("Scissors...")
    time.sleep(0.5)
    play = input("1 = Rock, 2 = Paper, 3 = Scissors: ")
    time.sleep(0.5)
    print("Shoot!")
    time.sleep(0.75)
    if botplay == "1":
        print("Rock!")
    if botplay == "2":
        print("Paper!")
    if botplay == "3":
        print("Scissors!")
    time.sleep(0.5)
    if botplay == "1" and play != "2":
        print("I won!")
    if botplay == "1" and play == "2":
        print("You won!")
    if botplay == "2" and play != "3":
        print("I won!")
    if botplay == "2" and play == "3":
        print("You won!")
    if botplay == "3" and play != "1":
        print("I Won!")
    if botplay == "3" and play == "1":
        print("You won!")
    time.sleep(0.75)    
    playagain = input("Wanna play again? ")
else:
    time.sleep(0.75)
    print("Good game!")