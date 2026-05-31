import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches" : ["Bali", "Maldives"],
    "mountains" : ["Swiss Alps", "Himalyas"],
    "cities" : ["Paris", "New York"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!"
    "Why did the computer go to the doctor? Because it had a virus!"
    "Why do you never give Elsa a balloon? Because she'll let it go!"
    "What's an elephant and an ant's favourite sport to play? Squash!"
]

def normalize_input(text):
    return re.sub(r"\s+", "", text.strip().lower())
def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: Let's try another.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: I'll suggest again.")
            recommend()
    else:
        print(Fore.RED + f"Sorry, I don't have that kind of destination.")
def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"Packing tips for {days} days in {location}":)
    print(Fore.GREEN + "- Pack versatile clothes")
    print(Fore.GREEN + "- Pack chargers or adapters")
    print(Fore.GREEN + "- Chack the weather forecast")