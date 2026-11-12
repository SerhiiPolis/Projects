# Завдання 1


# age = int(input("Скільки Вам років?:"))
#
# if age <12:
#     print("Ціна квитка - 80 грн.")
# elif 12 < age < 65:
#     print("Ціна квитка - 200 грн.")
# else:
#     print("Ціна квитка - 120 грн.")
#
# print("Гарного Вам дня !")

# Завдання 3

# month = input("Введіть місяць:")
# day = int(input("Введіть число:"))
#
# if month == "січень" and day == 1:
#     print("Новий рік!")
# elif month == "лютий" and day == 14:
#     print("День св.Валентина")
# elif month == "грудень" and day == 25:
#     print("Різдво")
# elif month == "квітень" and day == 1:
#     print("День сміху")
# else:
#     print("Звичайчий день")

# # Завдання 4
# PRICE1 = 80 #Дитячий квиток
# PRICE2 = 200 #Звичайний квиток
# PRICE3 = 120 # Квиток пенсійний
# age1 = int(input("Скільки Вам років?:"))
#
# total1 = 0
# if age1 <12:
#     total1 += PRICE1
# elif 12 < age1 < 65:
#     total1 += PRICE2
# else:
#     total1+= PRICE3
# print(total1)
#
# age2 = int(input("Скільки Вам років?:"))
#
# total2 = 0
# if age2 <12:
#     total2 += PRICE1
# elif 12 < age2 < 65:
#     total2 += PRICE2
# else:
#     total2+= PRICE3
# print(total2)
#
# age3 = int(input("Скільки Вам років?:"))
#
# total3 = 0
# if age3 <12:
#     total3 += PRICE1
# elif 12 < age3 < 65:
#     total3 += PRICE2
# else:
#     total3+= PRICE3
# print(total3)
#
# print(f"Загальна сума: {total1 + total2 + total3}")
#
# print("Гарного Вам дня !")


# Завдання 5

# product = input("Введіть назву товару: ")
#
# if product == "алкоголь" or product == "тютюн":
#     age = int(input("Введіть ваш вік: "))
#     if age >= 18:
#         print("Дозволено до продажу")
#     else:
#         print("Заборонено до продажу")
# elif product == "ліки":
#     prescription = input("У вас є рецепт від лікаря?")
#     if prescription == "так":
#         print("Дозволено до продажу")
#     else:
#         print("Заборонено до продажу")

# Завдання 6

# is_logged_in = input("Ви увійшли в систему? (так/ні): ")
#
#
# if is_logged_in == "так":
#     cart_is_empty = input("Ваш кошик порожній? (так/ні): ")
#     if cart_is_empty == "ні":
#         total_price = float(input("Введіть вартість замовлення: "))
#         balance = float(input("Введіть баланс: "))
#         if balance >= total_price:
#             print("Замовлення успішно оформлено!")
#         else:
#             print("Недостатньо коштів на рахунку")
#     else:
#         print("Ваш кошик порожній")
# else:
#     print("Будь ласка, увійдіть в систему")

# Завдання 7

# speed = int(input("Введіть Вашу швидкість в км/года:"))
#
# if speed > 90:
#     location = input("Ваше місцезнаходження (місто/траса):")
#     if location == "місто":
#         print("Вас оштрафовано!")
#     else:
#         print("Обережно!")
# elif speed < 20:
#     year = int(input("Скільки років машині?:"))
#     if year > 15:
#         print("Купи нову тачку!")
#     else:
#         print("Завітайте до СТО")
# else:
#     print("Гарної дороги!")


