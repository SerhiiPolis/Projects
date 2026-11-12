#Завдання1
#bank=float(input("Рахунок у банку:"))
#bill=float(input("Сума покупки:"))
#total=bank-bill
#print("Залишок:",total)
from dataclasses import field

#Завдання2
#price=float(input("Ціна чашки кави:"))
#quantity=int(input("Кількість чашок:"))
#total=price*quantity
#print("Сума замовлення:",total)

#Завдання3 (Добавити int)
#width = int(input("Введіть ширину: "))
#height = int(input("Введіть висоту: "))
#area = width * height
#print("Площа дорівнює:", area)

#Завдання4
bill1=float(input("Сумма рахунку:"))
guests=int(input("Кількість гостей:"))
tips=float(input("Сума чайових у %:"))
tips2=float(tips*0.01)
tips3=bill1*tips2
bill2=bill1+tips3
print("Чайові:",tips3)
print("Загальна сума:",bill1+tips3)
print("З кожного по:",bill2/guests)

#Завдання5
#distance=float(input("Відстань:"))
#fuel=float(input("Витрата пального:"))
#price=float(input("Ціна за 1л:"))
#print("Кількість палива",distance*fuel/100)
#num=float(distance*fuel/100)
#print("Ціна палива",price*num)

