# Так он високосный?
year = int(input("Please, enter the year : "))


def x(y):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return "It's a leap year!"
    else:
        return "This year is not leap year!"


print(x(year))


# year = int(input("Please, enter the year : "))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#    print("It's a leap year!")
# else:
#    print("This year is not leap year!")


# import calendar
# month = int(input("Please, enter the month : "))
# calendar.setfirstweekday(calendar.sunday)
# my cal = calendar.month(year, month)
# my cal = calendar.calendar(year)
# print(my cal)
