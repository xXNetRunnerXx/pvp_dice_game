#Random dice roll battle

import random
import time

print(" player 1 your turn are you ready to roll?")
#print("(y/n)")
time.sleep(1)
roll_descion = input("y/n")
if roll_descion == "y":
    roll = random.randint(1,6)
    print(roll)
elif roll_descion == "n":
    print("leaving game")

print(" player 2 your turn are you ready to roll?")
#print("(y/n)")
time.sleep(1)
roll_descion = input("y/n")
if roll_descion == "y":
    roll_two = random.randint(1,6)
    print(roll)
elif roll_descion == "n":
    print("leaving game")

player1roll = roll
player2roll = roll_two  

print(roll, roll_two)

if roll > roll_two:
    print("player 1 wins")
elif roll < roll_two:
    print("player 2 wins")



