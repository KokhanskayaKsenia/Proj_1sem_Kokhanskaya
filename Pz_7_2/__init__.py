#Дана строка, содержащая полное имя файла.
# Выделить из этой строки название последнего каталога (без символов «\»).
# Если файл содержится в корневом каталоге, то вывести символ «\ ».
s = r'D:\Users\SuperL\Desktop\Ксения\отчеты\огг.txt'
S = s[3:]
l = len(S)
d = 0
reversed = S [::-1]
for el in reversed:
    while d<1:
        d += 1
        if '\\' in reversed:
            for el in reversed:
                if el == '\\':
                    break
                print(el, end = '')
        else:
            print('\\ - имя каталога')








