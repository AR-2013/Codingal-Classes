import random
playing = True
number = str(random.randint(10, 20))

print("I will generate a number from 10 to 20 and you have to try and guess it.")
print("The game ends if you get it right")

while playing:
    guess = int(input("Give me your best guess: \n"))
    if number == guess:
        print("You win the game!")
        print("The number was", number)
        break
    else:
        print("That's not right, try again.") 