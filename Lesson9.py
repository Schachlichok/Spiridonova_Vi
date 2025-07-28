# Задача 1 (Создание и вызов функций)
# Напиши функцию print_hello(), которая выводит строку "Hello, Python!" при вызове.

def print_hello():
    print("Hello, Python!")

print_hello()

# Задача 2 (Аргументы функций)
# Напиши функцию multiply(a, b), которая:
# Принимает два числа как аргументы.
# Возвращает их произведение (не выводит!).

# def multiply(a, b):
#     return a*b
# result = multiply(int(input("Введите a:")), int(input ("Введите b:")))
# print (result)

# Задача 3 (Аргументы с дефолтными значениями)
# Напиши функцию greet(name, greeting="Привет"), которая:
# Принимает имя (name) и опциональный аргумент greeting (по умолчанию "Привет").
# Возвращает строку в формате "[greeting], [name]!".

def greet(name, greeting="Привет"):
    return f"{greeting}, {name}!"

print (greet("Vika"))
print (greet("Vika","Hello"))

# Задача 4 (Возврат нескольких значений)
# Напиши функцию calculate(a, b), которая:
# Принимает два числа
# Возвращает три значения: сумму, разность и произведение
# Результат должен возвращаться как кортеж

def calculate(a, b):
    return a+b, a-b, a*b
result = calculate(2, 3)
print (result)

# Задача 5 (Декораторы)
# Напиши декоратор @uppercase, который преобразует возвращаемое значение функции к верхнему регистру.

def uppercase(func):
    def wrapper():
        print(func().upper())
    return wrapper

@uppercase
def my_string():
    return "hello, world"

my_string()

