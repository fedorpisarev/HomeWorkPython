class Vehicle:
    __COLOR_VARIANTS = ['Red', 'Green', 'Blue', 'White', 'Black', 'Yellow', 'Gray']
    __COLOR_VARIANTS = list(map(str.lower, __COLOR_VARIANTS))

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self._model = __model
        self.power = __engine_power
        self._color = __color
    def get_model(self, model):
        pass

    def get_horsepower(self, power):
        pass

    def get_color(self, _color):
        pass


    def print_info(self):
        print(f"Модель: {self._model}")
        print(f"Мощность двигателя: {self.power}")
        print(f"Цвет: {self._color}")
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        reg_colours = [colour.lower() for colour in self.__COLOR_VARIANTS]  # для проверки без учета регистра
        if new_color.lower() in reg_colours:
            self._color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5




# Текущие цвета
__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()




