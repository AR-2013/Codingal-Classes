def add(P, Q):
    return P + Q
def subtract(P, Q):
    return P - Q
def multiply(P, Q):
    return P * Q
def divide(P, Q):
    return P / Q

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
print("Which of the following functions would you like to do?")
print("a - add")
print("b - subtract")
print("c - multiply")
print("d - divide")
choice = input("Enter which one-a,b,c or d: ")

if choice=="a":
    print(add(num1, num2))
elif choice=="b":
    print(subtract(num1, num2))
elif choice=="c":
    print(multiply(num1, num2))
elif choice=="d":
    print(divide(num1, num2))
else:
    print("Not a valid choice")