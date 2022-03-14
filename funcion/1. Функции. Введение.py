# build-in functions



# x = print ("Hello!")
# y =set
# print(type(x))
# print(type(y))

# print(x)
# print(y)


# built-in methods
# my_list = [1,2,3]
# my_list.append(4)
# print(my_list)
# my_list.clear()
# print(my_list)





# def print_greeting():
#      '''
#      Print 'Hello!' text
#      :return:None
     
#      '''
#      print('Hello!')



    






# print_greeting()

# help(print_greeting)


# def print_greeting_nwith_name(name = 'Nname'):
#     '''
#     :param name
#     :return: None
#     '''

#     print('Hello' + name +  '!')
# print_greeting_nwith_name('Jake')
# help(print_greeting_nwith_name)
# print_greeting_nwith_name()
# x = print_greeting_nwith_name ('Jane')
# print(x)



# def sum_of_two_numbers(a=0, b=0):
#     '''
#     :param a:The first addend
#     :param b:The secod addend
#     :param :Sum of a and b
    
    
#     '''
#     return a + b
# x = sum_of_two_numbers(45, 7)
# x = sum_of_two_numbers()
# print(x)
# help(sum_of_two_numbers)



# def is_hello_in_text(text):
#     if 'hello'  in text.lower():
#         return True
#     else:
#         return False
# print(is_hello_in_text('Hello everyone!'))




# def is_hello_in_text(text):
#     return  'hello'  in  text.lower()


# print(is_hello_in_text('everyone!'))

# def is_string_in_text(string, text):
#     return string in text
# print(is_string_in_text('he', 'The apple'))
# print(is_string_in_text('hey', 'The aplle'))

def greeting_depends_on_gener(name, gender):
    if gender =='male':
        return gender
        print('Hello'  +   name  + '! You look great!' )
    elif gender == 'famale':
        print('Hello' + name + '! Youare so nice')
    else:
        print('Hello' + name  +  '! I`ve never seen the creature like you!')
returned_value_1 = greeting_depends_on_gener('jake', 'male')
returned_value_2 = greeting_depends_on_gener('jane', 'famale')
returned_value_3 = greeting_depends_on_gener('ja', 'cmale')


print(returned_value_1)
print(returned_value_2)
print(returned_value_3)































































