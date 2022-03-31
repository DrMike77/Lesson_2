sp1 = []
for element in range(1, 10):
    sp1.append(element)
print(sp1)
print(len(sp1))
for a in range(-1, len(sp1)-3, 2):
    a = a + 1
    sp1[a], sp1[a + 1] = sp1[a + 1], sp1[a]
print(sp1)