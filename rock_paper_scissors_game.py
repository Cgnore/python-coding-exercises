import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_list = [rock, paper, scissors]
computer_choice = random.randint(0,2)
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors: "))
print("Your choice:\n" + game_list[user_choice])
if user_choice == 0:
    print("Computer choice:\n" + game_list[computer_choice])
    if computer_choice == 0:
        print("That's a draw!")
    elif computer_choice == 1:
        print("You lost...")
    else:
        print("You won!")
elif user_choice == 1:
    print("Computer choice:\n" + game_list[computer_choice])
    if computer_choice == 0:
        print("You won!")
    elif computer_choice == 1:
        print("That's a draw!")
    else:
        print("You lost...")
elif user_choice == 2:
    print("Computer choice:\n" + game_list[computer_choice])
    if computer_choice == 0:
        print("You lost...")
    elif computer_choice == 1:
        print("You won!")
    else:
        print("That's a draw!")
else:
    print("There must be a typo... Game is Over...")