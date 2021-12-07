print("Укажите размер списка N")
N = int (input())
print("Введите целое число K, удовлетворяющее условию 1<K<N")
K = int (input())
A = list(range(0, N))
S = len(A)
L = K
while L < S:
    print('элемент списка ', A[L], ' под номером ', L )
    L = L+K
