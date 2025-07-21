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
