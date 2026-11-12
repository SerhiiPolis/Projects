# Завдання 1

#Користувач вводить змінну radiec
#radius = float(input("Введіть радіус: "))

# Призначення значення змінній pi
#pi = 3.1415

# Розрахунок значення area за допомогою функцій * та **
#area =  radius * pi ** 2

# Виведення результату с двома знаками після коми
#print(f"Площа кола: {area:.2f}")

# Завдання 2

#budget = float(input("Введіть ваш бюджет:"))
#cup_price = float(input("Введіть ціну однієї чашки:"))

#print("Можна купити:", budget // cup_price)

# Завдання 3

#lenght_in_meters = float(input("Довжина в метрах:"))
#foot = float(lenght_in_meters * 3.2808399)
#yard = float(lenght_in_meters * 1.0936133)

#print(f"Довжина у футах: {foot:.2f}")
#print(f"Довжина у ярдах: {yard:.2f}")

# Завдання 4

#budget = float(input("Введіть ваш бюджет:"))
#cup_price = float(input("Введіть ціну однієї чашки:"))

#print("Можна купити:", budget // cup_price)
#print("Ваша решта:", budget % cup_price)

# Завдання 5

#minutes = int(input("Введіть кількість хвилин:"))
#hours = minutes // 60
#rem_minutes = minutes % 60

#print("Годин:",hours)
#print("Хвилин:",rem_minutes)

# Завдання 6

#apples = int(input("Введіть кількість яблук:"))
#milk = float(input("Введіть кількість молока (л):"))

#apples_per_cake = apples // 4
#milk_per_cake = milk // 1.2
#cake = int(min(apples_per_cake, milk_per_cake))

#print("Можна спекти пирогів:",cake)
#print("Залишиться яблук:", apples % 4)
#print(f"Залишиться молока: {milk - cake * 1.2:.1f}")

# Завдання 7

#sum = float(input("Сумма вкладу в грн.:"))
#year_percent = float(input("Відсоток ставки:"))
#percent = year_percent * 0.01

#income_1_year = sum * percent + sum
#print(f"Сума вкладу через 1 рік в грн.: {income_1_year:.1f}")

#income_2_year = income_1_year * percent + income_1_year
#print(f"Сума вкладу через 2 роки в грн.: {income_2_year:.1f}")

#income_3_year = income_2_year * percent + income_2_year
#print(f"Сума вкладу через 3 роки в грн.: {income_3_year:.1f}")

#income_4_year = income_3_year * percent + income_3_year
#print(f"Сума вкладу через 4 роки в грн.: {income_4_year:.1f}")

#income_5_year = income_4_year * percent + income_4_year
#print(f"Сума вкладу через 5 років в грн.: {income_5_year:.1f}")

# Завдання 8

#all_days = int(input("Кількість днів:"))
#year = all_days // 365
#rest_days = all_days % 365
#weeks = rest_days // 7
#days = rest_days % 7

#print("Років:", year)
#print("Тижнів:", weeks)
#print("Днів:", days)


print(rest)