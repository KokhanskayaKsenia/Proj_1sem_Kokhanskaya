#Описать функцию Minmax(X, Y), записывающую в переменную X минимальное из значений X и Y,
# а в переменную Y — максимальное из этих значений (X и Y — вещественные параметры,
# являющиеся одновременно входными и выходными). Используя четыре вызова этой функции,
# найти минимальное и максимальное из данных чисел A, B, C,
print("Введите число A")
A = input()
print("Введите число B")
B = input()
print("Введите число C")
C = input()
print("Введите число D")
D = input()
while type(A) != int:  # Обработка исключений 1-го числа
    try:
        A = int(A)
    except ValueError:
        print("Не то ввели!")
        A = input("Введите первое целое число: ")
while type(B) != int:  # Обработка исключений 2-го числа
    try:
        B = int(B)
    except ValueError:
        print("Не то ввели!")
        B = input("Введите второе целое число: ")
while type(C) != int:  # Обработка исключений 3-го числа
    try:
        C = int(C)
    except ValueError:
        print("Не то ввели!")
        C = input("Введите третье целое число: ")
while type(D) != int:  # Обработка исключений 4-го числа
    try:
        D = int(D)
    except ValueError:
        print("Не то ввели!")
        D = input("Введите четвертое целое число: ")

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

