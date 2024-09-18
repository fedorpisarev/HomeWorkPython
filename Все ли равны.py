first = input('Напиши число: ')
second = input('напиши еще одно: ')
third = input('это последнее, честно: ')
if first == second == third:
print(3)
elif first == second or first == third or second == third:
print(2)
else:
print(0)
