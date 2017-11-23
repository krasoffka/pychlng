f = open('py_chel2.txt', 'r') # в файле текс из соурса страницы
s = list(f.readlines())

z = []
for string in s:
    for num, val in enumerate(string):
        if num > 2 and num + 3 < len(string) and val.islower()\
                and string[num - 1].isupper() and string[num + 1].isupper() \
                and string[num - 2].isupper() and string[num + 2].isupper() \
                and string[num - 3].isupper() and string[num + 3].isupper()\
                and string[num + 1] == string[num + 2] == string[num + 3]:
            print(string[num - 3: num + 4])




