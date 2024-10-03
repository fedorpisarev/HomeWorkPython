def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
#print_params(1, 'строка', True)
#print_params(b = 25) # оно работает
#print_params(c = [1,2,3]) # оно тоже
#values_list = [9, 'stroka', True]
#values_dict = {'a': 2, 'b': 6,'c': 8}
#print_params(*values_list)
#print_params(**values_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42) # и снова работает!!!