"""
Task 24
Подготовка к ЕГЭ информатика
https://stepik.org/course/72713/syllabus
"""

# https://stepik.org/lesson/1239193/step/4?unit=1334312
from re import *
s = open('24_08_04.txt').readline()
reg = r'(?:A[0-9BCE-Z]+D)'
res1 = findall(reg, s)
res1 = len(max(res1, key=len))

res2 = findall(reg, s[::-1])  # теперь сначала 'D' а в конце 'A'
res2 = len(max(res2, key=len))
print(max(res1, res2))  # 273

# variant
s = open('24_08_04.txt').readline()
l = m = 0
for r in range(len(s)):
    if s[r] in 'AD':
        if s[l] in 'AD' and s[l] != s[r]:
            m = max(m, r-l+1)  # в случае когда s[l] != s[r]
        l = r  # фиксируем в указателе 'l' символ 'A' or 'D' для последующего поиска уходящего дальше указателя 'r'
print(m)  # 273



# https://stepik.org/lesson/1239193/step/6?unit=1334312
s = open('24_08_06.txt').read()
x=y=z=0
l=res=0
for r in range(len(s)):
    if s[r] in 'ABC':
        l=r+1
        x=y=z=0
        continue
    x+=s[r]=='X'
    z+=s[r]=='Z'
    y+=s[r]=='Y'
    while any([x>5, y>5, z>5]):
        x-=s[l]=='X'
        z-=s[l]=='Z'
        y-=s[l]=='Y'
        l+=1
    if x==y==z==5:
        res=max(res,r-l+1)
print(res)

# variant
s = open('24_08_06.txt').read()
for i in 'ABC':
    s = s.replace(i, ' ')
s = s.split()
s = [i for i in s if all([i.count('X')>4, i.count('Y')>4, i.count('Z')>4])]
res=0
for el in s:
    x = y = z = l = 0
    for r in range(len(el)):
        x+=el[r]=='X'
        z+=el[r]=='Z'
        y+=el[r]=='Y'
        while any([x>5, y>5, z>5]):
            x-=el[l]=='X'
            z-=el[l]=='Z'
            y-=el[l]=='Y'
            l+=1
        if x==y==z==5:
            res=max(res,r-l+1)
print(res)


# https://stepik.org/lesson/1239193/step/7?unit=1334312
s = open('24_08_07.txt').read()
res = c = l = 0
for r in range(3, len(s)):
    c += s[r-3:r+1] == 'SOLO'
    while c > 4:
        c -= s[l:l+4] == 'SOLO'
        l += 1
    if c == 4 and sum(i in s[l:r+1] for i in '0123456789') >= 5:
        res = max(res, r-l+1)
print(res)  # 431


