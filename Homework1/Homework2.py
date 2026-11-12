#Завдання1
#num1 = float(input("перше число: "))
#num2 = float(input("друге число: "))
#sum = num1 + num2
#average = sum / 2
#print("Сума:", sum)
#print("Середнє:", average)

#Завдання2
#uah=float(input("Сума у грн.:"))
#usd=float(input("Курс доллара:"))
#rate=uah/usd
#print("Загальна сума у $:",rate)

#Завдання3
#price=float(input("Ціна товару:"))
#discount=float(input("Знижка у %:"))
#disc=float(discount*0.01)
#print("Сума знижки:",price*disc)

#Завдання4
walk=3
fast_walk=4.5
run=9
walkt=float(input("Час повільної ходьби у хв.:"))
fast_walkt=float(input("Час швидкої ходьби у.хв.:"))
runt=float(input("Час бігу у хв.:"))
result1=walk*walkt
result2=fast_walk*fast_walkt
result3=run*runt
total=result1+result2+result3
print("Кількість спалених ккал під час повільної хотьби:",result1)
print("Кількість спалених ккал під час швидкої хотьби:",result2)
print("Кількість спалених ккал під час бігу:",result3)
print("Всього спалених ккал:",total)
