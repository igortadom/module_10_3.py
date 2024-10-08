import threading
import time
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            replenishment = randint(50, 500)
            self.balance += replenishment
            print(f'Пополнение: {replenishment}. Баланс: {self.balance} ')
            if self.balance >= 500 and self.lock.locked():
               self.lock.release()
            time.sleep(0.001)




    def take(self):
        for i in range(100):
            take_money = randint(50, 500)
            print(f'Запрос на {take_money} ')
            if take_money <= self.balance:
                self.balance -= take_money
                print(f'Снятие: {take_money}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')