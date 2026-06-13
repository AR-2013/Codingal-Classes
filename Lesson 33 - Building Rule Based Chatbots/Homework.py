import re
import random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Hawaii", "Phuket"],
    "mountains": ["Swiss Alps", "Himalayas", "Rocky Mountains", "Mount Fuji"],
    "cities": ["Paris", "New York", "Tokyo", "Dubai"],
    "forests": ["Amazon Rainforest", "Black Forest", "Daintree Rainforest"],
    "islands": ["Bora Bora", "Fiji", "Seychelles"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do you never give Elsa a balloon? Because she'll let it go!",
    "What's an elephant and an ant's favourite sport to play? Squash!"
]

fun_facts = {
    "bali": "Bali is known as the Island of the Gods.",
    "maldives": "The Maldives has over 1,000 coral islands.",
    "paris": "Paris is often called the City of Light.",
    "tokyo": "Tokyo is one of the world's largest cities.",
    "dubai": "Dubai is home to the Burj Khalifa, the tallest building in the world."
}

def normalize_input(text):
    return re.sub(r"\s+", "", text.strip().lower())

def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, cities, forests, or islands?")
    preference = normalize_input(input(Fore.YELLOW + "You: "))

    if preference in destinations:
        suggestion = random.choice(destinations[preference])

        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")

        if suggestion.lower() in fun_facts:
            print(Fore.CYAN + f"Fun Fact: {fun_facts[suggestion.lower()]}")

        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = normalize_input(input(Fore.YELLOW + "You: "))

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: Let's try another destination next time.")
        else:
            print(Fore.RED + "TravelBot: I didn't understand that.")
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have that category.")

def packing_tips():
    print(Fore.CYAN + "TravelBot: Where are you going?")
    location = input(Fore.YELLOW + "You: ")

    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"\nPacking tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes")
    print(Fore.GREEN + "- Bring chargers and adapters")
    print(Fore.GREEN + "- Check the weather forecast")
    print(Fore.GREEN + "- Carry important documents")
    print(Fore.GREEN + "- Pack any necessary medication")

def tell_joke():
    print(Fore.GREEN + random.choice(jokes))

def travel_quiz():
    print(Fore.CYAN + "Travel Quiz!")
    print(Fore.CYAN + "Which city is known as the City of Light?")
    print(Fore.CYAN + "A. London")
    print(Fore.CYAN + "B. Paris")
    print(Fore.CYAN + "C. Rome")

    answer = normalize_input(input(Fore.YELLOW + "Your answer: "))

    if answer == "b" or answer == "paris":
        print(Fore.GREEN + "Correct!")
    else:
        print(Fore.RED + "Incorrect. The answer is Paris.")

def destination_fact():
    destination = normalize_input(input(Fore.YELLOW + "Enter a destination: "))

    if destination in fun_facts:
        print(Fore.GREEN + fun_facts[destination])
    else:
        print(Fore.RED + "Sorry, I don't have a fact for that destination.")

print(Fore.CYAN + "Welcome to TravelBot!")

while True:
    print(Fore.CYAN + "\n----- MENU -----")
    print(Fore.CYAN + "1. Destination Recommendation")
    print(Fore.CYAN + "2. Packing Tips")
    print(Fore.CYAN + "3. Travel Joke")
    print(Fore.CYAN + "4. Travel Quiz")
    print(Fore.CYAN + "5. Destination Fact")
    print(Fore.CYAN + "6. Exit")

    choice = input(Fore.YELLOW + "Choose an option: ")

    if choice == "1":
        recommend()
    elif choice == "2":
        packing_tips()
    elif choice == "3":
        tell_joke()
    elif choice == "4":
        travel_quiz()
    elif choice == "5":
        destination_fact()
    elif choice == "6":
        print(Fore.GREEN + "TravelBot: Safe travels! Goodbye!")
        break
    else:
        print(Fore.RED + "Invalid choice. Please try again.")