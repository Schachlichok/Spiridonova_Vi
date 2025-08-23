# Задача 1
# Раздел: Простое наследование
# Создай:Базовый класс Vehicle с методом start_engine(), который выводит "Двигатель запущен"
# Дочерний класс Car, который наследует Vehicle и добавляет метод drive(), выводящий "Машина едет"

class Vehicle:
    def start_engine (self):
        print ("Двигатель запущен")

class Car(Vehicle):
    def drive(self):
        print ("Машина едет")
my_car = Car ()
my_car.start_engine ()
my_car.drive()

# Задача 2
# Раздел: Переопределение методов
# Создай:
# Базовый класс Animal с методом make_sound(), который выводит "Животное издает звук"
# Дочерний класс Dog, который:
# Наследует Animal
# Переопределяет make_sound() → выводит "Гав-гав!"

class Animal:
    def make_sound (self) :
        print ("Животное издает звук")
class Dog(Animal):
    def make_sound (self) :
        print ("Гав-гав")
my_dog = Animal ()
my_dog.make_sound ()
my_dog = Dog ()
my_dog.make_sound ()

# Задача 3
# Раздел: Доступ к атрибутам родителя
# Модифицируй предыдущие классы:
# В базовый класс Animal добавь атрибут species = "животное" в теле класса
# Дочерний класс Dog должен:
# Сохранять переопределенный метод make_sound() (выводит "Гав-гав")
# Добавить метод show_species(), который выводит:
# "Я собака, но я тоже {species}" (где species — атрибут родителя)
# Условия:
# Не создавай species в классе Dog — обращайся к родительскому атрибуту
# Не используй super() (пока что)

class Animal:
    SPECIES = "животное"
    def make_sound (self) :
        print ("Животное издает звук")
class Dog(Animal):
    def make_sound (self) :
        print ("Гав-гав")
    def show_species (self) :
        print (f"Я собака, но я тоже {self.SPECIES} ")
my_dog = Dog ()
my_dog.show_species ()

# Задача 4
# Условие:
# Создай родительский класс Vehicle с методом show_info(), который печатает:
# "Это транспортное средство: {self.name}".
# Создай дочерний класс Car, который наследуется от Vehicle.
# В классе Car определи атрибут name = "Toyota".
# Не переопределяй метод show_info() в Car – он должен остаться из родительского класса.
# Требование:
# Создай экземпляр класса Car и вызови его метод show_info(). В результате должен выводиться текст:
# "Это транспортное средство: Toyota".

class Vehicle:
    def show_info (self):
        print (f"Это транспортное средство: {self.NAME}")
class Car(Vehicle):
    NAME = "Toyota"
my_car = Car ()
my_car.show_info ()

class Person:
    def greet (self):
        print (f"Привет! Меня зовут {self.NAME}.")

class Student (Person):
    NAME = "Алексей"

my_student = Student ()
my_student.greet()

class Device:
    def info (self):
        print ("Это электронное устройство")
class Phone (Device):
    BRAND = "Xiaomi"
    def info (self):
        print (f"Это телефон марки {self.BRAND}")
my_phone = Phone ()
my_phone.info()


class Shape:
    def describe(self):
        return f"Название фигуры: {self.NAME}, её цвет: {self.color}"


class Circle(Shape):
    NAME = "Круг"

    def __init__(self, color, radius):
        self.color = color
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14


class Square(Shape):
    NAME = "Квадрат"

    def __init__(self, color, side):
        self.color = color
        self.side = side

    def area(self):
        return self.side ** 2


circle = Circle("желтый", 3)
square = Square("желтый", 3)

print(circle.describe())
print(square.describe())
print(circle.area())
print(square.area())
