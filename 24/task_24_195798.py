""""""
"""
Task 24
ЕГЭ информатика 2025. Полный курс
https://stepik.org/course/195798
"""


""" 27.2 Практика (ур. базовый) """
# https://stepik.org/lesson/1229626/step/1?unit=1243178
from re import *
reg = r'(?:[CDF][AU])+'
with open('add/course_195798/27.2_Задание_1.txt') as fl:
    s = fl.read()
    res = findall(reg, s)
    if res:
        print(len(max(res, key=len)) // 2)  # 173

# через цикл
with open('add/course_195798/27.2_Задание_1.txt') as fl:
    s = fl.read()
    Mx = 0
    cnt = 0
    i = 0
    while i <= len(s) - 2:
        if all([s[i] in 'CDF', s[i+1] in 'AU']):
            cnt += 1
            Mx = max(Mx, cnt)
            i += 2
        else:
            cnt = 0
            i += 1
    print(Mx)



# https://stepik.org/lesson/1229626/step/2?unit=1243178
from re import *
reg = r'(?:CFE|FCE)+'
with open('add/course_195798/27.2_Задание_2.txt') as fl:
    s = fl.read()
    res = findall(reg, s)
    if res:
        print(len(max(res, key=len)) // 3)  # 103

# через цикл 1)
with open('add/course_195798/27.2_Задание_2.txt') as fl:
    s = fl.read()
    s = s.replace('CFE', '*').replace('FCE', '*')
    Mx = 0
    cnt = 0
    for i in range(len(s)):
        if s[i] == '*':
            cnt += 1
            Mx = max(Mx, cnt)
        else:
            cnt = 0
print(Mx)  # 103

# через цикл 2)
with open('add/course_195798/27.2_Задание_2.txt') as fl:
    s = fl.read()
    Mx = 0
    cnt = 0
    i = 0
    while i <= len(s) - 3:
        if any([s[i:i+3] == 'CFE', s[i:i+3] == 'FCE']):
            cnt += 1
            Mx = max(Mx, cnt)
            i += 3
        else:
            cnt = 0
            i += 1
    print(Mx)  # 103



# https://stepik.org/lesson/1229626/step/3?unit=1243178
from re import *
reg = r'(?:[24][135])+'
with open('add/course_195798/27.2_Задание_3.txt') as fl:
    s = fl.read()
    res = findall(reg, s)
    if res:
        print(len(max(res, key=len)) // 2)  # 10


with open('add/course_195798/27.2_Задание_3.txt') as fl:
    s = fl.read()
    i = 0
    Mx = 0
    cnt = 0
    while i <= len(s) - 2:
        if s[i] in '24' and s[i + 1] in '135':
            cnt += 1
            i += 2
            Mx = max(Mx, cnt)
        else:
            cnt = 0
            i += 1
print(Mx)  # 10


# https://stepik.org/lesson/1229626/step/4?unit=1243178
with open('add/course_195798/27.2_Задание_4.txt') as fl:
    s = fl.read()
    cnt = 0
    for i in range(len(s) - 9):
        cnt += s[i:i+9] == s[i:i+9][::-1]
print(cnt)  # 202820


# https://stepik.org/lesson/1229626/step/5?unit=1243178
with open('add/course_195798/27.2_Задание_5.txt') as fl:
    s = fl.read().replace('DD', 'D D')
    mx = max(len(i) for i in s.split() if 'FE' in i)
    print(mx)  # 2486


# https://stepik.org/lesson/1229626/step/6?unit=1243178
from re import *
reg = r'(?:[12]{2}[AB])+'
with open('add/course_195798/27.2_Задание_6.txt') as fl:
    s = fl.read()
    res = sorted(findall(reg, s), key=len)
    pass
print(len(res[-1]) // 3)  # 67

with open('add/course_195798/27.2_Задание_6.txt') as fl:
    s = fl.read()
    Mx = 0
    i = 0
    cnt = 0
    while i <= len(s) - 3:
        if all([s[i] in '12', s[i+1] in '12', s[i+2] in 'AB',]):
            cnt += 1
            Mx = max(Mx, cnt)
            i += 3
        else:
            cnt = 0
            i += 1
print(Mx)  # 67


# https://stepik.org/lesson/1229626/step/7?unit=1243178
from re import *
reg = r'(?:A.A|C.C)+'
with open('add/course_195798/27.2_Задание_7.txt') as fl:
    s = fl.read()
    res = sorted(findall(reg, s), key=len)
    pass
print(len(res[-1]) // 3)  # 17

with open('add/course_195798/27.2_Задание_7.txt') as fl:
    s = fl.read()
    Mx = 0
    i = 0
    cnt = 0
    while i <= len(s) - 3:
        if any([s[i] + s[i+2] == 'AA', s[i] + s[i+2] == 'CC']):
            cnt += 1
            Mx = max(Mx, cnt)
            i += 3
        else:
            cnt = 0
            i += 1
print(Mx)  # 17


# https://stepik.org/lesson/1229626/step/8?unit=1243178
with open('add/course_195798/27.2_Задание_8.txt') as fl:
    s = fl.read()
    m = 0
    for l in range(len(s)):
        for r in range(l + m, len(s) + 1):
            st = s[l:r]
            if st.count('.') <= 5:
                m = max(m, len(st))  # считаем пока меньше 6 точек
            else:
                break
print(m)  # 550


# https://stepik.org/lesson/1229626/step/9?unit=1243178
with open('add/course_195798/27.2_Задание_9.txt') as fl:
    s = fl.read()
print(s.count('NEWYEAR'))  # 6



# https://stepik.org/lesson/1229626/step/10?unit=1243178
from re import *
reg = r'X*Y*Z*'
with open('add/course_195798/27.2_Задание_10.txt') as fl:
    s = fl.read()
    res = sorted(findall(reg, s), key=len)
print(len(res[-1]))  # 15

with open('add/course_195798/27.2_Задание_10.txt') as fl:
    s = fl.read()
    k = 1
    Mx = 0
    for i in range(len(s) - 1):
        if s[i] <= s[i + 1]:
            k += 1
            Mx = max(Mx, k)
        else:
            k = 1
    print(Mx)  # 15


# https://stepik.org/lesson/1229626/step/11?unit=1243178
with open('add/course_195798/27.2_Задание_11.txt') as fl:
    s = fl.read().replace('QW', 'Q W').split()
    res = max(s, key=len)
    print(len(res))  # 5267



# https://stepik.org/lesson/1229626/step/12?unit=1243178
from re import *
reg = r'[02468]+|[13579]+'
with open('add/course_195798/27.2_Задание_12.txt') as fl:
    s = fl.read()
    res = findall(reg, s)
    res = max(res, key=len)
print(len(res))  # 18

with open('add/course_195798/27.2_Задание_12.txt') as fl:
    s = fl.read()
    k = 1
    Mx = 0
    for i in range(len(s) - 1):
        if int(s[i]) % 2 == int(s[i + 1]) % 2:
            k += 1
            Mx = max(Mx, k)
        else:
            k = 1
    print(Mx)  # 18



""" 27.3 Практика (ур. усложненный) """

# https://stepik.org/lesson/1229627/step/1?unit=1243179
with open('add/course_195798/27.3_Задание_1.txt') as fl:
    s = fl.read()
    s = s.replace('XYZY', 'XY ZY')  # избавляемся от плохой комбинации, но сохраняем ее хорошие половинки
    Mx = 0
    for l in range(len(s) - 2):
        for r in range(l, len(s) + 2, 2):
            row = s[l:r+2]
            if all([row[-2] in 'XZ', row[-1] == 'Y']):
                Mx = max(Mx, len(row))
            else:
                break
print(Mx // 2)  # 8

# Быстрее (за 1 проход)
with open('add/course_195798/27.3_Задание_1.txt') as fl:
    s = fl.read()
    s = s.replace('XYZY', 'XY ZY')  # избавляемся от плохой комбинации, но сохраняем ее хорошие половинки
    Mx = 0
    cnt = 0
    i = 0
    while i < len(s) - 1:
        if s[i] in 'XZ' and s[i + 1] in 'Y':
            cnt += 1
            Mx = max(Mx, cnt)
            i += 2
        else:
            cnt = 0
            i += 1
print(Mx)  # 8



# https://stepik.org/lesson/1229627/step/2?unit=1243179
from collections import Counter
d = []
with open('add/course_195798/27.3_Задание_2.txt') as fl:
    s = fl.read()
    i = 0
    while i <= len(s) - 5:
        if s[i:i+2] + s[i+3:i+5] == 'CBBC':
            d.append(s[i+2])
        i += 1
m = sorted(Counter(d).items(), key=lambda x: (-x[1]))[0][0]
print(m, d.count(m), sep='')  # C5760

# variant
alf = 'ABCDEF'
d = [0] * len(alf)
with open('add/course_195798/27.3_Задание_2.txt') as fl:
    s = fl.read()
    for i in range(len(s) - 5):
        if s[i:i+2] + s[i+3:i+5] == 'CBBC':
            d[alf.index(s[i+2])] += 1
print(alf[d.index(max(d))], max(d), sep='')  # C5760



# https://stepik.org/lesson/1229627/step/3?unit=1243179
with open('add/course_195798/27.3_Задание_3.txt') as fl:
    s = fl.read().strip()
    m = s[0]
    res = ''
    for i in range(len(s) - 1):
        if ord(s[i]) > ord(s[i+1]):
            m += s[i+1]
            res = max(res, m, key=len)
        else:
            m = s[i+1]
print(res)  # zrqjWRC1


# https://stepik.org/lesson/1229627/step/4?unit=1243179
from collections import Counter
with open('add/course_195798/27.3_Задание_4.txt') as fl:
    s = fl.read()
    d = []
    i = 0
    while i < len(s) - 2:
        if s[i] + s[i+2] == 'AC':
            d.append(s[i+1])
            pass
        i += 1
res = sorted(Counter(d).items(), key=lambda x: (-x[1], ord(x[0])))[0]
print(res[0], res[1], sep='')  # T72


# https://stepik.org/lesson/1229627/step/5?unit=1243179
from re import *
reg = r'D+'
with open('add/course_195798/27.3_Задание_5.txt') as fl:
    s = fl.read()
    res = findall(reg, s)
print(len(min(res, key=len)))  # 5


# https://stepik.org/lesson/1229627/step/6?unit=1243179
with open('add/course_195798/27.3_Задание_6.txt') as fl:
    s = fl.read()
    cnt = 0
    for i in range(len(s) // 2):
        cnt += s[i] == s[-(i + 1)]
    print(cnt)  # 19100


# https://stepik.org/lesson/1229627/step/7?unit=1243179
with open('add/course_195798/27.3_Задание_7.txt') as fl:
    s = fl.read()
    # s = '5566123998877111'
    cnt = 1
    Mx = 0
    for i in range(len(s) - 1):
        if sum(map(int, s[i:i+2])) >= 10:
            cnt += 1
            Mx = max(Mx, cnt)
        else:
            cnt = 1
print(Mx)  # 26


# https://stepik.org/lesson/1229627/step/8?unit=1243179
with open('add/course_195798/27.3_Задание_8.txt') as fl:
    s = fl.read()
    s = s.replace('A', 'A A').replace('F', 'F F')
    s = s.split()
    Mx = 100 ** 100
    for i in s:
        if all([i[0] == 'A', i[-1] == 'F', len(i) > 2]):
            Mx = min(Mx, len(i))
    print(Mx)  # 7

# variant
with open('add/course_195798/27.3_Задание_8.txt') as fl:
    s = fl.read()
    Mx = 100**100
    idx = [i for i in range(len(s)) if s[i] == 'A']
    for i in idx:
        f = s.index('F', i)
        if f - i > 1:
            Mx = min(Mx, f - i - 1)
    print(Mx + 2)  # 7



# https://stepik.org/lesson/1229627/step/9?unit=1243179
from re import *
reg = r'\d[A-Z]{5}\d'
with open('add/course_195798/27.3_Задание_9.txt') as fl:
    s = fl.read()
    res = findall(reg, s)
print(len(res))  # 61

# variant
with open('add/course_195798/27.3_Задание_9.txt') as fl:
    s = fl.read()
    for i in '0123456789':
        s = s.replace(i, ' ')
    s = s.split()
    res = [1 for i in s if len(i) == 5]
    print(len(res))  # 61


# https://stepik.org/lesson/1229627/step/10?unit=1243179
from re import *
reg = r'(?<!J)BOSS(?!J)'  # что бы захватились BOSSBOSS
with open('add/course_195798/27.3_Задание_10.txt') as fl:
    s = fl.read()
    res = findall(reg, s)
print(len(res))  # 2198

# variant
with open('add/course_195798/27.3_Задание_10.txt') as fl:
    s = fl.read()
    k = 0
    r2 = []
    for i in range(len(s) - 5):
        if s[i] != 'J' and s[i + 5] != 'J' and s[i+1:i + 5] == 'BOSS':
            k += 1
            r2 += [s[i:i+6]]
print(k)  # 2198





""" 27.5 Закрепление (ч. 2) """
# https://stepik.org/lesson/1229629/step/14?unit=1243181
from collections import Counter
s = ''
N = 100**100
with open('add/course_195798/repeat/27.5_Задание_24.txt') as fl:
    for r in fl.readlines():
        n = Counter(r)['N']
        if n < N:
            N = n
            s = r
res = Counter(s).items()
res = sorted(res, key=lambda x: (-x[1], -ord(x[0])))
print(res[0][0])  # Y




""" 28.5 Закрепление (ч. 2) """
# https://stepik.org/lesson/1229674/step/14?unit=1243226
with open('add/course_195798/repeat/28.4_Задание_24.txt') as fl:
    s = fl.read()
    # s = '123' + 'T' * 100 + '2T' + 'T' * 99 + '123'
    m = 100
    Mx = 0
    for l in range(len(s)):
        for r in range(l + m, len(s) + 1):
            row = s[l:r]
            if row.count('T') > 100:
                break
            if row.count('T') == 100:
                Mx = max(Mx, len(row))
                m = Mx
    print(Mx)



