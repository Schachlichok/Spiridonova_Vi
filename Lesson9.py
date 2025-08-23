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

# 1. Базовые функции
# Задача 1
# Напиши функцию is_even(num), которая возвращает True, если число num чётное, и False — если нечётное.

def is_even(num):
    return num % 2 == 0

print (is_even(6))
print (is_even(7))

# 2. Аргументы по умолчанию
# Задача 2
# Напиши функцию create_user(name, age, city="Москва"), которая возвращает строку:
# "Пользователь [name], [age] лет, город [city]".

def create_user(name, age, city="Москва"):
  return f"Пользователь {name}, {age} лет, город {city}"

print (create_user("Lera", 94))
print (create_user("Lora", 90, "Paris"))

# 3. Возврат нескольких значений
# # Задача 3
# # Напиши функцию min_max(numbers), которая принимает список чисел и возвращает кортеж (минимум, максимум).

def min_max(numbers):
    return min(numbers), max(numbers)
numbers = [9, 8 , 6 , 3]
print (min_max(numbers))

# 4. Декораторы
# Задача 4
# Напиши декоратор @bold, который оборачивает возвращаемую строку функции в HTML-тег <b>.

def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

@bold
def message():
    return "This is string"

print(message())

# Задача 5
# Создай функцию square, которая принимает число и возвращает его квадрат.

def square(num):
    print (num**2)
square(6)

# Задача 6 (Функция, возвращающая словарь)
# Напиши функцию create_user_dict(), которая:
# Принимает три аргумента: name (строка), age (число), city (строка, по умолчанию "Москва").
# Возвращает словарь

def create_user_dict(name,age,city="Москва"):
    return { "name": name ,
"age": age,
"city": city}
print (create_user_dict("Vova", 54))

def greet(name):
    return f"Привет, {name}!"
print(greet("Alla"))

def order(coffee, size="medium"):
    return f"Ваш заказ: {size} {coffee}"
print(order("капучино"))
print(order("капучино", "250мл"))

def multiply(a, b):
    result = a*b
    # return result
    print(f"Результат: {a} * {b} = {result}")

multiply(7, 8)

def greet_decorator(func):
    def wrapper():
        print("Функция начинается...")
        func()
        print("Функция завершена!")
    return wrapper

@greet_decorator
def say_hello():
    print("Привет, мир!")
say_hello()