MARGARITA = 150
PEPERONI = 180
CHEESE = 200

print("Меню :")
print("1. Вибрати піцу")
print("2. Вихід")

while True:
    choise = int(input("Виберіть дію:"))
    if choise == 2:
        print("До побачення!")
        break
    elif choise == 1:
        print("Наші піци:")
        print("Маргарита – 150 грн")
        print("Пепероні – 180 грн")
        print("Чотири сири – 200 грн")
        pizza = input("Яку піцу бажаєте?:")
        if pizza == "Маргарита" or pizza == "Пепероні" or pizza == "Чотири сири":
            quantity = int(input("Скільки штук?:"))
        else:
            print("У нас немає такої!")
            continue
        print(f"Ви замовили {pizza} , {quantity}шт.")
