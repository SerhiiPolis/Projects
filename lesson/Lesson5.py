#  Завдання 1


# age = int(input("Введіть свій вік:"))
# if 18 < age < 65:
#     print("Працездатний/на")
# else:
#     print("Непрацездатний/на")

# Завдання 2

# login = input("Введіть логін:")
# pasword = input("Введіть пароль:")
#
#
# if pasword == "OpenSesame123" and login == "AliBaba":
#     print("Доступ дозволено!")
# else:
#     print("Доступ заблоковано!")


# Завдання 3

# price = float(input("Ціна товару:"))
# quantity = int(input("Кількість товару:"))
# total = price * quantity
#
# age = int(input("Ваш вік:"))
#
# if age < 18 or age > 65:
#     print(f"Сума зі знижкою 15%:{total - (total * 0.15)}")
# else:
#     print(f"Сума покупки:{total}")

# Завдання 4

# age = 25
# has_license = "так"
# accidents = 0
#
# if age >= 18 and has_license == "так" and accidents == 0:
#     print("Оренда дозволена")
# else:
#     print("Оренда заборонена")

# Завдання 5

# price = float(input("Введіть ціну покупки:"))
# delivery = 120
# total = price + delivery
# discount1 = delivery - (delivery * 0.05)
# discount2 = delivery - (delivery * 0.2)
#
# if 500 < price < 1000:
#     print(f"Загальна ціна:{price + discount1}")
# elif 1000 < price < 2000:
#     print(f"Загальна ціна:{price + discount2}")
# elif price > 2000:
#     print("Загальна ціна:", price)
# else:
#     print(f"Загальна ціна:{total}")

# Завдання 6

# sum = float(input("Сума вкладу:"))
# year = int(input("Термін вкладу в роках:"))
#
# if sum <= 10000 and year < 3:
#     percent = 0.08
# elif sum <= 10000 and year > 3:
#     percent = 0.1
# elif 10001 <= sum < 50000 and year < 3:
#     percent = 0.12
# elif 10001 <= sum < 50000 and year > 3:
#     percent = 0.14
# else:
#     percent = 0.2
#
# total = sum * (1+percent)**year
# pay = total / (year * 12)
# print(f"Ставка відсотка:{100 * percent}%")
# print(f"Загальна сума кредиту:{total:.2f} ")
# print(f"Щомісячний платіж:{pay:.2f}")
