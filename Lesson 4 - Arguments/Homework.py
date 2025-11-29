condition1 = input("Is the programme you want to shut down not saved? Answer yes or no: ")
if condition1 == 'yes' or 'Yes':
    condition2 = input("Do you know your username or password for next time you want to login: ")
    if condition2 == 'yes' or 'Yes':
        print("You can shut down")
    elif condition2 == 'no' or 'No':
       print("You can't shut down")
    else:
        print("Sorry")
elif condition1 == 'no' or 'No':
    print("You can't shut down")
else:
    print("Sorry")
    
