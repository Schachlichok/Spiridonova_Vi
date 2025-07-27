# file = open("Message", "w", encoding="utf-8")
# file.write("Обновление записи\nПрошло успешно")

# file = open("Message", "r", encoding="utf-8")
# # print(file.readline())
#
# for line in file.readlines():
#     print(line)

# file = open("Message", "a", encoding="utf-8")
# file.write("\nНовая строка успешно добавлена")

# file = open("Message", "r+", encoding="utf-8")
# for line in file.readlines():
#     print(line)
# file.seek(0) # номер элемента откуда читать
# print (file.read())
# #
# file.write("Начало")
# file.close()

# Обязательно нужен контекстный менеджер, для предотвращения зависшего
# открытого файла и закрытия файла при выходе из блока

# with open("Message", "r+", encoding="utf-8") as file:
#   print(file.read())

# with open("Message", "r+", encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())

# with open("Message", "w") as file:
#     file.write("Привет, мир") # Записываем строку в файл
#     file.write("Это пример записи в файл.") # Добавляем еще одну строку

# with open("Message", "r") as file:
#     content = file.read() # Читаем содержимое файла
#     print(content)

# Задача 1 (Чтение файла)
# Дан файл notes.txt с текстом:
# Первая строка
# Вторая строка
# Напиши код, который выводит содержимое всего файла на экран.
#
# file = open("notes.txt", "r", encoding="utf-8")
# print(file.read())
# file.close()

# Задача 2 (Запись в файл)
# Создай файл output.txt и запиши в него строку: "Тест записи файла"

with open("output.txt", "w+", encoding="utf-8") as file:
    file.write("Тест записи файла")
    file.seek(0)
    print(file.read())

# Задача 3 (Добавление в файл)
# Дополни файл output.txt строкой "\nДополнительная строка"
# без перезаписи всего содержимого.

with open("output.txt", "a+", encoding="utf-8") as file:
    file.write("\nДополнительная строка")
    file.seek(0)
    print(file.read())

# Задача 4 (Чтение по строкам)
# Дан файл data.txt с содержимым:

# with open ("data.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         print("Запись:", line.strip())

# Задача 5 (Контекстный менеджер и запись)
# Создай новый файл log.txt и запиши в него три строки (каждая через отдельный write()):

with open("log.txt", "w+", encoding="utf-8") as file:
    file.write("1: Начало работы")
    file.write("\n2: Процесс выполнения")
    file.write("\n3: Конец работы")
    file.seek(0)
    print(file.read())

