MARGARITA = 150
PEPERONI = 180
CHEESE = 200
q_margatita = 0
q_peperoni = 0
q_cheese = 0

print("Меню :")
print("1. Вибрати піцу")
print("2. Вихід")
print("3. Показати все замовлення")

while True:
    choice = int(input("Виберіть дію:"))
    if choice == 2:
        print("До побачення!")
        break

    if choice > 3 or choice < 1:
        print("Виберіть пункт із меню!")
        continue

    if choice == 1:
        print("Наші піци:")
        print("Маргарита – 150 грн")
        print("Пепероні – 180 грн")
        print("Чотири сири – 200 грн")

        pizza = input("Яку піцу бажаєте?:")
        quantity = int(input("Скільки штук?:"))

        print(f"Ви замовили {pizza} , {quantity}шт.")

        if quantity < 0:
            print("Кількість не може бути від'ємною!")
            continue

        if pizza == "Маргарита":
            q_margatita += quantity
        elif pizza == "Пепероні":
            q_peperoni += quantity
        elif pizza == "Чотири сири":
            q_cheese += quantity
        else:
            print("У нас немає такої!")
            continue

    total_quant = q_cheese + q_peperoni + q_margatita
    if total_quant > 15:
        print(f"Не можна замовляти більше 15 шт., ви вже замовили {total_quant} шт.!")
        break

    if choice == 3:
        total_margarita = q_margatita * MARGARITA
        total_peperoni = q_peperoni * PEPERONI
        total_cheese = q_cheese * CHEESE

        print("")
        print("========== ВАШЕ ЗАМОВЛЕННЯ ==========")
        print("")
        print("Піца      Кількість       Вартість")
        print("--------------------------------------")

        if q_margatita > 0:
            print(f"МАРГАРИТА     {q_margatita}             {total_margarita}")
        if q_peperoni > 0:
            print(f"ПЕПЕРОНІ      {q_peperoni}             {total_peperoni}")
        if q_cheese > 0:
            print(f"ЧОТИРИ СИРИ   {q_cheese}             {total_cheese}")

        print("")
        print("--------------------------------------")
        print(
            f"Загальна вартість:          {total_margarita + total_peperoni + total_cheese} грн."
        )
        print("======================================")
        print("Дякуємо за замовлення!")
        break
