print("Укажите размер списка N")
N = int (input())
A = list(range(0, N))
print('Изначальный список ', A)
for i in range(N-1, 0, -1):
    A[i] = A[i-1]
A[0] = 0
print('Модернизированный список ', A)