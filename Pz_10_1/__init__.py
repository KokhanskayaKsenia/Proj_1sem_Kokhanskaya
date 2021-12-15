# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Элементы в обратном порядке:
# Сумма элементов последней половины:
print("Укажите размер списка N")
N = int (input())
A = list(range(-N, N))
def sumDidgits(N): # Вычисляем сумму цифр.
    sum = 0
    for i in range(N, 2*N):
        sum = sum+int(A[i])
    return sum
S = sumDidgits(N)
A = str(A)
reversed = A [::-1]
Z = str(len(A))
f3 = open('data_3.txt ', 'w')
f3.writelines(A)
f3.close()
f4 = open('data_4.txt ', 'w')
f4.write('Исходные данные: ')
f4.write('\n')
f4.writelines(A)
f4.write('\n')
f4.write('Количество элементов: ')
f4.write(Z)
f4.write('\n')
f4.write('Элементы в обратном порядке')
f4.write('\n')
f4.writelines(reversed)
f4.write('\n')
f4.write('Сумма второй половины элементов равна')
f4.write(str(S))
f4.close()
