import threading
from time import sleep


class Knight(threading.Thread):
    total_enemies = 100
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemies = Knight.total_enemies

        while enemies > 0:
            sleep(1)
            self.days += 1
            enemies -= self.power
            if enemies < 0:
                enemies = 0
            print(f"{self.name} сражается {self.days}...", f"осталось {enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} {'день' if self.days == 1 else 'дня'}!")

    # Создание объектов класса Knight
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
    # Запуск потоков
first_knight.start()
sleep(0.1)
second_knight.start()


