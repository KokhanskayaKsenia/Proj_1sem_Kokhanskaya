#
print("Введите значение A, которое целое число")
A = int (input())
print("Введите значение B, которое целое число")
B = int (input())
if A%2 == 1:
    if B%2 ==1:
        print("Ложь")
    else:
        print("Правда")
else:
    if B%2 == 1:
        print("Правда")
    else:
        print("Ложь")