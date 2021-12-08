print("Укажите размер списка N")
N = int (input())
A = list(range(-10, N))
S = 0
M = 0
for i in range(0, N):
    if A[i] <= A[i+1]:
        S+= 1
    else:
        A[i] >= A[i+1]
        M+= 1
print('монотонно убывает ', M, ' раз и монотонно возрастает ', S, 'раз')