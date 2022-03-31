l1 = list()
p1 = list()
q1 = list()
for i in range(0, 3):
   n = str(input("Введите название девайса:"))
   p = int(input("Введите цену девайса:"))
   q = int(input("Введите количество товаров:"))
   l1.append(n)
   p1.append(p)
   q1.append(q)
cor_1 = (1, {"name": l1[0], "price": p1[0], "quantity": int(q1[0]), "meas": "шт"})
cor_2 = (2, {"name": l1[1], "price": p1[1], "quantity": q1[1], "meas": "шт."})
cor_3 = (3, {"name": l1[2], "price": p1[2], "quantity": q1[2], "meas": "шт."})
print("Название девайсов:", cor_1[1]["name"], cor_2[1]["name"], cor_3[1]["name"])
print("Цена девайсов:", cor_1[1]["price"], cor_2[1]["price"], cor_3[1]["price"])
print("Количество девайсов:", cor_1[1]["quantity"], cor_2[1]["quantity"], cor_3[1]["quantity"])

for name, price, quantity in zip(l1, p1, q1):
    print(1, {"name": name, "price": price, "quantity": quantity, "meas": "шт"})