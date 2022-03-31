t = str(input("Введите строку из слов с пробелами"))
l = t.split(' ')
z = list(l)
for i in range(1,len(z)):
    n = len(z[i])
    s = z[i]
    print(i, s[0:10])
