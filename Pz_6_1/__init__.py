#Дан список A размера N и целое число K (1 < K < N).
# Вывести элементы список с порядковыми номерами, кратными K: AK, A2*K, A3*K,... . Условный оператор не использовать.
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
