"""
Task 17
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248
"""


""" 6.2 Тренировка 17,18,23 """
# https://stepik.org/lesson/552239/step/1?unit=545967
mx = 0
mn = 19991
cnt = 0
for i in range(777, 19990 + 1):
    n_oct = i
    mx_oct = 0
    while n_oct:
        mx_oct = max(mx_oct, n_oct % 8)
        n_oct = n_oct // 8
    if (not i % 11 or not i % 13) and i % 15 and mx_oct == 6:
        cnt += 1
        mx = max(mx, i)
        mn = min(mn, i)
print(cnt, mx - mn)  # 803 19082


# https://stepik.org/lesson/552239/step/2?unit=545967
mn = 52312
cnt = 0
for i in range(4616, 52312):
    n = str(i)
    if sum(map(int, n)) == 10 and '0' in n:
        cnt += 1
        mn = min(i, mn)
print(cnt, mn)  # 555 5005


# https://stepik.org/lesson/552239/step/3?unit=545967
mn = 13487
cnt = 0
for n in range(7525, 13487):
    if all([not n % 7, n % 6, n % 9, n % 14, n % 21]):
        cnt += 1
        mn = min(n, mn)
print(cnt, mn)  # 284 7525

# Короче
mn = 13487
cnt = 0
for n in range(7525, 13487, 7):
    if all([n % 2, n % 3]):
        cnt += 1
        mn = min(n, mn)
print(cnt, mn)  # 284 7525


# https://stepik.org/lesson/552239/step/4?unit=545967
cnt, mx  = 0, 0
for n in range(25552, 58886):
    c = 0
    for i in range(10, 100):
        c += not n % i
        if c == 15:
            cnt += 1
            mx = max(n, mx)
            break
print(mx, cnt)  # 58800 420


# https://stepik.org/lesson/552239/step/5?unit=545967
ls = []
for n in range(4735, 8757):
    if all([not n % 5, not n % 17, n % 7, n % 14]):
        s = str(n)
        if s[2] >= s[1]:
            ls += [n]
ls.sort()
res = ls[0] + ls[-1] + sum(ls) / len(ls)
print(int(res))  # 20510



""" 7.28 ЕГЭ Тренировка 17 """
# https://stepik.org/lesson/421032/step/1?unit=410642
with open('17-1.txt') as fl:
    d = list(map(int, fl))
cnt = 0
nm = -10_001
for i in range(len(d) - 1):
    ls = [d[i], d[i + 1]]
    a, b = None, None
    nine = [i for i in ls if not abs(i) % 9]
    if len(nine) == 1:
        a = nine[0]
        ls.remove(a)
        b = ls[0]
        if oct(abs(b))[-1] == '3':
            cnt += 1
            nm = max(a, b, nm)
print(cnt, nm)  # 252 9971


# https://stepik.org/lesson/421032/step/2?unit=410642
with open('17-2.txt') as fl:
    d = list(map(int, fl))
cnt = 0
nm = max(d)
pos = d.index(nm) + 1
for el in d:
    cnt += el == nm
print(cnt, pos)  # 9 26


# https://stepik.org/lesson/421032/step/3?unit=410642
with open('17-257.txt') as fl:
    d = list(map(int, fl))
cnt = 0
sm_pair = 0
d4 = [i for i in d if i % 10 == 4]
sm = max(d4) + min(d4)
for i in range(len(d) - 1):
    pair = sum(d[i: i + 2])
    t = d[i: i + 2]
    if pair < sm:
        cnt += 1
        sm_pair = max(pair, sm_pair)
print(cnt, sm_pair)  # 503 10094


# https://stepik.org/lesson/421032/step/4?unit=410642
def conv(ls, b = 7):
    for n in ls:
        s = ''
        while n:
            s = str(n % b) + s
            n //= b
        if '36' in s:
            return True
    return False

with open('17-243.txt') as fl:
    d = list(map(int, fl))

cnt = 0
sm_min = 100_000
d_107_max = max([i for i in d if not i % 107])

for i in range(len(d) - 1):
    el = d[i: i + 2]
    # if len([j for j in el if j > d_107_max]):
    if el[0] > d_107_max or el[1] > d_107_max:
        if conv(el):
            cnt += 1
            sm_min = min(sm_min, sum(el))
print(cnt, sm_min)  # 14 11350


# https://stepik.org/lesson/421032/step/5?unit=410642
from statistics import mean

def fn(el):
    for i in el:
        if all([not i % 7, i % 3, i % 11, i % 13]):
            return True
    return False

with open('17-4.txt') as fl:
    d = list(map(int, fl))

cnt = 0
nm = 20_000
avr = mean(d)
for i in range(len(d) - 1):
    el = d[i:i + 2]
    if (el[0] < avr or el[1] < avr) and fn(el):
        cnt += 1
        nm = min(nm, sum(el))
print(cnt, nm)  # 225 2639


# https://stepik.org/lesson/421032/step/6?auth=login&unit=410642
cnt = 0
mn = 10**10
with open('add/course_57248/17-4.txt') as fl:
    ls = list(map(int, fl.readlines()))
    avr = sum(ls) / len(ls)  # 5442.9905
    for i in range(len(ls) - 1):
        l = ls[i: i + 2]
        if sum(n < avr for n in l) and sum('7' in str(n) for n in l):
            cnt += 1
            mn = min(mn, sum(l))
print(cnt, mn)  # 827 2378


# https://stepik.org/lesson/421032/step/7?auth=login&unit=410642
cnt = 0
mn = 10**10
with open('add/course_57248/17-4.txt') as fl:
    ls = list(map(int, fl.readlines()))
    avr = sum(ls) / len(ls)  # 5442.9905
    for i in range(len(ls) - 1):
        l = ls[i: i + 2]
        if sum(n < avr for n in l) and sum('5' not in str(n) for n in l):
            cnt += 1
            mn = min(mn, sum(l))
