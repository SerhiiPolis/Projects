print("Меню:")
print("1. Вибрати піцу")
print("2. Вихід")

while True:
    choise = int(input("Виберіть дію:"))
    if choise == 2:
        print("До побачення!")
        break
    elif choise == 1:
        pizza = input("Яку піцу бажаєте?:")
        quantity = int(input("Скільки штук?:"))
        print(f"Ви замовили {pizza} , {quantity}шт.")
