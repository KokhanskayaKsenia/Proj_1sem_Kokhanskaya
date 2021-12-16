#Даны два целых числа: A, B. Проверить истинность высказывания: «Ровно одно из чисел A и B нечетное».
print("Введите значение A, которое целое число")
A = input()
print("Введите значение B, которое целое число")
B = input()
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