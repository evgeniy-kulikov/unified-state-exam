"""
Task 24
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248
"""

""" 7.37 ЕГЭ Тренировка 24 """
from re import *
reg = r'C+'
with open('add/course_57248/k7-0.txt') as fl:
    ls = findall(reg, fl.read())
    if ls: print(len(max(ls, key=len)))
    else: print(0)  # 0
# В файле k7-0.txt нет символов  C


# https://stepik.org/lesson/511852/step/2?auth=login&unit=504044
from re import *
reg = r'C+'
with open('add/course_57248/k7-5.txt') as fl:
    res = findall(reg, fl.read())
    print(len(max(res, key=len)))  # 2



# https://stepik.org/lesson/511852/step/3?auth=login&unit=504044
# Вариант (один проход по строке)
with open('add/course_57248/k7-25.txt') as fl:
    s = fl.read()
    res = c = fl = 0
    for i in range(len(s)):
        if s[i] == 'C':  # событие
            if not fl:
                fl = 1  # включаем режим подсчета
            if fl:
                c += 1
                res = max(res, c)
        else:
            c = fl = 0  # отключаем режим подсчета + сброс счётчика
    print(res)  # 5


# https://stepik.org/lesson/511852/step/4?auth=login&unit=504044
from re import *
reg = r'[ABDE]+'
with open('add/course_57248/k7a-5.txt') as fl:
    res = findall(reg, fl.read())
    print(len(max(res, key=len)))  # 19

# Вариант
with open('add/course_57248/k7a-5.txt') as fl:
    s = fl.read()
    res = c = fl = 0
    for i in range(len(s)):
        if s[i] in 'ABDE':
            if not fl:
                fl = 1
            if fl:
                c += 1
                res = max(res, c)
        else:
            c = fl = 0
    print(res)  # 19


# https://stepik.org/lesson/511852/step/5?auth=login&unit=504044
from re import *
reg = r'(DBAC)+DBA|DB|D'  # последний фрагмент DBAC может быть неполным
c = 0
with open('add/course_57248/k7b-2.txt') as fl:
    res = finditer(reg, fl.read())
    for i in res:
        s = i.group()
        if len(s) >= 4: # reg ловит отдельные DBA  DB  D
            c = max(c, len(s))
print(c)  # 95

# https://stepik.org/lesson/511852/step/5?auth=login&unit=504044
# Вариант
res = fl = c = 0
with open('add/course_57248/k7b-2.txt') as data:
    st =  data.read()
    st = st.replace('DBAC', '*') # для легкости поиска
    for i in range(len(st) - 3):
        if st[i] == '*':  # начало поиска
            fl = 1  # режим поиска
            if fl:
                c += 4
                res = max(res, c)
        else:
            if fl:  # добавление остатка (при наличии)
                res += sum([st[i] == 'D', st[i:i+2] == 'DB', st[i:i+3] == 'DBA'])
            fl = c = 0  # сброс режима поиска
print(res)


# https://stepik.org/lesson/511852/step/6?auth=login&unit=504044
def f(a,b,c):
    if a in 'BCD':
        if b in 'BDE' and b != a:
            if c in 'BCE' and c != b:
                return 1
    return 0

cnt = 0
with open('add/course_57248/k7c-1.txt') as data:
    st =  data.read()
    for i in range(len(st) - 2):
        a,b,c = st[i:i+3]
        cnt += f(a,b,c)
print(cnt) # 1280



# https://stepik.org/lesson/511852/step/7?auth=login&unit=504044
from re import *
reg = r'C+'
res = 0
with open('add/course_57248/k7-m1.txt') as data:
    st =  data.read()
    c = findall(reg, st)
    if c:
        res = min(c, key=len)
print(len(res), len(c), len(st)) # 5 6 126


# https://stepik.org/lesson/511852/step/8?auth=login&unit=504044
cnt = idx = 0
with open('add/course_57248/k7-m21.txt') as data:
# with open('add/course_57248/test.txt') as data:
    st =  data.read()
    for i in range(len(st) - 2):
        a,b,c = st[i:i+3]
        if a < b < c:
            cnt += 1
            idx = i
print(cnt, idx)


# https://stepik.org/lesson/511852/step/9?auth=login&unit=504044
res = 0
cnt = 1
with open('add/course_57248/24-1.txt') as data:
    d = data.read()
    for i in range(len(d) - 1):
        if d[i] < d[i+1]:
            cnt += 1
            res = max(res, cnt)
        else:
            cnt = 1
