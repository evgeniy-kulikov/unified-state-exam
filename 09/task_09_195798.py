""""""
"""
Task 09
ЕГЭ информатика 2025. Полный курс
https://stepik.org/course/195798
"""

""" 14.2 Практика (ур. базовый) """
# https://stepik.org/lesson/1222738/step/1?unit=1236141
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        ls = sorted(map(int, f.split()))
        if len(set(ls)) == 5:
            cnt += ls[0] + ls[-1] < sum(ls[1:-1]) * 3 / 4
print(cnt)  # 11420



# https://stepik.org/lesson/1222738/step/2?unit=1236141
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        ls = list(map(int, f.split()))
        cnt += any([ls.count(18) == 5, not sum(ls) % 18])
print(cnt)  # 923

# Второе условие задачи делает излишним проверку первого условия
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        ls = list(map(int, f.split()))
        cnt += not sum(ls) % 18
print(cnt)  # 923


# https://stepik.org/lesson/1222738/step/4?unit=1236141
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        ls = sorted(map(int, f.split()))
        d = [i for i in ls if not i % 3]
        cnt += all([len(d) == 3, ls[-1] - ls[0] <= sum(d)])
print(cnt)  # 1835


# https://stepik.org/lesson/1222738/step/4?unit=1236141
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        a,b,c,d = sorted(map(int, f.split()))
        if d < a+b+c:
            cnt += a+d == b+c
print(cnt)  # 116


# https://stepik.org/lesson/1222738/step/5?unit=1236141
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        a,b,c = list(map(int, f.split()))
        cnt += any([a * b % 10 == 4, b * c % 10 == 4, a * c % 10 == 4])
print(cnt)  # 965


# https://stepik.org/lesson/1222738/step/6?unit=1236141
from math import prod
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        d = sorted(map(int, f.split()))
        if d[-1]**3 >= prod(d[:-1]) * 2:
            cnt += d[0] > 10
            # cnt += sum(1 for i in d if i > 10) == 4
print(cnt)  # 1820


# https://stepik.org/lesson/1222738/step/7?unit=1236141
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        d = sorted(map(int, f.split()))
        cnt += (d[0] + d[-1]) / 2 in d
print(cnt)  # 76


# https://stepik.org/lesson/1222738/step/7?unit=1236141
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        a,b,c = list(map(int, f.split()))
        cnt += any([(a+b)/2==c, (a+c)/2==b, (b+c)/2==a])
print(cnt)  # 67


# https://stepik.org/lesson/1222738/step/9?unit=1236141
from itertools import permutations
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        d = list(map(int, f.split()))
        cnt += all(not sum(p) % 2 for p in permutations(d, 2))
print(cnt)  # 29


# https://stepik.org/lesson/1222738/step/10?unit=1236141
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        d = sorted(map(int, f.split()))
        if len(set(d)) == 5:
            m = d[2] * 2
            cnt += all([m > d[-1], m > d[0]*3])
print(cnt)  # 2914


# https://stepik.org/lesson/1222738/step/11?unit=1236141
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        d = list(map(int, f.split()))
        rep = [i for i in d if d.count(i) > 1]
        one = [i for i in d if d.count(i) == 1]
        if all([set([rep.count(i) for i in rep]) == {2, 4}, len(one)==3]):
            cnt += sum(one) / 3 >= max(rep)
print(cnt)  # 647


# https://stepik.org/lesson/1222738/step/12?unit=1236141
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        d = list(map(int, f.split()))
        rep = [i for i in d if d.count(i) == 2]
        one = [i for i in d if d.count(i) == 1]
        if all([len(set(rep)) == 3, len(one)==1]):
                cnt += (max(rep) + min(rep)) / 2 < one[0]
print(cnt)  # 3382


# https://stepik.org/lesson/1222738/step/12?unit=1236141
cnt = res = 0
with open('test.txt') as fl:
    for f in fl:
        cnt += 1
        d = list(map(int, f.split()))
        rep = [i for i in d if d.count(i) == 3]
        one = [i for i in d if d.count(i) == 1]
        if len(rep) == 3 and len(one) == 4:
            if rep[0] > sum(d) / 7:
                res = cnt
print(res)  # 15958


# https://stepik.org/lesson/1222738/step/12?unit=1236141
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        a,b,c,d = sorted(map(int, f.split()))
        if not (a + d) % 3:
            cnt += any([b-a == d-c, d-a == c-b, c-a == d-b])
