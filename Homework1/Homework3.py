# Завдання 1
# Користувач вводить змінну у кг.
#clay = float(input("Введіть масу глини (кг): "))

# Перевод з кг. в грами
#clay *= 1000

# Задаємо значення кількості грам на одну фігуру
#clay_per_figure = 130

# Розраховуємо максимальну кількість фігурок
#figures = clay // clay_per_figure

# Виводимо на єкран значення figures
#print(f"Можна зробити: {figures} фігурок")

# Завдання 2

#catch1 = int(input("Скільки зловив 1-й рибалка:"))
#catch2 = int(input("Скільки зловив 2-й рибалка:"))
#catch3 = int(input("Скільки зловив 3-й рибалка:"))

#all_catch = catch1 + catch2 + catch3
#average = int(all_catch / 3)
#max_catch = max(catch1, catch2, catch3)

#print("В середньому риб на одного рибалку:", average)
#print("Масимальний улов:", max_catch)

# Завдання 3

#budget = float(input("Введіть Ваш бюджет у грн.:"))

#simple_place = int(budget // 150)
#vip_place = int(budget // 250)

#print("Кількість людей на звичайні місця:",simple_place)
#print("Кількість людей на VIP місця",vip_place)

# Завдання 4

sum = int(input("Введіть суму в грн.:"))

par500 = sum // 500
rest_sum = sum % 500

par200 = rest_sum // 200
rest_sum2 = rest_sum % 200

par100 = rest_sum2 // 100
rest = rest_sum2 % 100

print("Купюри по 500:",par500)
print("Купюри по 200:",par200)
print("Купюри по 100:",par100)
print("Залишок:",rest)