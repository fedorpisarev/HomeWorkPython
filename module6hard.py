class Figure:
    sides_count = 0
    def __init__(self, color, *sides):

        self.__sides = []
        self.__color = []
        self.filled = False
        useful_sides = None

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        colors = [r, g, b]
        for color in colors:
            if not (0 <= color <= 255):
                return False
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) == True: self.__color = [r, g, b]


    def __is_valid_sides(self, sides):

        if len(sides) == self.useful_sides and (0 not in sides):
            return True
        return False


    def set_sides(self, *args):
        old_sides = self.__sides

        if self.__is_valid_sides(args) == True:
            self.__sides = list(args)

        if "Triangle" in str(self):
            if self.is_triangle_impossible() is True:
                self.__sides = old_sides
            return

        if self.useful_sides == 1:
            list_ = []
            for i in range(self.sides_count):
                list_.append(self.__sides[0])
            self.__sides = list_
            del list_

    def get_sides(self):
        return self.__sides

    def __len__(self):
        if self.__sides is not None:
            return sum(self.__sides)
        else:
            return 0

class Circle(Figure):
    sides_count = 1
    useful_sides = 1

    def __init__(self, *args):
        Figure.__init__(self, *args)
        self.__radius = None

    def get_square(self):
        return 3.14 * (self.__radius ** 2)



class Triangle(Figure):
    def __init__(self):
        super().__init__(sides_count=3)
        self.__base = 0
        self.__height = 0

    def get_square(self):
        return (self.__base * self.__height) / 2

class Cube(Figure):
    def __init__(self,color, side=1):
        sides_count=12
        self.__side = side

    def get_sides(self):
        return [self.__side] * 12

    def get_volume(self):
        return self.__side ** 3

    def set_sides(self, side):
        if side <= 0:
            return
        self.__side = side

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

cube1.set_color(222, 35, 130)
cube1.set_sides(6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())

cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(6)
print(cube1.get_sides())

circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())