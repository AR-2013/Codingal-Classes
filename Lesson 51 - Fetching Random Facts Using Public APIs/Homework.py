
import requests

url = "https://www.drivebird.com/api/tech-facts/random"

def get_random_technology_fact():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(f"Did you know? {fact_data['data'][0]['fact']}")
    else:
        print("Failed to fetch fact")

while True:
    user_input = input("Press enter to get a random technology fact or press q to quit: ")
    if user_input.lower() == 'q':
        break
    get_random_technology_fact()
