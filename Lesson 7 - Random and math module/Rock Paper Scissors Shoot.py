import random
user_action = input("Rock, paper or scissors? ")
computer_choices = ["rock", "paper", "scissors"]
computer_action = random.choice(computer_choices)

print(computer_action)
if computer_action==user_action:
    print("It's a tie!")
elif computer_action=="rock" and user_action=="paper":
    print("You win!")
elif user_action=="rock" and computer_action=="paper":
    print("You lose!")
elif computer_action=="paper" and user_action=="scissors":
    print("You win!")
elif computer_action=="scissors" and user_action=="paper":
    print("You lose!")
elif computer_action=="rock" and user_action=="scissors":
    print("You lose!")
elif computer_action=="scissors" and user_action=="rock":
    print("You win!")