print(res)  # 7



# https://stepik.org/lesson/511852/step/10?auth=login&unit=504044
cnt = 0
with open('add/course_57248/24-s1.txt') as data:
    ls = data.readlines()
    for d in ls:
        cnt += d.count('YZ') > 1
print(cnt)  # 433


# https://stepik.org/lesson/511852/step/11?auth=login&unit=504044
# расстояние между первым и последним одинаковыми символами в строке
# (внутренние одинаковые (если они есть) считаются вместе со всеми другими разными символами)
res = 0
with open('add/course_57248/24-164.txt') as data:
    for d in data:
        if d.count('E') < 20:
            for a in set(d):
                if d.count(a) > 1:
                    res = max(res, d.rfind(a) - d.find(a))
print(res)  # 974

# расстояние между двумя последовательными одинаковыми символами в строке (не только для двух, но и более)
# из-за другой логики оценки условия задачи, это решение не принимается
l = res = 0
with open('add/course_57248/24-164.txt') as data:
    for d in data:
        if d.count('E') < 20:
            for a in set(d):  # уменьшение проходов
                if d.count(a) > 1:  # уменьшение проходов
                    for r in range(len(d) - 1):
                        if d[r] == a:
                            l = r  # фиксируем левую границу при наступлении события
                        if d[r + 1] == a:  # окончание события
                            res = max(res, r - l + 1)
print(res)  # 273


# https://stepik.org/lesson/511852/step/12?auth=login&unit=504044
with open('add/course_57248/24-s1.txt') as file:
    data = file.readlines()
    s = ''
    cnt = 0
    for d in data:
        q = d.count('Q')
        if q >= cnt:
            cnt = q
            s = d
    alf = sorted(set(s.strip()))
    num = [s.count(a) for a in alf]
    w = alf[num.index(min(num))]  # буква встречается реже всего, но стоит раньше в алфавите
cnt = 0
for d in data:
    cnt += d.count(w)
print(w, cnt, sep='')  # C38412


# https://stepik.org/lesson/511852/step/13?auth=login&unit=504044
cnt = 0
with open('add/course_57248/24-j9.txt') as file:
    s = file.read().strip()
    for i in range(len(s) // 2):
        a = s[i]
        b = s[i-1]
        cnt += s[i] == s[-i - 1]
print(cnt)


# https://stepik.org/lesson/511852/step/14?auth=login&unit=504044
idx = [0] * 26
with open('add/course_57248/24-s2.txt') as file:
    s = file.read().strip()
    alf = sorted(set(s))
    for i in range(1, len(s)):
        if s[i - 1] == 'A':
            idx[alf.index(s[i])] += 1
    cnt = max(idx)
    i_cnt = idx.index(cnt)
    w = alf[i_cnt]
    pass
print(w, cnt, sep='')  # L1567


# https://stepik.org/lesson/511852/step/15?auth=login&unit=504044
l = flag = res = 0
with open('add/course_57248/24.txt') as file:
    s = file.read().strip()
    for r in range(len(s) - 1):
        if s[r] != s[r + 1] and not flag:  # условие события
            l = r
            flag = 1
        # завершение события: повторяющаяся буква или конец строки
        if flag and (s[r] == s[r + 1] or r == len(s) - 2):
            res = max(res, r - l + 1)
            flag = 0
print(res)  # 35



# https://stepik.org/lesson/511852/step/16?auth=login&unit=504044
l = flag = cnt = 0
res = idx = 0
with open('add/course_57248/24-164.txt') as file:
    txt = file.read()
    data = txt.split()
    for i, s in enumerate(data):
        s = s.strip()
        for r in range(len(s) - 1):
            if s[r] == s[r + 1]:  # start event
                if not flag:
                    l = r
                    flag = 1
            if s[r] != s[r + 1] and flag:  # end event
                cnt = max(cnt, r - l + 1)
                l = flag = 0
            if flag and s[r] == s[r + 1] and r == len(s) - 2:  # end line
                cnt = max(cnt, r - l + 2)
                l = flag = 0
        if cnt > res:
            res = cnt
            idx = i

st = data[idx]  # работаем с найденой строкой (через ее индекс)
w = ''
c = 0
for a in sorted(set(st)):
    if st.count(a) > c:
        w = a
        c = st.count(a)
print(w, txt.count(w), sep='')  # K36582

