def product_of_tuple(numbers):
    product = 1
    for value in numbers:
        product *= value
    return product

my_tuple = (2, 3, 4, 5)

result = product_of_tuple(my_tuple)
print("The product of the tuple is:", result)