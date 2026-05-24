print("Hello! I am AI bot!")

name = input("What is your name: ")

print("Nice to meet you", name)

print("How are you feeling today? (good/bad): ")
mood = input().lower()

if mood=="good":
    print("I am glad to hear that!")
elif mood=="bad":
    print("Oh no! I am sorry to hear that. Hope things get better soon.")
else:
    print("Its ok. I understand. Sometimes it's hard to put feelings into words.")

print("Nice chatting with you", name)