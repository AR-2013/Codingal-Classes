numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]

result = map(lambda x, y: x + y, numbers1, numbers2)
print("Addition of two lists: ")
print(list(result))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sq(num):
    return num*num
square = list(map(sq, nums))
print("Squares of numbers in a list: ")
print(square)