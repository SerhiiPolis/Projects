print("Вітаємо вас у нашій бібліотеці")
print("Меню бібліотеки:")
print("1. Отримати книжку")
print("2. Повернути книжку")
print("0. Вихід")

while True:
    choise = int(input("Виберіть дію :"))
    name = input("Введіть ім'я:")
    book = input("Введіть назву книжки:")
    if choise == 0:
        break
    elif choise == 1:
        day = int(input("На скільки днів?:"))
        print(f"Книжку {book} видано читачеві {name} на {day} днів")
    elif choise == 2:
        print(f"Читач {name} повернув книжку {book}")
print("Гарного вам дня")