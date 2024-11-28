

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']



first_result =  (len(i) - len(x) for i, x in zip(first, second) if len(i) != len(x))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))


print(list(first_result))
print(list(second_result))