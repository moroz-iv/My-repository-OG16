#  Сравним списки?
import random
x = int(input("Введите максимальное значение списка: "))
y = int(input("Введите минимальное значение списка: "))
z = int(input("Введите максимальное количество элементов списка: "))

a1 = [random.randint(y, x) for i1 in range(z)]
print("Значения списка a1: " + "\n" + str(a1))

a2 = [random.randint(y, x) for i2 in range(z)]
print("Значения списка a1: " + "\n" + str(a2))

c = []
for d in a1:
    if d not in a2:
        c.append(d)
print("Уникальные занчения списка a1: " + "\n" + str(c))
c1 = []
for d1 in a2:
    if d1 not in a1:
        c1.append(d1)
print("Уникальные занчения списка a2: " + "\n" + str(c1))


# b = [(x, y) for x in a1 for y in a2]
# b1 = [(x, y) for x in a1 for y in a2 if x not in a2 and y not in a1]

# print(b)
# print(b1)
