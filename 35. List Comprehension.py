import numbers


#greeting= 'hello!'
#letter_list=[]
#for letter in greeting:
   # letter_list.append(letter)
#print(letter_list)




# letter_list = [letter for letter in greeting]
# print(letter_list)
# number_list=[number for number in '0123456789']
# print(number_list)
# number_list_1=[num for num in range(0,10)]
# print(number_list_1)
# number_list_2=[num **2 for num in range(0,10)]
# print(number_list_2)
# number_list_3=[-((num-3)/2) **2 for num in range(0,10)]
# print(number_list_3)

number_list = [5, 43, -2, 11, -55, -12, 3, 345]
new_list= [number **3 / 2 for number in number_list if number > 0]
print(new_list)




















































































