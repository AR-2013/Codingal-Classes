def subtract(x, y): 
    return x - y

total_cost = float(input("How much was the bill in digits: "))
amount_paid = float(input("How much did you pay in digits: "))

change = subtract(amount_paid, total_cost)
print("Your change is", change)

