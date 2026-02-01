import random

choices = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

password = ""
length = 8

for i in range(length):
    password = password + random.choice(choices)

print("Your password is:", password)
