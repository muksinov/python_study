# подсчитать число парных и непарных чисел в массиве
List=[1,5,36,32,6,3,143,64234,64,21,12,34,45,4444]
#print(len(List))

# even = 0
# for number in List :
#     if number % 2 == 0:
#         even = even+1
#
# print(f'Парних чисел {even}')
# print(f'Не парних чисел {len (List)-even}')


#создать новый мисив в который поместить числа которые меньше 70 из первого масивать а те которые больше или равные 70 поделить на 2 и тоже поместить в новый массив
# number_4 = []

# for number in List:
#     if number  < 70:
#         number_4.append(number)
#     if number >= 70:
#         number_4.append(number/2)
# print(number_4)

#отсортировать старый массив по порядку возростания


List.sort()
print(List)





