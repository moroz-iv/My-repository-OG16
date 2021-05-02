# А что если так?

def funk(a, b):
    if a > b:
        return "Успешно!"
    elif a == b:
        return "Почти!!"
    elif a < b:
        return "Лузер!!!"


print("Результат: " + funk(int(input("Введите первое число: ")), int(input("Введите втрое число: "))))
