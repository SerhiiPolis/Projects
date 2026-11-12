# Завдання 1

# while True:
#     mark = int(input("Яка Ваша оцінка?: "))
#
#     if 1 <= mark <= 5:
#         break
#
#     print("Введіть правильну оцінку!")
#
# if mark == 1:
#     print("Дуже погано")
# elif mark == 2:
#     print("Погано")
# elif mark == 3:
#     print("Задовільно")
# elif mark == 4:
#     print("Добре")
# else:
#     print("Чудово")

# Завдання 2

# yes = 0
# no = 0
#
# while True:
#     wotes = input("Чи потрібні нові дитячі садочки?(так/ні)")
#     if wotes == "так":
#         yes += 1
#     if wotes == "ні":
#         no += 1
#     if wotes == "стоп":
#         print(f"Голоси ЗА - {yes} , ПРОТИ - {no} ")
#         if yes > no:
#             print(f"Більше голосів ЗА - {yes}!!!")
#         else:
#             print(f"Більше голосів ПРОТИ - {no}")
#         break


# Завдання 3

# print("Введіть число (0 для виходу):")
# while True:
#     num = int(input("Ваше число: "))
#     if num == 0:
#         print("Вихід з програми.")
#         break
#     print(f"Ви ввели: {num}")
