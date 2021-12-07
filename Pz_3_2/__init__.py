print("Введите число A от 1 до 12")
A = int (input())
if A == 2:
    print("В месяце 28 дней")
else:
    if A < 8:
        if A%2 == 0:
            print("В месяце 30 дней")
        else:
            print("В месяце 31 день")
    else:
        if A%2 == 0:
            print("В месяце 31 день")
        else:
            print("В месяце 30 дней")


