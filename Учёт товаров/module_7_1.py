from pprint import pprint



class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self. category = str(category)
    def __str__(self):
        str_product = f'{self.name}, {self.weight}, {self.category}'
        return  str_product

class Shop: # tuple
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r+')
        prod_str = file.read()
        file.close()
        # pprint(prod_str)
        return prod_str

    def add(self, *products):
        file_get = self.get_products()
        for i in products:
            if self.get_products().find(f'{i.name},') == -1:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()
            else:
                print(f'Продукт {i.name} уже есть в магазине')




s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # _str_

s1.add(p1, p2, p3)

print(s1.get_products())