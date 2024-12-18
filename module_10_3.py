import threading
import random
import  time

lock = threading.Lock()
balance = 0
class Bank:
    def __init__(self, balance: int):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        global balance
        lock.acquire()
        for i in range(100):
            if balance >= 500 and lock.locked() == True:
                lock.release()
            random_number = random.randint(50, 500)
            balance += random_number
            print(f"Пополнение: {random_number}. Баланс: {balance} {lock.locked()}")
            time.sleep(0.01)


    def take(self):
        global balance
        lock.acquire()

        for i in range(100):
            random_number = random.randint(50, 500)
            print(f"Запрос на {random_number}")
            if random_number <= balance:

                balance -= random_number
                print(f"Снятие: {random_number}. Баланс: {balance} {lock.locked()}")
                time.sleep(0.001)
            else:
                print("Запрос отклонён, недостаточно средств")
                lock.acquire()





bk = Bank(0)
# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {balance}')