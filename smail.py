for number in range(1,11):
    print('\U0001f600' * number)

nested_list = [[1,2,3], [4,5,6,True], [7,8,9,'text'],
               [10,11,1213], [False,23,'hello']]
               
# for inner_list in nested_list:
#     print( nested_list)

# for inner_list in nested_list:
#     for number in inner_list:
#         print(number)



[[print(number) for number in inner_list] for inner_list in nested_list]









