print(cnt)  # 6



""" 14.3 Практика (ур. усложненный) """
# https://stepik.org/lesson/1222739/step/1?unit=1236142
from math import prod
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        d = f.split()
        ml = prod(map(int, ''.join(d)))
        sm = sum(map(int, d))
        cnt += ml > sm
print(cnt)  # 3649


# https://stepik.org/lesson/1222739/step/2?unit=1236142
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        a,b,c,d = sorted(map(int, f.split()))
        if d < a+b+c:
            cnt += all([b + a != d + c, d + a != c + b, c + a != d + b])
print(cnt)  # 2396


# https://stepik.org/lesson/1222739/step/3?unit=1236142
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        d = list(map(int, f.split()))
        one = [i for i in d if d.count(i) == 1]
        two = [i for i in d if d.count(i) == 2]
        if len(one) == 4 and len(two) == 2:
            cnt += sum(one) / 4 >= sum(two)
print(cnt)  # 64


# https://stepik.org/lesson/1222739/step/4?unit=1236142
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        d = list(map(int, f.split()))
        a = len(d) > len(set(d))
        b = sum(i % 2 for i in d) == 3
        cnt += a != b
print(cnt)  # 1852


# https://stepik.org/lesson/1222739/step/5?unit=1236142
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        d = list(map(int, f.split()))
        a = len(d) == len(set(d))
        b = sum(i % 2 for i in d) < 3
        cnt += a and b
print(cnt)  # 1078


# https://stepik.org/lesson/1222739/step/6?unit=1236142
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        d = list(map(int, f.split()))
        if len(d) == len(set(d)):
            a = [i for i in d if not i % 2]
            b = [i for i in d if i % 2]
            cnt += len(a) > len(b) and sum(a) < sum(b)
print(cnt)  # 241


# https://stepik.org/lesson/1222739/step/7?unit=1236142
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        d = [i % 2 for i in map(int, f.split())]
        for i in range(3):
            if sum(d[i: i+3]) == 3:
                cnt += 1
                break
print(cnt)  # 248


# https://stepik.org/lesson/1222739/step/8?unit=1236142
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        d = list(map(int, f.split()))
        n = sum(d) / 5
        cnt += len([i for i in d if i > n]) >= 3
print(cnt)  # 1035


# https://stepik.org/lesson/1222739/step/9?unit=1236142
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        d = list(map(int, f.split()))

        one = sum(d.count(i) == 1 for i in d) == 4
        two = sum(d.count(i) == 2 for i in d) == 2
        a = one and two

        even = [i for i in d if not i % 2]
        odd = [i for i in d if i % 2]
        if even:
            even = sum(even) / len(even)
        else:
            even = 0
        if odd:
            odd = sum(odd) / len(odd)
        else:
            odd = 0
        b = abs(even - odd) > 50

        cnt += a != b
print(cnt)  # 862


# https://stepik.org/lesson/1222739/step/10?unit=1236142
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        d = list(map(int, f.split()))
        one = list(i for i in d if d.count(i) == 1)
        two = list(i for i in d if d.count(i) > 1)
        if one and two:
          cnt += sum(one) / len(one) < sum(two) / len(two)
print(cnt)  # 1770


# https://stepik.org/lesson/1222739/step/10?unit=1236142
with open('test.txt') as fl:
    for f in fl:
        d = sorted(map(int, f.split()))
        one = list(i for i in d if d.count(i) == 1)
        two = list(i for i in d if d.count(i) == 2)
        if len(one) == 2 and len(two) == 4 and d[-1] not in two:
            if d[0] * d[-1] > sum(d[1:-1]):
                print(sum(d))  # 138
                break


# https://stepik.org/lesson/1222739/step/12?unit=1236142
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        d = list(map(int, f.split()))
        one = sum(1 for i in d if d.count(i) == 1) == 4
        rep = sum(1 for i in d if d.count(i) == 3) == 3
        a = one and rep
        b = sum(d[i] <= d[i + 1] for i in range(6)) == 6
        cnt += a + b <= 1
print(cnt)  # 14018


