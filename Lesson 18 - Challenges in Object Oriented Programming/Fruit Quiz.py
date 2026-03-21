import random

class FruitQuiz:
    def __init__(self):
        self.fruits = {'apple':'red',
                       'oragne':'orange',
                       'banana':'yellow',
                       'watermelon':'green',
                       'blueberry':'blue',
                       'grape':'purple'}
    def quiz(self):
        while(True):
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the colour of {}?".format(fruit))
            user_answer = input()
            if user_answer.lower() == color:
                print("Correct Answer!")
            else:
                print("Wrong Answer!")