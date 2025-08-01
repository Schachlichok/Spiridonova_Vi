# Задача 1 (Создание списка)
# Создай список fruits с тремя фруктами: "яблоко", "банан", "апельсин". Выведи его на экран.

fruits = ["яблоко", "банан", "апельсин"]
print(fruits)

# Задача 2 (Получение элементов списка)
# Дан список:
# numbers = [10, 20, 30, 40, 50]
# Выведи на экран первый и последний элементы этого списка.

numbers = [10, 20, 30, 40, 50]
print(numbers[0], numbers[-1])

# Задача 3 (Добавление элементов в список)
# Дан пустой список:
# shopping_list = []
# Добавь в него элементы "хлеб" и "молоко" (по одному), затем выведи список.

shopping_list = []
shopping_list.append("хлеб")
shopping_list.append("молоко")
print(shopping_list)

# Задача 4 (Слияние списков)
# Даны два списка:
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# Объедини их в один список (без изменения исходных) и выведи результат.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)

# Задача 5 (Добавление элементов в конкретное место списка)
# Дан список:
# tools = ["отвёртка", "дрель", "пила"]
# Вставь слово "молоток" на вторую позицию и выведи обновлённый список.

tools = ["отвёртка", "дрель", "пила"]
tools.insert(1,"молоток")
print(tools)

# Задача 6 (Замена элементов в списке)
# Дан список:
# electronics = ["телефон", "планшет", "ноутбук", "роутер"]
# Замени элемент "планшет" на "телевизор" и выведи обновлённый список.

electronics = ["телефон", "планшет", "ноутбук", "роутер"]
electronics[1] = "телевизор"
print(electronics)

# Задача 7 (Удаление элементов из списка)
# Дан список:
# books = ["Роман", "Детектив", "Фантастика", "Учебник"]
# Удали элемент "Детектив" по значению (не по индексу) и выведи список.

books = ["Роман", "Детектив", "Фантастика", "Учебник"]
books.remove("Детектив")
print(books)

# Задача 8 (Создание списка)
# Создай список colors с пятью цветами на твой выбор
# (например: "красный", "синий" и т.д.) и выведи его.

colors = ["red","white","green","blue", "yellow"]
print(colors)

# Задача 9 (Получение элементов списка)
# Дан список:
# languages = ["Python", "Java", "C++", "JavaScript"]
# Выведи на экран второй и предпоследний элементы этого списка.

languages = ["Python", "Java", "C++", "JavaScript"]
print(languages[1],languages[-2])

# Задача 10 (Очистка списка)
# Дан список:
# temp_list = [1, 2, 3, 4, 5]
# Полностью очисти его (сделай пустым) и выведи результат.

temp_list = [1, 2, 3, 4, 5]
temp_list.clear()
print(temp_list)

# Задача 11 (Добавление элементов в список)
# Дан список:
# numbers = [10, 20, 30]
# Добавь в него числа 40 и 50 (по одному) и выведи обновлённый список.

numbers = [10, 20, 30]
numbers.append(40)
numbers.append(50)
print(numbers)

# Задача 12 (Срезы списков)
# Дан список:
# alphabet = ["a", "b", "c", "d", "e", "f", "g"]
# Выведи срез от 3-го до 5-го элемента включительно (индексы: начало и конец среза).

alphabet = ["a", "b", "c", "d", "e", "f", "g"]
print(alphabet[2:5])

# Задача 13 (Замена элементов через срезы)
# Дан список:
# data = ["яблоко", "груша", "слива", "вишня", "арбуз"]
# Замени срезом элементы "груша", "слива", "вишня" на "персик", "апельсин" и выведи список.

data = ["яблоко", "груша", "слива", "вишня", "арбуз"]
data[1:4] = "персик", "апельсин"
print(data)

shopping_list = []
shopping_list.extend (["хлеб", "яйца"])
print (shopping_list)

numbers = [10, 20, 30, 40, 50]
print (numbers[2:5])

fruits = ["яблоко", "банан", "апельсин", "киви"]
fruits.remove("банан")
print (fruits)

tools = ["отвёртка", "дрель", "пила"]
tools.insert(1,"молоток")
print(tools)

electronics = ["телефон", "планшет", "ноутбук", "роутер"]
electronics[1]="телевизор"
print(electronics)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print (list1+list2)

temp_list = [1, 2, 3, 4, 5]
temp_list.clear()
print(temp_list)

animals = ["кошка", "собака", "тигр", "жираф"]
print(animals[0],animals[-1])

letters = ["a", "b", "c", "d", "e"]
new_letters = letters[2:5]
new_letters.append("f")
print (new_letters)

data = [10, 20, 30, 40, 50]
data[1:4]=25,35
print(data)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0],matrix[1][1])

items = ["яблоко", "банан", "яблоко", "апельсин", "яблоко"]
result = items.count("яблоко")
print(result)

list_a = [1, 2, 3]
list_b = [4, 5]
list_a.extend(list_b)
print(list_a)

original = [1, [2, 3], 4]
copy = original.copy()
copy[1] = 100
print (original,copy)

