grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = ['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron']
res = students.sort()
Num = (grades[0])
average = sum(Num) / len(Num)
grades[0] = average
Num = (grades[1])
average = sum(Num) / len(Num)
grades[1] = average
Num = (grades[2])
average = sum(Num) / len(Num)
grades[2] = average
Num = (grades[3])
average = sum(Num) / len(Num)
grades[3] = average
Num = (grades[4])
average = sum(Num) / len(Num)
grades[4] = average
klass = dict(zip(students, grades))
name = input('введите имя ученика: ')
print(klass.get(name))
numbers = (klass.get(name))
print(klass)