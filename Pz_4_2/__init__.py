
print("Введите число N, которое больше 1")
N = int (input())
if N>1:
    K = 0
    while 3**K < N:
        K = K+1
    print("Наибольшее целое число равно ", K-1)
else:
    print("Не соответствует условию задачи")