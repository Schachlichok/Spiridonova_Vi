temperature = 25
if temperature >30:
    print (Жарко)
else:
    print("Приемлемо")

temperature = 25
result = "Жарко" if temperature >30 else "Приемлемо"
print (result)

password = "qwerty123"
if password == "admin":
    print("Доступ разрешён")
else:
    print("Доступ запрещён")

password = "qwerty123"
result = "Доступ разрешён" if password == "admin" else "Доступ запрещён"
print (result)

score = 85
if score >= 90:
    print ("Отлично")
elif score >= 70:
    print ("Хорошо")
else:
    print ("Удовлетворительно")

score = 85
result = "Отлично" if score >= 90 else "Хорошо" if score >= 70 else "Удовлетворительно"

age = 20
has_ticket = True
if age >= 18 and has_ticket:
    print ("Проход разрешён")
else:
    print ("Проход запрещён")

is_weekend = False
temperature = 28
if is_weekend or (temperature > 25 and is_weekend == False ):
    print ("Идём гулять")
else:
    print ("Не идём гулять")

is_weekend = False
temperature = 28
result = "Идём гулять" if is_weekend or (temperature > 25 and is_weekend == False) else "Не идём гулять"
print (result)

balance = 100
result = "Пополнить баланс" if balance < 50 else "Достаточно"
print (result)

is_member = True
total_purchase = 12000
if is_member or total_purchase > 10000:
    print ("Скидка 10%")

has_umbrella = True

is_raining = True
temperature = 15
print("Идем гулять" if (has_umbrella and is_raining) or temperature > 20 else "")

is_restricted = False
if not is_restricted:
    print ("Доступ открыт")

score = 85
if score>=60:
    print ("Проходной балл")

age = 17
if age >=18:
    print ("Вход разрешён")
else:
    print ("Вход запрещён")

temperature = -5
if temperature > 30:
    print ("Жарко")
elif temperature < 10:
    print ("Холодно")
else:
    print ("Тепло")

has_ticket = True
is_weekend = False
if has_ticket and  not is_weekend:
    print ("Идём в кино")

balance = 45
print ("Пополнить баланс" if balance < 50 else "Остаток достаточный")

age = 18
if age>=18:
    print("Доступ разрешён")
else:
    print("Доступ запрещён")

num = 8
if num%2 ==0 and num>0:
    print("Число четное и положительное")
elif num%2 == 0 and num<0:
    print("Число четное и отрицательное")
elif num%2 != 0 and num>0:
    print("Число нечетное и положительное")
elif num%2 != 0 and num<0:
    print("Число нечетное и отрицательное")
else:
   print("Число является нулем")
# //////////////////

num = 8
if num%2 ==0:
    print("Число четное")
else:
    print("Число нечетное")
if num>0:
    print("Число положительное")
# //////////////////

has_ticket = True
is_weekday = False
if has_ticket or (not is_weekday and has_ticket):
    print("Можно в кино")

x = 10
y = 5
z = 15
if x>y and x>z:
    print("x наибольший из трёх чисел")
if y < z < x:
    print("z среднее по величине число")

balance = 50
status =  "Пополнить баланс" if balance<100 else "Достаточно"
print (status)

text = "Python"
print(text.startswith("Pyt"))
print(len(text) >5)

grade = 4
if grade == 5:
    print("Отлично")
elif grade == 4:
    print("Хорошо")
elif grade == 3:
    print("Удовлетворительно")
else:
    print("Неуд")


number = 25
if 20<=number<=30:
    print("В диапазоне")

items = (10, 20, 30)
result ="Есть" if 20 in items else "Нет"
print(result)

is_member = True
total_purchase = 1500
result = "Скидка 10%" if is_member and total_purchase>1000 else "Нет скидки"
print(result)

