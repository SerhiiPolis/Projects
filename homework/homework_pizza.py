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
    choise = int(input("Виберіть дію:"))
    if choise == 2:
        print("До побачення!")
        break
    if choise > 3 or choise < 1:
        print("Виберіть пункт із меню!")
        continue
    if choise == 1:
        print("Наші піци:")
        print("Маргарита – 150 грн")
        print("Пепероні – 180 грн")
        print("Чотири сири – 200 грн")
        pizza = input("Яку піцу бажаєте?:")
        quantity = int(input("Скільки штук?:"))
        if quantity < 0:
            print("Кількість не може бути від'ємною!")
            continue
        if pizza == "Маргарита":
            q_margatita += quantity
            continue
        elif pizza == "Пепероні":
            q_peperoni += quantity
            continue
        if pizza == "Чотири сири":
            q_cheese += quantity
            continue
        else:
            print("У нас немає такої!")
            continue
    print(f"Ви замовили {pizza} , {quantity}шт.")
    if choise == 3:
        total_quant = q_cheese + q_peperoni + q_margatita
        if total_quant > 15:
            print("НЕ ЛУСНЕШЬ?! Не можна замовляти більше 15 шт.!")
            break
        total1 = q_margatita * MARGARITA
        total2 = q_peperoni * PEPERONI
        total3 = q_cheese * CHEESE
        print("")
        print("========== ВАШЕ ЗАМОВЛЕННЯ ==========")
        print("")
        print("Піца      Кількість       Вартість")
        print("--------------------------------------")
        if q_margatita > 0:
            print(f"МАРГАРИТА     {q_margatita}             {total1}")
        if q_peperoni > 0:
            print(f"ПЕПЕРОНІ      {q_peperoni}             {total2}")
        if q_cheese > 0:
            print(f"ЧОТИРИ СИРИ   {q_cheese}             {total3}")
        print("")
        print("--------------------------------------")
        print(f"Загальна вартість:          {total1 + total2 + total3} грн.")
        print("======================================")
        print("Дякуємо за замовлення!")
        break
