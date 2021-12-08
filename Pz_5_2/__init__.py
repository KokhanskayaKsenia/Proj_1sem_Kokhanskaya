#
print("Введите число A")
A = int (input())
print("Введите число B")
B = int (input())
print("Введите число C")
C = int (input())
print("Введите число D")
D = int (input())

def Minmax(X, Y): # функция сортировки
    if X < Y:
        return (X, Y)
    else:
        return (Y, X)

A, B = Minmax(A, B)
C, D = Minmax(C, D)
A, C = Minmax(A, C)
B, D = Minmax(B, D)
print("минимальное число равно ", A, "максимальное число равно ", D)

