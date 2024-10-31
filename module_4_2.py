def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function() # ничего не выводит
#inner_function() # выдает ошибку, вследствие различия пространства имён
test_function() # все работает
