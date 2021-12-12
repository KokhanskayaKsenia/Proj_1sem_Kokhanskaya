#Дана строка, содержащая полное имя файла.
# Выделить из этой строки название последнего каталога (без символов «\»).
# Если файл содержится в корневом каталоге, то вывести символ «\ ».
s = r'D:\Users\SuperL\Desktop\Ксения\Отчеты\огг.txt'
S = s[3:]
l = len(S)
d = 0
x = 0
reversed = S [::-1]
for el in reversed:
    while d<1:
        d += 1
        if '\\' in reversed:
            for el in reversed:
                x += 1
                if el == '\\':
                    reversed = reversed[x:]
                    break
            x = 0
            for el in reversed:
                if el == '\\':
                    break
                x += 1
            reversed = reversed[:x]
            S = reversed[::-1]
            print("Последний каталог:", S)

        else:
            print('\\ - имя каталога')








