#immutable_var = 200, "fish", True
#print(immutable_var)
#immutable_var[1] = 'рыба'
#print(immutable_var)
immutable_var = 200, "fish", True
print(immutable_var)
print('Это кортеж, а выше была попытка внести изменения в кортеж, в отличии от списка он не изменяем, такие дела.')
mutable_list = [200, "fish", True]
print(mutable_list)
mutable_list[1] = 'рыба'
print(mutable_list)
print('А это был СПИСОК, его можно изменять и у нас получилось! Вот они для наглядности: Кортеж и Список')
print(immutable_var)
print(mutable_list)

