my_list = [7, 5, 3, 3, 2]
a = int(input("Введите целое число "))
if a > max(my_list):
    my_list.insert(0, a)
elif a < min(my_list):
    my_list.insert(len(my_list), a)
else:
    n = len(my_list)
    for i in range(0, n):
        if a == my_list[i]:
            my_list.insert(i+1, a)
            break
print(my_list)