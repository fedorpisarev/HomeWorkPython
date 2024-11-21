def add_everything_up(a ,b):
    try:
        sum = a + b
        print(sum)
    except TypeError:
        mus = f'{a}{b}'
        print(mus)





add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)
