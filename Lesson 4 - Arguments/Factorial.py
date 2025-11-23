def factorial(x):
    '''This is a recursive string to find the factorial of a number!'''
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
    
print(factorial.__doc__)
print("The factorial of 0 is: ", factorial(0))
print("The factorial of 1 is: ", factorial(1))
print("The factorial of 2 is: ", factorial(2))
print("The factorial of 5 is: ", factorial(5))
print("The factorial of 10 is: ", factorial(10))