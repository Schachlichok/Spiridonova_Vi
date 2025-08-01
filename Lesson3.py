# Практикуем длинное предложение
from builtins import PythonFinalizationError

long_text = """Практикуем очень
очень
очень длинное предложение"""
print (long_text)

# Практикуем перенос строки

new_line = "начем писать \nс новой строки"
print (new_line)

print ("чтоб не тратиь время\nбудем писать сразу в принте")

# Индекс элемента
#       0123456
text = "t e x t"
#      -7-5-3-1

print(text[2])
print(text[-1])

# Срезы-извлечение части слова из строки
# Любая перменная = текущая переменная [начало:конец:шаг] или [::h]-от начала до конца с h-шагом/[::-1] (обр шаг)
# Принцип- срезается от указанного индекса до конечного, но конечный не включается. Шаг (h)- срезается каждый h-ый элемент.

text = "python"
result = text [0:6:2]
print(result)

# len(переменная)-длина перем-й.
# конкатенация - просто сложение переменных типа str
item_name = "iphone 15 pro"
item_price = " 555$"
print (item_name + item_price)

# f строки- позволяют вписывать в строки переменные или то, что нам надо.
# просто ставим f перед кавычками, а остальное вписываем в фигурные скобки
print (f"я купила {item_name} за {item_price}")
# Или
print (f"стоимость нового {item_name + item_price}")


# Практика
# Задача 1 (Создание строки)
# Создай строку "Hello, Python!" и выведи её на экран.

stroka = "Hello, Python!"
print(stroka)

# Задача 2 (Доступ к символам)
# Дана строка:
# text = "Программирование"
# Выведи на экран 3-й символ этой строки.

text = "Программирование"
print(text[2])

# Задача 3 (Срезы)
# Дана строка:
# word = "автоматизация"
# Выведи на экран срез с 3-го по 7-й символ включительно

word = "автоматизация"
print(word[2:7])

# Задача 4 (Получение длины строки)
# Дана строка:
# s = "Интерпретатор"
# Выведи на экран её длину (количество символов)
s = "Интерпретатор"
print(len(s))

# Задача 5 (Конкатенация строк)
# Даны две строки:
# part1 = "Hello, "
# part2 = "world!"
# Объедини их и выведи результат на экран без пробелов между переменными в коде.
part1 = "Hello, "
part2 = "world!"
part1_1 = part1.strip()
print(f"{part1_1}{part2}")
print(part1_1 + part2)

# Задача 6 (Базовые методы строк)
# Дана строка:
# s = "   python is great   "
# Удали лишние пробелы в начале и конце строки и выведи результат.

s = "   python is great   "
print(s.strip())

# Задача 7 (F-строки)
# Даны переменные:
# language = "Python"
# year = 1991
# Используя f-строку, выведи сообщение:
# "Язык Python был создан в 1991 году."

language = "Python"
year = 1991
print(f"Язык {language} был создан в {year} году")

# Задача 8 (Срезы + конкатенация)
# Дана строка:
# text = "Обучение"
# Выведи на экран слово "чение" (используй срез)
# и затем допиши к нему " — это просто!" (без кавычек в итоговой строке).

text = "Обучение"
print(f"{text[3:8]}— это просто!")

# Задача 9 (Базовые методы строк)
# Дана строка:
# s = "СОБАКА"
# Приведи все её символы к нижнему регистру и выведи результат

s = "СОБАКА"
print(s.lower())

# Задача 10 (Последняя! Получение длины + F-строка)
# Дана строка:
# word = "дизайн"
# Выведи сообщение:
# "В слове 'дизайн' 6 букв"
# (число должно подставляться автоматически через len()).

word = "дизайн"
print(f"В слове '{word}' {len(word)} букв")

# Закрепление темы
text = "Программирование"
print (text[0], text[-1])

s = "Автоматизация"
print (s[3:8])

phrase = "   Hello, World!   "
print (phrase.strip().lower())

