# Так просто?

number = int(input("Please, enter the number : "))
print(number)
s = str(number)
sm = 0
for i in range(len(s)):
    sm += int(s[i])
print(sm)


# Сумма рандомного числа
# from random import random

# number = int(random() * 77777)
# print(number)
#  s = str(number)
# sm = 0
# for i in range(len(s)):
#    sm += int(s[i])
# print(sm)


# Сумма трьох чисел
# number = int(input("Please, enter the number : "))
# print(number)
# s = str(number)
# a = int(s[0])
# b = int(s[1])
# c = int(s[2])
# print(a+b+c)
