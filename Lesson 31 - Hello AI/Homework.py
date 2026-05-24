print("Hello! I am AI bot!")

name = input("What is your name: ")

print("Nice to meet you", name)

print("How are you feeling today? (good/bad): ")
mood = input().lower()

if mood=="good":
    print("I am glad to hear that!")
    print("What would you like help with today?")
    help = input().lower()
    if help == "nothing":
        print("Ok. Let me know if you need anything.")
    else:
        print("Of course I can help! Just send over what you need help with.")
elif mood=="bad":
    print("Oh no! I am sorry to hear that. Would you like to talk about it? (yes/no)")
    answer = input().lower()
    if answer=="no":
        print("Ok. Let me know if you need anything else.")
    elif answer=="yes":
        print("Ok, go ahead.")
        talkaboutit = input().lower()
        print("I understand what you're going through. Would you like to talk some more about it? (yes/no)")
        yesorno = input().lower()
        if yesorno=="yes":
            print("Go ahead.")
            talkaboutit2 = input().lower()
        elif yesorno=="no":
            print("Ok. I understand.")
        else:
            print("I didn't understand your answer. PLease input yes or no.")
            yesorno2 = input().lower()
            if yesorno2=="yes":
                print("Go ahead.")
                talkaboutit3 = input().lower()
            elif yesorno2=="no":
                print("Ok. Let me know if you need anything.")
    else:    
        print("Sorry I didn't understand please try inputting your response again in a yes or no format.")
        answer2 = input().lower()
else:
    print("Its ok. I understand. Sometimes it's hard to put feelings into words.")

print("Nice chatting with you", name)