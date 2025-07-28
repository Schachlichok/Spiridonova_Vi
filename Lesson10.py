# 1. Создание класса
# Задача: Создай пустой класс Robot
# 2. Добавь в класс Robot общий атрибут
# material = "metal", который будет одинаковым для всех роботов.
# 3. Добавь конструктор __init__
# в класс Robot, чтобы при создании робота можно было задавать его name
# 4.(из раздела "Методы класса"):
# Добавь метод greet в класс Robot,
# который будет возвращать строку "Hello, my name is [name]!", где [name] - это имя робота.
# 5.Следующая задача (из раздела "Объект класса"):
# Создай объект класса Robot с именем "C-3PO" и вызови его метод greet
# 6.Следующая задача (закрепляем параметр self):
# Добавь в класс Robot метод describe, который будет выводить:
# "I am made of {MATERIAL} and my name is {name}"
from email.errors import BoundaryError


class Robot:

    MATERIAL = "metal"
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}!")

    def describe(self):
        print(f"I am made of {self.MATERIAL} and my name is {self.name}")

my_robot = Robot("C-3PO")
my_robot.greet()
my_robot.describe()

# 7.Создай класс Book с:
# Атрибутами класса cover_type = "paperback"
# Конструктором, принимающим title и author
# Методом info, который возвращает строку "{title} by {author}"

class Book:
    COVER_TYPE = "paperback"

    def __init__(self,title,author):
        self.title = title
        self.author = author

    def info(self):
        print(f"{self.title} by {self.author}")

my_book = Book("Дюймовочка","Г.Х.Андерсен")
my_book.info()

# Создай класс Wallet:
# Атрибут класса currency = "RUB" (валюта)
# Конструктор, принимающий:
# owner (владелец)
# balance (баланс, по умолчанию 0)
# Методы:
# add_cash(amount) → увеличивает баланс на amount и выводит:
# "В кошелек добавлено {amount} {currency}"
# spend_cash(amount) → уменьшает баланс, если хватает денег.
# Если не хватает → "Недостаточно средств"
# check_balance() → возвращает строку:
# "У {owner} в кошельке {balance} {currency}"

class Wallet:

    CURRENCY = "RUB"
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def add_cash(self):
        print(f"В кошелек добавлено столько-то {self.CURRENCY}")

    @staticmethod
    def spend_cash():
        print(f"Недостаточно средств")

    def check_balance (self):
        print(f" У {self.owner} в кошельке {self.balance} {self.CURRENCY}")

my_wallet = Wallet ("меня",222)
my_wallet.add_cash()
my_wallet.spend_cash()
my_wallet.check_balance()
