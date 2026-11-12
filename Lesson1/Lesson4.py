# Завдання 1
# time = int(input("Введіть час у хв.:"))

# if time >0:
#     sec = time * 60
#     print(f"Це {sec} секунд")
# else:
#     print("Час має бути додатнім!")

# Завдання 2

# pasword = input("Введіть пароль:")
#
# if pasword == "OpenSesame123":
#     print("Доступ дозволено!")
# else:
#     print("Доступ заблоковано!")

# Завдання 3
#
# length = int(input("Введіть довжину в метрах:"))
# unit = input("В які одиниці перевести?: (см чи км):")
#
# if unit == "см":
#     print(f"{length*100}см.")
# elif unit == "км":
#     print(f"{length/1000}км.")
# else:
#     print("Помилка! Введіть СМ чи КМ")

#Завдання 4

#
# answer = input("Відповідь на Велике Питання Життя, Всесвіту і Всього Іншого:")

#
# if answer == "42":
#     print("Правильно")
# #
# elif answer == "сорок два":
#     print("Правильно")
# elif answer== "сорок-два":
#     print("Правильно")
# else:
#  print("Не правильно")
#
#  elif answer == "42":
#  print("Правильно") ----- # Лишній рядок так як дана умова вже вказана в строці 37

# Завдання 5

# grade = int(input("Введіть оцінку: "))
# if grade == 2:
#     print("Незадовільно")
# elif grade == 3:
#     print("Задовільно")
# elif grade == 4:
#     print("Добре")
# elif grade == 5:
#     print("Відмінно")
# else:
#     print("Оцінка має бути від 2 до 5")

# Завдання 6

# pizza_price = float(input("Ціна піцци:"))
# pizza_quantity = int(input("Кількість піц:"))
# budget = float(input("Ваш бюджет:"))
#
# total_price =float(pizza_price * pizza_quantity)
#
# if budget>total_price:
#     print(f"Вам достатньо грошей на {pizza_quantity} піцци")
# else:
#     print(f"Вам не вистачає {total_price - budget}грн.")

# Завдання 7

number = int(input("Введіть число: "))

if number % 2 == 0:
    print(number, "Even number")
else:
    print(number, "Odd number")




