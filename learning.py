import random

rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

player_move = input("      ROCK: 1\n      PAPER: 2\n      SCISSORS: 3\nPlease enter your move: ")
if player_move == "1":
    player_move = rock
elif player_move == "2":
    player_move = paper
elif player_move == "3":
    player_move = scissors

random_integer = random.randint(1, 3)
computer_move = ""
if random_integer == 1:
    computer_move = rock
elif random_integer == 2:
    computer_move = paper
elif random_integer == 3:
    computer_move = scissors

if player_move == computer_move:
    print(f"YOU CHOSE:{player_move}\n\nCOMPUTER CHOSE:{computer_move}\nIT IS A DRAW!")
elif player_move == rock and computer_move == paper:
    print(f"YOU CHOSE:{player_move}\n\nCOMPUTER CHOSE:{computer_move}\nCOMPUTER WINS!")
elif player_move == rock and computer_move == scissors:
    print(f"YOU CHOSE:{player_move}\n\nCOMPUTER CHOSE:{computer_move}\nYOU WIN!")
elif player_move == paper and computer_move == rock:
    print(f"YOU CHOSE:{player_move}\n\nCOMPUTER CHOSE:{computer_move}\nYOU WIN!")
elif player_move == paper and computer_move == scissors:
    print(f"YOU CHOSE:{player_move}\n\nCOMPUTER CHOSE:{computer_move}\nCOMPUTER WINS!")
elif player_move == scissors and computer_move == rock:
    print(f"YOU CHOSE:{player_move}\n\nCOMPUTER CHOSE:{computer_move}\nCOMPUTER WINS!")
elif player_move == scissors and computer_move == paper:
    print(f"YOU CHOSE:{player_move}\n\nCOMPUTER CHOSE:{computer_move}\nYOU WIN!")
else:
    print("You typed an invalid value. YOU LOST!")
