PILLOW = 0
PILLOW_PRICE = 650
BLANKET = 0
BLANKET_PRICE = 1700
LAMP = 0
LAMP_PRICE = 500
KEY = 0
KEY_PRICE = 60
print("Товари:")
print("подушка – 650 грн")
print("ковдра – 1700 грн")
print("лампа – 500 грн")
print("брелок – 60 грн")
print("Меню дій:")
print("1. Додати товар")
print("2. Видалити товар")
print("3. Очисти кошик")
print("4. показати вміст кошики та суму покупки")
print("5. вихід")

while True:
    action = int(input("Виберіть дію:"))
    if action == 5:
        print("Дякуємо за покупку!")
        break
    if action == 1:
        buy = input("Який товар додати?:")
        if buy == "подушка":
            PILLOW += 1
        elif buy == "ковдра":
            BLANKET += 1
        elif buy == "лампа":
            LAMP += 1
        elif buy == "брелок":
            KEY += 1
        else:
            print("Такого товару не існує!")

    if action == 2:
        buy = input("Який товар видалити?:")
        if buy == "подушка":
            PILLOW -= 1
        elif buy == "ковдра":
            BLANKET -= 1
        elif buy == "лампа":
            LAMP -= 1
        elif buy == "брелок":
            KEY -= 1
        else:
            print("Такого товару не існує!")

    if action == 3:
        PILLOW = 0
        BLANKET = 0
        LAMP = 0
        KEY = 0
        print("Кошик очишено")

    if action == 4:
        total_pillow = PILLOW * PILLOW_PRICE
        total_blanket = BLANKET * BLANKET_PRICE
        total_lamp = LAMP * LAMP_PRICE
        total_key = KEY * KEY_PRICE
        print("У вашому кошику")
        if PILLOW > 0:
            print(f"Подушки - {PILLOW}шт. ")
        if BLANKET > 0:
            print(f"Ковдри - {BLANKET}шт. ")
        if LAMP > 0:
            print(f"Лампи - {LAMP}шт. ")
        if KEY > 0:
            print(f"Брелоки - {KEY}шт. ")
        total_price = total_pillow + total_lamp + total_key + total_blanket
        print(f"На суму {total_price} грн.")

