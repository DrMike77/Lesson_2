l1, p1, q1 = [], [], []
count = int(input("Введите количество товаров: "))
for _ in range(count):
    l1.append(str(input("Введите название девайса: ")))
    p1.append(int(input("Введите цену девайса: ")))
    q1.append(int(input("Введите количество товаров: ")))
for name, price, quantity in zip(l1, p1, q1):
    print(l1.index(name)+1, {"name": name, "price": price, "quantity": quantity, "meas": "шт"})