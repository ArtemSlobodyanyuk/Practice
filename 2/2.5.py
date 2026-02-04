class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance   # приватний атрибут

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Сума поповнення має бути додатною")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Недостатньо коштів або некоректна сума")

    def get_balance(self):
        return self.__balance


# Демонстрація
account = BankAccount(1000)

account.deposit(110)
account.withdraw(100)

print("Баланс:", account.get_balance())

# Спроба прямої зміни (не працює)
account.__balance = 10000

print("Баланс після прямої спроби зміни:", account.get_balance())
