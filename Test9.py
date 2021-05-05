# Списки? Списки!
import random
x = int(input("Введите максимальное значение списка: "))
y = int(input("Введите минимальное значение списка: "))
z = int(input("Введите максимальное количество элементов списка: "))

a = [random.randint(y, x) for i in range(z)]

print(a)
