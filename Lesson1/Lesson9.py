#  Завдання 1

# total = 0
# num = int(input("Введіть число від 1 до 9"))
#
# if num < 1 or num > 9:
#     print("Введіть правильне число!")
# else:
#     for i in range(1,11):
#         total = i * num
#         print(f"{i} * {num} = {total}")

# Завдання 2

# total = 0
# count = 0

# while True:
#     grade = int(input("Введіть оцінку: "))
#     if grade == 0:
#         break
#
#     total += grade
#     count += 1
# if count > 0 :
#     average_grade = total / count
#     print(f"середня оцінка:{average_grade}")
# else :
#     print("")

# Завдання 3


# print("1. сума")
# print("2. різниця")
# print("3. добуток")
# print("4. частка")
# print("5. вихід")
#
# while True:
#     action = int(input("Введіть номер дії:"))
#     if action == 5:
#         print("До побачення!")
#         break
#     if action < 1 or action > 5:
#         print("Не вірна дія!")
#         continue
#     if action == 1:
#         num1 = int(input("Введіть перше число:"))
#         num2 = int(input("Введіть друге число:"))
#         total1 = num1 + num2
#         print(f"Сума = {total1}")
#     elif action == 2:
#         num1 = int(input("Введіть перше число:"))
#         num2 = int(input("Введіть друге число:"))
#         total1 = num1 - num2
#         print(f"Різниця = {total1}")
#     elif action == 3:
#         num1 = int(input("Введіть перше число:"))
#         num2 = int(input("Введіть друге число:"))
#         total1 = num1 * num2
#         print(f"Добуток = {total1}")
#     else:
#         num1 = int(input("Введіть перше число:"))
#         num2 = int(input("Введіть друге число:"))
#         if num2 == 0:
#             print("На 0 ділити не можна!")
#             continue
#         else:
#             total1 = num1 / num2
#             print(f"Частка = {total1}")

# Завдання 4
# i = 1
#
# while i <= 3:
#
#     name = input("Введіть ім'я: ")
#     if name == "admin":
#         print("Це ім'я недоступне")
#         continue
#     else:
#         print(f"Учасник №{i}: {name}")
#         i += 1

#Завдання 5

# import random
# secret_num = random.randint(0, 100)
# times = 0
# while True:
#
#     num = int(input("Введіть число:"))
#     if num < secret_num:
#         print("Замало")
#         times += 1
#     if num > secret_num:
#         print("Забагато")
#         times += 1
#     if num == secret_num:
#         print(f"Ви вгадали за {times} спроб")






