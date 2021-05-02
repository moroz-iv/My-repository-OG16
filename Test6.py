# Калькулятор + функция

def xyz(c, a, b):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        return round(a / b)
    else:
        return "Выбрана неверная операция"


x = input("Что делаем? (+,-,*,/): ")
y = int(input("Введи первое число: "))
z = int(input("Введи второе число: "))


print("Результат: " + str(xyz(x, y, z)))
