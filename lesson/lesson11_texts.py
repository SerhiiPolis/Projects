# Завдання 1

# text = input("Введіть рядок:")
# symbol = input("Введіть символ:")
#
# count = text.count(symbol)
# print(f"Символ {symbol} зустрічається {count} рази")

# text = input("Введіть рядок:")
# symbol = input("Введіть символ:")
# count = 0
#
# for ch in text:
#     if ch == symbol:
#         count += 1
#
# print(f"Символ {symbol} зустрічається {count} рази")


# Завдання 2

# text = input("Введіть рядок:")
#
# count = len(text)
# print(f"У рядку {count} символів")
#
# if "python" in text:
#      print(f"У рядку є слово python")
# else:
#      print("У рядку відсутнє слово python")
#
# count_szh = text.count("s") + text.count("z") + text.count("h")
# print(f"У рядку {count_szh} шипячих літер")


# Завдання 3

# text = input("Введіть текст: ")
#
# result = text.replace(" ", "-")
# print(f"Змінений текст: {result}")


# Завдання 4


# text = input("Введіть рядок:")
# word = input("Введіть слово:")
#
# count_word = text.count(word)
# print(f"У тексті слово {word} зустрічається {count_word} рази ")

# Завдання 5

# items = input("Введіть ваші речі: ")
# new_items = items.lower()
#
# if "ніж" in new_items or "гроші" in new_items or "отрута" in new_items:
#     print("У вас є речі які заборонено перевозити")
# else:
#     print("Оформлено доставку")

# Завдання 6

# text = input("Введіть рядок:")
# letter = 0
# num = 0
#
# for ch in text:
#     if ch.isdigit():
#         num += 1
#     elif ch.isalpha():
#         letter += 1
#
# print(f"Літер - {letter}")
# print(f"Цифр - {num}")

# Завдання 7


# while True:
#     password = input("Введіть пароль:")
#
#     if len(pas) < 8:
#         print("Пароль повинен буди довшим за 8 символів")
#         continue
#
#     num = 0
#     letter = 0
#
#     for ch in pas:
#         if ch.isdigit():
#             num += 1
#         if ch.isalpha():
#             let += 1
#
#     if num < 1:
#         print("Повинна бути хоча б одна цифра")
#         continue
#
#     if let < 1:
#         print("Повинна бути хоча б одна літера")
#         continue
#
#
#     print(f"Ваш пароль - {pas}")
#     break
