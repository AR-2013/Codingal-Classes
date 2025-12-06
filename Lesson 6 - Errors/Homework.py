try:
    age = int(input("What is your age in numbers: "))
except ValueError:
    print("Please put your age in numbers")
else:
    if age%2==0:
        print("Your age is even")
    else:
        print("Your age is odd")