import random

rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors "))
game = [rock, paper, scissors]
random_index = random.randint(0,2)

if choice == 0:
    print(f'Your choice:\n {game[0]}')
    print(f'Computer chose:\n {game[random_index]}')
    if random_index == 0:
        print("It's a draw")
    elif random_index == 1:
        print('You lose')
    else:
        print('You win')
elif choice == 1:
    print(f'Your choice:\n {game[1]}')
    print(f'Computer chose:\n {game[random_index]}')
    if random_index == 0:
        print('You win')
    elif random_index == 1:
        print("It's a draw")
    else:
        print('You lose')
elif choice == 2:
    print(f'Your choice:\n {game[2]}')
    print(f'Computer chose:\n {game[random_index]}')
    if random_index == 0:
        print('You Lose')
    elif random_index == 1:
        print('You win')
    else:
        print("It's a draw")
else:
    print("Invalid number. You lose")
