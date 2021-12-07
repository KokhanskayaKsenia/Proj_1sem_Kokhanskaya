print("Введите число N")
N = int (input())
K = 0

def sumDidgits(N): # Вычисляем сумму цифр.
    sum = 0
    while N!=0 :
        sum += N%10
        N = N//10
    return sum

while N!=0:
    N = N-sumDidgits(N)
    K = K+1
print("Операция выполнена ", K, "раз")


