f = open('py_chel2.txt', 'r') # в файле текс из соурса страницы
s = list(f.readlines())

z = []
for string in s:
    for ch in string:
        if string.count(ch) < 2:
            z.append(ch)

print(s[3])
print(s[3].count('^'))



x=[]
for ch in z:
    if z.count(ch) < 2:
        x.append(ch)

print(''.join(x))