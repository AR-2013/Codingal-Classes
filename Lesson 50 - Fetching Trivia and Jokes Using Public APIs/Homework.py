import requests
import random
import html

url = "https://www.codingal.com/student/dashboard/projects/12764815/"
response = requests.get(url)
data = response.json()

if data["response_code"] == 0:
    score = 0

    print("================================")
    print("        TRIVIA QUIZ")
    print("================================")

    for number, question in enumerate(data["results"], 1):
        question_text = html.unescape(question["question"])
        correct_answer = html.unescape(question["correct_answer"])
        incorrect_answers = [
            html.unescape(answer)
            for answer in question["incorrect_answers"]
        ]

        answers = incorrect_answers + [correct_answer]
        random.shuffle(answers)

        print(f"\nQuestion {number}:")
        print(question_text)

        for i, answer in enumerate(answers, 1):
            print(f"{i}. {answer}")

        while True:
            try:
                choice = int(input("Enter your answer (1-4): "))

                if choice in range(1, 5):
                    break

                print("Please enter a number from 1 to 4.")
            except ValueError:
                print("Please enter a number.")

        if answers[choice - 1] == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {correct_answer}")

    print("\n================================")
    print("           QUIZ OVER")
    print("================================")
    print(f"Your score: {score}/5")

    if score == 5:
        print("Perfect score!")
    elif score >= 3:
        print("Great job!")
    else:
        print("Good effort! Try again!")

else:
    print("Sorry, there was a problem getting the questions.")