city = "Москва"
population = 12_000_000
print (f"В городе {city} живёт {population} человек.")

part1 = "Python"
part2 = " — это сила!"
print (part1+part2)

word = "автомобиль"
result = word.startswith("авто")
print (result)

file = "document.pdf"
result = file.endswith(".pdf")
print(result)

text = "Изучаем Python"
"Python" in text
print("Python" in text)

s = "   Hello World!   "
print (s.strip())

data = "!!ПРИМЕР, СТРОКИ!!"
print (data.lower().strip("!"))

text = "Я изучаю Python и Python это круто"
print (text.replace("Python","программирование"))

s = "банан, яблоко, банан, груша, банан"
print("банан" in s)  # Проверка наличия (True)
print(s.count("банан"))

# Повторение
# Задача 1 (Срезы строк)
# Дана строка:
# text = "автоматизация"
# Выведи подстроку с 3-го по 7-й символ включительно.

text = "автоматизация"
print(text[2:7])

# Задача 2 (Методы строк)
# Дана строка:
# s = "   Hello, World!   "
# Удали лишние пробелы в начале и конце строки и выведи результат.

s = "   Hello, World!   "
print(s.strip())

# Задача 3 (Конкатенация)
# Даны две строки:
# part1 = "Python"
# part2 = " - это сила!"
# Объедини их в одну строку без пробелов между переменными в коде.

part1 = "Python"
part2 = "- это сила!"
print(part1+part2)

# Задача 4 (F-строки)
# Даны переменные:
# city = "Москва"
# population = 12_000_000
# Выведи строку: "В городе Москва живёт 12_000_000 человек".

city = "Москва"
population = 12_000_000
print(f"В городе {city} живёт {population} человек")

# Задача 5 (Поиск подстроки)
# Дана строка:
# text = "Я изучаю Python и Python это круто"
# Найди и выведи индекс первого вхождения слова "Python".

text = "Я изучаю Python и Python это круто"
print(text.find("Python"))

# Задача 6 (Замена подстроки)
# Дана строка:
# sentence = "Я люблю Java"
# Замени слово "Java" на "Python" и выведи результат.

sentence = "Я люблю Java"
print (sentence.replace("Java","Python"))

# Задача 7 (Регистр символов)
# Дана строка:
# word = "ПРОГРАММИРОВАНИЕ"
# Приведи все символы к нижнему регистру и выведи результат.

word = "ПРОГРАММИРОВАНИЕ"
print(word.lower())

# Задача 8 (Разделение строки)
# Дана строка:
# data = "яблоко,банан,апельсин"
# Разбей строку по запятым в список фруктов и выведи список.

data = "яблоко,банан,апельсин"
print(data.split(","))

# Задача 9 (Длина строки)
# Дана строка:
# password = "Secret123"
# Выведи длину этой строки.

password = "Secret123"
print(len(password))

# Задача 10 (Повторение строки)
# Дана строка:
# symbol = "*"
# Выведи эту строку повторённую 10 раз подряд.

symbol = "*"
print(symbol * 10)

password = "erpr"
print(password == password[::-1])

password = "0123456789"
print(password[::3])

password = "0123456789!"
print(password.strip("!"))
print(id(password))

filename = "document.pdf"
print(filename.startswith("doc"))
print(filename.endswith(".pdf"))

text = "https://example.com"
print ("Веб-адрес" if text.startswith("http://") or text.startswith("https://") else "Неизвестный формат")

data = "  REPORT_2023.txt  "
print(data.strip().startswith("REPORT"))
print(data.strip().endswith(".txt"))

def divide(a, b):
    assert b!=0, "b равно нулю"
    return a/b
print(divide(int(input ("Введите а")),int(input ("Введите b"))))

def check_login(login):
    assert len(login)>=5, "Логин должен быть минимум 5 символов"
    assert " " not in login, "Логин должен быть без пробелов"
    return True
print(check_login("muxomor122"))