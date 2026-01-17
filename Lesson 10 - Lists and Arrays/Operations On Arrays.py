my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(my_set)

my_set = {1.0, 1.1, 1.2, 1.3, 1.4, 1.5, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}
print(my_set)

my_set = {1, 2, 3, 4, 3, 2, 1}
print(my_set)

my_set = set([1, 2, 3, 2, 1])
print(my_set, "\n")

num_set = ([0, 1, 3, 4, 5])
print("Original set:")
print(num_set)
num_set.pop()
print("After removing the first element of said set:")
print(num_set, "\n")