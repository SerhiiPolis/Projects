# Завдання 1

# text = input("Введіть рядок англійською мовою: ")
#
# count = 0
# for letter in text:
#     if letter in "aeiou":
#         count += 1
#
# print(f"Кількість голосних літер: {count}")

# Поясніть будь ласка, чому це працює?
# Чому рахується кожна літера окремо, а не слово "aeiou"?
# Дуже дякую


# Завдання 2

# sentence = input("Введіть речення:")
#
# while True:
#     change_word = input("Введіть слово яке треба змінити:")
#     if change_word == "EXIT":
#         print("До побачення!")
#         break
#
#     if change_word in sentence:
#         sentence = sentence.replace(change_word, change_word.upper())
#         print(sentence)

# Завдання 3

count = 0

text = input("Введіть текст:")

for sign in text:
    if sign in "!.?":
        count += 1

print(f"У тексті {count} речень")