# https://stepik.org/lesson/1222739/step/13?unit=1236142
from math import prod
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        d = list(map(int, f.split()))
        one = [i for i in d if d.count(i) == 1]
        rep = [i for i in d if d.count(i) == 2]
        if len(one) == 3 and len(rep) == 4:
            cnt += prod(rep) > prod(one) * 2
print(cnt)  # 162


# https://stepik.org/lesson/1222739/step/14?unit=1236142
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        d = sorted(map(int, f.split()))
        one = [i for i in d if d.count(i) == 1]
        rep = [i for i in d if d.count(i) > 1]
        if all([one, rep, d[0] not in rep]):
            cnt += d[0] + d[-1] < sum(rep)
print(cnt)  # 447


# https://stepik.org/lesson/1222739/step/15?unit=1236142
# Задача - головоломка!!!!
res = 0
ls = []
with open('test.txt') as fl:
    for f in fl:
        ls += [list(map(int, f.split()))]
    rotate = list(zip(*ls))
    for row in ls:
        cnt = 0
        for i in range(6):
            cnt += row.count(row[i]) == 1 and rotate[i].count(row[i]) > 150
        res += cnt >= 5
print(res)  # 9527



""" 14.4 Закрепление """
# https://stepik.org/lesson/1222740/step/9?unit=1236143
cnt = 0
with open('test.txt') as fl:
    for f in fl:
        d = list(map(float, f.replace(',', '.').split()))
        cnt += sum(d) / 24 - min(d) >= 8
print(cnt)  # 51



""" 15.3 Закрепление """
""" 16.4 Закрепление """
# https://stepik.org/lesson/1223041/step/9?auth=login&unit=1236528
# https://stepik.org/lesson/1223041/step/9?unit=1236528
c = 0
with open('test.txt') as fl:
    for f in fl:
        d = list(map(int, f.split()))
        if len(d) == len(set(d)):
            even = [i for i in d if not i % 2]
            odd = [i for i in d if i % 2]
            c += len(even) >= 3 and sum(even) < sum(odd)
    print(c)  # 241


""" 17.4 Закрепление """
# https://stepik.org/lesson/1223105/step/9?unit=1236594
from statistics import mean
c = 0
with open('test.txt') as fl:
    for f in fl:
        d = list(map(int, f.split()))
        two = [i for i in d if d.count(i) == 2]
        one = [i for i in d if d.count(i) == 1]
        if len(two) == 4 and len(one) == 3:
            c += mean(one) < mean(two)
    print(c)  # 24


""" 19.4 Закрепление """
# https://stepik.org/lesson/1225428/step/9?unit=1238919
c = 0
with open('test.txt') as fl:
    for f in fl:
        d = list(map(int, f.split()))
        if len(set(d)) == 5:
            even = [i for i in d if not i % 2]
            odd = [i for i in d if i % 2]
            if len(even) > len(odd):
                c += sum(even) < sum(odd)
    print(c)  # 241


""" 20.4 Закрепление """
# https://stepik.org/lesson/1226263/step/9?unit=1239750
from statistics import  mean
c = 0
with open('test.txt') as fl:
    for f in fl:
        d = list(map(float, f.split()))
        c += max(d) >= mean(d) + 7
    print(c)  # 241


""" 21.4 Закрепление """
# https://stepik.org/lesson/1227125/step/9?unit=1240643
c = 0
with open('test.txt') as fl:
    for f in fl:
        x,y,z = (map(int, f.split()))
        d = sorted([x*y, z*y, z*x])
        c += sum(d[:-1]) < d[-1]
    print(c)  # 3119


""" 23.4 Закрепление (ч. 1) """
# https://stepik.org/lesson/1227731/step/9?unit=1241246
c = 0
with open('test.txt') as fl:
    for f in fl:
        d = list(map(int, f.split()))
        if len(set(d)) == 5:
            odd = [i for i in d if i % 2]
            even = [i for i in d if not i % 2]
            c += len(even) > 2 and sum(even) < sum(odd)
print(c)  # 241


""" 24.4 Закрепление (ч. 1) """
# https://stepik.org/lesson/1227745/step/9?unit=1241266
def good(ls: list):
    for n in ls:
        if ls.count(n) == 1 and d.count(n) == 46:
            return 1
    return 0

cnt = 0
with open('test.txt') as fl:
    d = list(map(int, fl.read().split()))
    for i in range(0, len(d), 6):
        row = d[i:i+6]
        cnt += good(row)
print(cnt)  # 445



