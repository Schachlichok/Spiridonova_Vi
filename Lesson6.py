# Задача 1 (Создание словаря)
# Создай словарь student с ключами: "name" (значение — твоё имя)
# и "age" (твой возраст). Выведи словарь.

student = {"name": "Виктория", "age": 25}
print (student)

# Задача 2 (Доступ к элементам по ключу)
# Дан словарь:
# book = {"title": "Гарри Поттер", "author": "Дж. Роулинг", "year": 1997}
# Выведи значение ключа "author".

book = {"title": "Гарри Поттер", "author": "Дж. Роулинг", "year": 1997}
print (book["author"])

# Задача 3 (Добавление элемента)
# Дан словарь:
# car = {"brand": "Toyota", "model": "Camry"}
# Добавь ключ "year" со значением 2020 и выведи обновлённый словарь.

car = {"brand": "Toyota", "model": "Camry"}
car["year"] = 2020
print (car)

# Задача 4 (Удаление элемента)
# Дан словарь:
# person = {"name": "Алексей", "age": 30, "city": "Москва"}

person = {"name": "Алексей", "age": 30, "city": "Москва"}
del person["age"]
print(person)

# Задача 5 (Проверка наличия ключа)
# Дан словарь:
# device = {"type": "smartphone", "brand": "Xiaomi", "os": "Android"}

device = {"type": "smartphone", "brand": "Xiaomi", "os": "Android"}
print( "os" in device)

# Задача 6 (Получение всех ключей)
# Дан словарь:
# country = {"name": "Франция", "capital": "Париж", "language": "французский"}

country = {"name": "Франция", "capital": "Париж", "language": "французский"}
print (country.keys())

# Задача 7 (Обновление значения)
# Дан словарь:
# product = {"name": "Ноутбук", "price": 50000, "in_stock": True}
# Измени значение ключа "price" на 45000 и выведи обновлённый словарь.

product = {"name": "Ноутбук", "price": 50000, "in_stock": True}
product["price"]=45000
print(product)

# Задача 8 (Получение значений)
# Дан словарь:
# movie = {"title": "Интерстеллар", "director": "Нолан", "year": 2014}
# Выведи все значения этого словаря в виде списка.

movie = {"title": "Интерстеллар", "director": "Нолан", "year": 2014}
print(movie.values())

# Задача 9 (Проверка наличия значения)
# Дан словарь:
# fruit = {"name": "Яблоко", "color": "зелёное", "weight": 150}
# Проверь, есть ли в словаре значение "зелёное", и выведи True или False.

fruit = {"name": "Яблоко", "color": "зелёное", "weight": 150}
print("зелёное" in fruit.values())

# Задача 10 (Добавление через update())
# Дан словарь:
# user = {"name": "Мария", "email": "maria@example.com"}
# Добавь к нему ключ "age" со значением 28 через метод update() и выведи обновлённый словарь.

user = {"name": "Мария", "email": "maria@example.com"}
user["age"] = 28
print(user)

# Задача 11 (Метод pop())
# Дан словарь:
# data = {"id": 101, "status": "active", "count": 42}
# Удали ключ "count" через pop() и выведи удалённое значение.

data = {"id": 101, "status": "active", "count": 42}
count = data.pop("count","Count not found")
print(count)

student = {"name": "Viola", "age": "30", "courses": "русский, математика, литература"}
print(student)

book = {"title": "1984", "author": "Оруэлл", "year": 1949}
author = book["author"]

student = {"name": "Nicola", "age": 14, "courses": ["Python", "Автоматизация"]}
print(student)

car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
print(car["model"])

book = {"title": "1984", "author": "Оруэлл"}
book["year"] = 1949
print(book)

pc = {"brand": "HP", "ram": 16, "cpu": "Intel", "year": 2022}
del pc["year"]
print(pc)

pc = {"brand": "HP", "ram": 16, "cpu": "Intel", "year": 2022}
pc.pop("year")
print(pc)

phone = {"model": "iPhone 13", "color": "black", "storage": 128}
print(phone.keys())
print(phone.values())

laptop = {"brand": "Lenovo", "os": "Windows", "price": 750}
print("os" in laptop)
if "os" in laptop:
    print(laptop["os"])

profile = {"name": "Alex", "age": 30}
profile["city"] = "Москва"
profile["job"] = "Инженер"