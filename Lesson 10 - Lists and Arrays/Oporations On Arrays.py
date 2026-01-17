import array as arr

array_num = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 5, 3, 6, 9, 2, 3,  6, 1, 2, 4, 2])

print("Original array "+str(array_num))

print("Number of occurences of the number 3 in said array: "+str(array_num.count(3)))

array_num.reverse()
print("Reverse the order of the items: ")
print(str(array_num))