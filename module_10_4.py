import threading
import queue
import random
import time


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None  # Гость по умолчанию None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        wait_time = random.randint(3, 10)
        time.sleep(wait_time)  # Ожидание
        print(f"{self.name} покушал(-а) и ушёл(ушла)")


class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            available_table = self.find_available_table()
            if available_table is not None:
                available_table.guest = guest
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {available_table.number}")
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def find_available_table(self):
        for table in self.tables:
            if table.guest is None:  # Если стол свободен
                return table
        return None  # Если все столы заняты

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None

                if table.guest is None and not self.queue.empty():
                    next_guest = self.queue.get()
                    table.guest = next_guest
                    print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                    next_guest.start()




    # Создание столов
tables = [Table(number) for number in range(1, 6)]

    # Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya',
    'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel',
    'Ilya', 'Alexandra'
]

    # Создание гостей
guests = [Guest(name) for name in guests_names]

    # Заполнение кафе столами
cafe = Cafe(*tables)

    # Приём гостей
cafe.guest_arrival(*guests)

    # Обслуживание гостей
cafe.discuss_guests()
