# До тех пор пока while не разлучит нас!
b = int(input("Number b: "))
c = 1
a = 0
while a <= 1000:
    a += c
    if a < b:
        print(a)
        continue

    if a > b:
        break

    print("Радостное сообщение!!!")
