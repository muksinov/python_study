# number_list =[6,43,-2,11,-55,-12,3,345]
# new_list=[number **3 /2 for number in number_list if number > 0]
# print(new_list)
# new_list_1 = ['+' if number > 0 else '-' if number < 0
#              else 'zero' for number in number_list]
# print(new_list_1)






# numbers_dict = {'first':1, 'second':2, 'third':3}
# new_dict ={key: value ** 3 for key, value in numbers_dict.items()}
# print(new_dict)
# number_list=[6, 43, 0, -2,11, -55, -12, 3, 345]
# numbers_dict = {number: number ** 2 for number in number_list}
# print(numbers_dict)
# numbers_dict = {number: 'positive' if number > 0
# else 'negative' if number < 0 else 'zero' for number in number_list}
# print(numbers_dict)


number_list=[6, 43, 0, -2,11, -55, -12, 3, 345]
numbers_set = { number ** 2 for number in number_list}
print(numbers_set)
numbers_set = { number ** 2 for number in range (3, 11)}
print(numbers_set)
number_list=[6, 43, 0, -2,11, -55, -12, 3, 345]
letter_set = {letter.upper()for letter in 'hello' }
print(letter_set)






























































































