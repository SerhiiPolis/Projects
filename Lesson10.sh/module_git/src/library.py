print("Вітаємо вас у нашій бібліотеці")
print("Меню бібліотеки:")
print("1. Отримати книжку")
print("0. Вихід")

while True:
    choise = int(input("Виберіть дію :"))
    if choise == 0:
        break
    elif choise == 1:
        name = input("Введіть ім'я:")
        book = input("Введіть назву книжки:")

print("Гарного вам дня")