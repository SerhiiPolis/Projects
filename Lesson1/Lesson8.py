# Завдання 1

# name = input("Введіть своє ім'я:")
#
# while True:
#     age  = int(input("Введіть свій вік:"))
#     if age > 0:
#         break
#
#     print("Введіть правильний вік:")
#
# print(f"Привіт {name}. Тобі {age} років. ")

# Завдання 2
# total = 0
# goal = float(input("Цільова сума? "))
#
# while True:
#     daily_amount = float(input("Сьогоднішній вклад? "))
#     total += daily_amount
#     if total >= goal:
#         break
#
# print(f"Мету досягнуто! У скарбничці {total} грн.")

# Завдання 3

# while True:
#
#     lenght = float(input("Введіть довжину в метрах"))
#     yard = lenght / 0.9144
#     foot = lenght / 0.3048
#     print(f"Це {yard:.2f} ярдів чи {foot:.2f} футів")
#
#     ans = input("Закінчити роботу?(так/ні):")
#     if ans == "так":
#         break


# Завдання 4

# total = 0
# goal = float(input("Цільова сума? "))
# days = 0
# while True:
#     daily_amount = float(input("Сьогоднішній вклад? "))
#     total += daily_amount
#     days += 1
#     if total >= goal:
#         break
#
# print(f"Мету досягнуто за {days} днів! У скарбничці {total} грн.")

# Завдання 5

# total_items = 0
# print("Додайте товари. Для завершення введіть 'stop'.")
#
# while True:
#     item = input("Введіть товар: ")
#
#     if item == "stop":
#         print("Підрахунок завершений")
#         break
#
#     total_items += 1
#
# print(f"Всього товарів додано: {total_items}")

# Завдання 6
# passw = 1111
# times = 0
#
# while True:
#     user_pass = int(input("Введіть пароль:"))
#     times += 1
#
#     if user_pass == passw:
#         print("Вірний пароль")
#         break
#     if times >= 3:
#         print("Перевищено ліміт спроб:")
#         break
#     print("Пароль не вірний")


