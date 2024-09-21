my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list2 = []
print(my_list)
num = 0
while num <= len(my_list):
    number = (int(input('введите цифру: ')))
    if number > 0:
        my_list2.append(number)
        print()
    elif number == 0:
        print()
    else:
        break
    num += 1
print(my_list2)