import copy
original = [10, [20, 30], 40]
deep_copy = copy.deepcopy(original)
deep_copy[1][0] = 99
deep_copy[1][1] = 99
deep_copy[0] = 100
print (original,deep_copy)

# Повторение
# Задача 1 (Создание списка)
# Создай список fruits, содержащий 3 любимых фрукта. Выведи первый и последний элемент.
fruits = ["банан", "манго", "мандарин"]
print(fruits[0], fruits[2])

# Задача 2 (Добавление элементов)
# Дан пустой список numbers = []. Добавь в него числа 5, 10, 15 (по одному) и выведи список.

numbers = []
numbers.append(5)
numbers.append(10)
numbers.append(15)
print(numbers)

# Задача 3 (Срезы списка)
# Дан список:
# letters = ['a', 'b', 'c', 'd', 'e']
# Выведи подсписок с 2-го по 4-й элемент включительно.

letters = ['a', 'b', 'c', 'd', 'e']
print(letters[1:4])

# Задача 4 (Удаление элементов)
# Дан список:
# colors = ['red', 'green', 'blue', 'yellow']
# Удали элемент 'green' и выведи изменённый список.

colors = ['red', 'green', 'blue', 'yellow']
colors.remove("green")
print(colors)

# Задача 5 (Методы списков)
# Дан список:
# data = [3, 1, 4, 1, 5]
# Выполни:
# Сортировку списка
# Подсчёт количества элементов 1
# Выведи результаты.

data = [3, 1, 4, 1, 5]
data.sort()
print(data.count(1))

# Задача 6 (Копирование списка)
# Дан список:
# original = [10, 20, 30]
# Создай его копию (не ссылку!) и измени в копии первый элемент на 100. Выведи оба списка.

original = [10, 20, 30]
my_copy = original.copy()
print (original )
my_copy[0]=100
print (my_copy)

# Задача 7 (Поиск элемента)
# Дан список:
# names = ['Alice', 'Bob', 'Charlie']
# Проверь, есть ли имя 'Bob' в списке, и выведи True/False.

names = ['Alice', 'Bob', 'Charlie']
print("Bob" in names)

# Задача 8 (Объединение списков)
# Даны списки:
# list1 = [1, 2]
# list2 = [3, 4]
# Создай новый список, объединив их, и выведи его.

list1 = [1, 2]
list2 = [3, 4]
print (list1+list2)
################# вложенный список
list1 = [1, 2]
list2 = [3, 4]
list1.append(list2)
print (list1)

# Задача 9 (Очистка списка)
# Дан список:
# temp = [True, False, None]
# Очисти его и выведи пустой список.

temp = [True, False, None]
temp.clear()
print(temp)

# Задача 10 (Генерация списка)
# Создай список чисел от 5 до 10 включительно с помощью list(range()).

print(list(range(5,11)))

# Задача 1 (Метод extend)
# Дан список:
# list1 = [1, 2, 3]
# list2 = [4, 5]
# Добавь все элементы list2 в list1 с помощью extend() и выведи результат.

list1 = [1, 2, 3]
list2 = [4, 5]
list1.extend(list2)
print(list1)

# Задача 1 (Методы расширения списка)
# Дан список:
# main_list = [10, 20, 30]
# extra_data = (40, 50)  # Кортеж
# Добавь все элементы extra_data в main_list. Выбери метод самостоятельно.

main_list = [10, 20, 30]
extra_data = (40, 50)
main_list.extend(extra_data)
print(main_list)

# Задача 2 (Удаление элементов)
# Дан список:
# items = ["A", "B", "C", "D", "E", "F"]
# Удали элементы по условиям:
# Третий элемент по индексу
# Последний элемент
# Элемент со значением "B"

items = ["A", "B", "C", "D", "E", "F"]
del items[2]
items.pop()
items.remove("B")
print(items)

# Задача 3 (Копирование списка)
# Дан список:
# original = [1, [2, 3], 4]
# Создай:
# Поверхностную копию
# Глубокую копию
# Измени вложенный список [2, 3] в обеих копиях. Сравни результаты с оригиналом.

import copy
original = [1, [2, 3], 4]
my_copy = original.copy()
deep_copy = copy.deepcopy(original)
my_copy[1][0] = 0
deep_copy[1][0] = 8
print (original == my_copy)
print (original == deep_copy)

# Задача 4 (Комбинированная работа)
# Дан список:
# data = [["a", "b"], "c", "d"]
# Добавь элементы списка ["e", "f"] в конец
# Удали первый вложенный список
# Создай независимую копию итогового списка

data = [["a", "b"], "c", "d"]
list = ["e", "f"]
data.extend(list)
del data[0]
data_copy = data.copy()
print(data)

# Задача 5 (Очистка списка)
# Дан список:
# temp = [True, None, [1, 2], "text"]
# Полностью очисти список двумя разными методами.

temp = [True, None, [1, 2], "text"]
temp.clear()
print(temp)

temp = [True, None, [1, 2], "text"]
del temp[:]
print(temp)