#greeting = 'hello!'
# letter_list =[]
# for letter in greeting:
#     letter_list.append(letter)
# print(letter_list)

# letter_list = [letter for letter in greeting]
# print(letter_list)
# number_list = [letter for letter in '0123456789']
# print(number_list)
# number_list_1 = [letter for letter in range(0, 10)]
# print(number_list_1)
# number_list_2 = [letter **2 for letter in range(0, 10)]
# print(number_list_2)
# number_list_3 = [-((letter -3 ) /2) **2 for letter in range(0, 10)]
# print(number_list_3)

number_list =[6,43,-2,11,-55,-12,3,345]
new_list=[number **3 /2 for number in number_list if number > 0]
print(new_list)
new_list_1 = ['+' if number > 0 else '-' for number in number_list]
print(new_list_1)






