print("Вітаємо вас у нашій бібліотеці")
print("Меню бібліотеки:")
print("1. Отримати книжку")
print("2. Повернути книжку")
print("3. Вихід")

while True:
    choise = int(input("Виберіть дію :"))
    name = input("Введіть ім'я:")
    book = input("Введіть назву книжки:")
    if name == "" or book =="":
        print("Введіть корректні дані!")
        continue
    if choise == 3:
        break
    elif choise == 1:
        day = int(input("На скільки днів?:"))
        if day < 0:
            print("Не вірно вказаний термін!")
            continue
        if day > 30:
            print("Максимальний термін - 30 днів!")
            continue
        print(f"Книжку {book} видано читачеві {name} на {day} днів")
    elif choise == 2:
        print(f"Читач {name} повернув книжку {book}")
print("Гарного вам дня")