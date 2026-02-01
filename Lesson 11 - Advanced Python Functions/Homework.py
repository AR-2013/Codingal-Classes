num = int(input("Enter a number: "))

odd_numbers = []
even_numbers = []

for i in range(1, num):
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)

fruits = ["apple", "banana", "mango", "orange"]

updated_fruits = []

for fruit in fruits:
    updated_fruits.append(fruit.capitalize())

print("Original fruits list:", fruits)
print("Updated fruits list:", updated_fruits)


