Seasons = {1: "Winter", 2: "Spring", 3: "Summer", 4: "Autumn"}
a = int(input("Введите номер месяца"))
if a < 1 or a > 12:
        print("Вы ввели неправильное число :(")
elif a < 3 or a > 11:
        print(Seasons[1])
elif a > 2 and a < 6:
        print(Seasons[2])
elif a > 5 and a < 9:
        print(Seasons[3])
elif a > 8 and a < 12:
        print(Seasons[4])