print(cnt, mn)  # 1304 2378


# https://stepik.org/lesson/421032/step/8?auth=login&unit=410642
cnt = 0
mn = 10**10
with open('add/course_57248/17-4.txt') as fl:
    ls = list(map(int, fl.readlines()))
    avr = sum(ls) / len(ls)  # 5442.9905
    for i in range(len(ls) - 1):
        l = ls[i: i + 2]
        if sum(n < avr for n in l) and sum('1' in str(n) for n in l) == 2:
            cnt += 1
            mn = min(mn, sum(l))
print(cnt, mn)  # 231 2378


# https://stepik.org/lesson/421032/step/9?auth=login&unit=410642
cnt = mx = 0
with open('add/course_57248/17-1.txt') as fl:
    ls = list(map(int, fl.readlines()))
    avr = sum(ls) / len(ls)  # -105.6732
    for i in range(len(ls) - 2):
        l = ls[i: i + 3]
        if sum(n < avr for n in l) and sum(not n % 3 for n in l):
            cnt += 1
            mx = max(mx, sum(l))
print(cnt, mx)  # 6151 18891


"""***"""
# https://stepik.org/lesson/421032/step/10?unit=410642
c = 0
c_min = 20_001
with open('add/course_57248/17-243.txt') as fl:
    ls = list(map(int, fl))
    num = sum(sum(map(int, str(i))) for i in ls if not i % 37)  # 5121
    for i in range(len(ls) - 1):
        a, b = ls[i:i+2]
        if all([a > num, b > num]):
            c += 1
            c_min = min(c_min, a+b)
print(c, c_min)  # 3025 10383

"""**"""
# https://stepik.org/lesson/421032/step/11?unit=410642
cnt = 0
c_max = -30_001
def f(n):
    return n > 0 and str(n)[-1] == '9'

with open('add/course_57248/17-204.txt') as fl:
    ls = list(map(int, fl))
    for i in range(len(ls) - 2):
        a, b, c = ls[i:i+3]
        if all([not f(a), f(b), not f(c)]):
            cnt += 1
            c_max = max(c_max, a+b+c)
print(cnt, c_max)  # 206 23427


"""***"""
# https://stepik.org/lesson/421032/step/12?unit=410642
with open('add/course_57248/17-1.txt') as fl:
    st = flag = 0
    i_min = 100_000
    d = list(map(int, fl))
    mir = [int(d[i-1] < d[i] > d[i+1]) for i in range(1, len(d) - 1)]
    for i, k in enumerate(mir):
        if k:
            if flag:
                i_min = min(i_min, i - st)
            flag = 1
            st = i
print(sum(mir), i_min)


# https://stepik.org/lesson/421032/step/12?unit=410642
with open('add/course_57248/17-339.txt') as fl:
    sm_max = cnt = 0
    data = list(map(int, fl))
    n_min = min(i for i in data if i > 0 and not i % 19)  # 703
    for i in range(len(data) - 1):
        d = sum(data[i:i+2])
        if d < n_min:
            cnt += 1
            sm_max = max(sm_max, d)
print(cnt, sm_max)  # 4984 696



""" 7.29 ЕГЭ Тренировка 17 """
# https://stepik.org/lesson/789914/step/1?auth=login&unit=792575
cnt = 0
mn = 10**10
with open('add/course_57248/17-342.txt') as fl:
    ls = list(map(int, fl.readlines()))
    min37 = min(i for i in ls if not i % 37)  # 518
    max73 = max(i for i in ls if not i % 73)  # 438
    for i in range(len(ls) - 1):
        if sum(max73 < n < min37 for n in ls[i: i + 2]) == 1:
            cnt += 1
            mn = min(mn, sum(ls[i: i + 2]))
print(cnt, mn)  # 136 574


# https://stepik.org/lesson/789914/step/2?auth=login&unit=792575
cnt = 0
sm = 0
with open('add/course_57248/17-338.txt') as fl:
    data = list(map(int, fl))
    min_n = min(data)
    for i in range(len(data) - 1):
        d = data[i: i+2]
        if any(k % 117 == min_n for k in d):
            cnt += 1
            sm = max(sm, sum(d))
print(cnt, sm)  # 15067 199479


# https://stepik.org/lesson/789914/step/3?auth=login&unit=792575
cnt = 0
sm_max = 0
with open('add/course_57248/17-339.txt') as fl:
    data = list(map(int, fl))
    min_n = min(i for i in data if i > 0 and not i % 19)
    for i in range(len(data) - 1):
        d = data[i: i+2]
        if sum(d) < min_n:
            cnt += 1
            sm_max = max(sm_max, sum(d))
print(cnt, abs(sm_max))  # 4984 696





# https://stepik.org/lesson/789914/step/6?auth=login&unit=792575
""" Хитрая задачка """
from itertools import permutations
def f(ls):
    ls = map(str, ls)
    for p in permutations(ls, r=2):
        cnt = 0
        for i in range(4):
            cnt += p[0][i] != p[1][i]
        if cnt == 2:
            return 1

cnt = mx = 0
with open('add/course_57248/17-316.txt') as fl:
    data = list(map(int, fl))
    min_n = sum(sorted(set(data))[:3])  # 3006
    for i in range(len(data) - 2):
        d = data[i: i+3]
        if f(d) and sum(d) > min_n:
            cnt += 1
            mx = max(mx, sum(d))
print(cnt, mx)  # 3098 29764