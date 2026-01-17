test_dict = {'Codingal' : 3, 'is' : 2, 'best' : 2, 'for' : 2, 'coding' : 1}
print("The original dictionary : " + str(test_dict))

num = 2

res = 0
for key in test_dict:
    if test_dict[key] == num:
        res = res + 1


answer = input("Do you want to check the frequency for the number 2?(Answer Yes or No): ")
if answer == "Yes":
                print("Frequency of 2 is : " + str(res))
else:
   print("Ok, bye!")