print("Введите число N, которое больше 0")
N = int (input())
if N > 0:
    i = 0
    S = 0
    for i in range(1, N+1):
        S = S+(N+i)**2
        i = i+1
    print("Итог выражения равен ", S)
else:
    print("Не соответствует условию задачи")
