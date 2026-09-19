import requests

url = "https://www.codingal.com/student/dashboard/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("Users:")
    print()

    for user in data:
        print("Name:", user["name"])
        print("Username:", user["username"])
        print("Email:", user["email"])
        print("-" * 30)
else:
    print("Failed to fetch data.")
    print("Status code:", response.status_code)