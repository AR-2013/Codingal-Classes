try:
    num1, num2 = eval(input("Enter two numbers sepreated by a comma: "))
    result = num1 / num2
    print("The result is", result)
except ZeroDivisionError:
    print("Division by 0 is an error!")
except SyntaxError:
    print("Put two numbers seperated by a comma like this 1, 2:")
except:
    print("Wrong input")
else:
    print("No excpetions")
finally:
    print("This code will execute no matter what!")