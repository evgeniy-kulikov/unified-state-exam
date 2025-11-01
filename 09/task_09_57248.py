""""""
"""
Task 09
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248
"""

# https://stepik.org/lesson/797932/step/1?auth=login&unit=819598
cnt = 0
with open('9-170.txt') as fl:
    for el in fl:
        dbl = None
        ls = list(map(int, el.split()))
        ls.sort()
        if len(set(ls)) == 5:
            for i in range(5):
                if ls[i] == ls[i + 1]:
                    dbl = ls[i]
                    ls.remove(dbl)
                    ls.remove(dbl)
                    break
            # if dbl * 2 >= ls[0] + ls[-1]:
            if dbl * 2 >= min(ls) + max(ls):
                cnt += 1
print(cnt)  # 1159


# https://stepik.org/lesson/797932/step/2?auth=login&unit=819598
from statistics import mean
cnt = 0
with open('9-170.txt') as fl:
    for el in fl:
        ls = list(map(int, el.split()))
        if len(set(ls)) == 6:
            ls.sort()
            if mean(ls) >= (ls[2] + ls[3]) / 2:
                cnt += 1
print(cnt)  # 2097


# https://stepik.org/lesson/797932/step/3?auth=login&unit=819598
from math import prod  # перемножить элементы списка
from statistics import geometric_mean

cnt = 0
with open('09/09-01.txt') as file:
    for f in file:
        d = list(map(int, f.split()))
        one = [i for i in d if d.count(i) == 1]
        rep = [i for i in d if d.count(i) > 1]
        if len(one) == 2 and geometric_mean(rep) >= prod(one):
            cnt += 1
    print(cnt)  # 12
# prod(rep)**(1/len(rep)) - среднее ГЕОМЕТРИЧЕСКОЕ




# Мой другой подход!!!
# https://stepik.org/lesson/797932/step/4?auth=login&unit=819598
def fn(dabl, unic):
    for d in dabl:
        for u in unic:
            if d < u:
                return False
    return True

cnt = 0
with open('9-170.txt') as fl:
    for el in fl:
        unic, dabl = [], []
        d = dict()
        for n in map(int, el.split()):
            d.setdefault(n, 0)
            d[n] += 1
        dabl = [k for k, v in d.items() if v == 2]
        unic = [k for k, v in d.items() if v == 1]
        if dabl and fn(dabl, unic):
            cnt += 1
print(cnt)  # 665


# https://stepik.org/lesson/797932/step/5?auth=login&unit=819598
def fn(trio, unic):
    if sum(unic) * 3 <= trio[0] ** 3:
        return True
    return False

cnt = 0
with open('9-170.txt') as fl:
    for el in fl:
        unic, trio = [], []
        d = dict()
        for n in map(int, el.split()):
            d.setdefault(n, 0)
            d[n] += 1
        trio = [k for k, v in d.items() if v == 3]
        unic = [k for k, v in d.items() if v == 1]
        if trio and len(unic) == 3 and fn(trio, unic):
            cnt += 1
print(cnt)  # 134


# https://stepik.org/lesson/797932/step/6?auth=login&unit=819598
cnt = 0
with open('9-176.txt') as fl:
    for el in fl:
        unic, rep = [], []
        d = dict()
        for n in map(int, el.split()):
            d.setdefault(n, 0)
            d[n] += 1
        rep = [k for k, v in d.items() if v > 1]
        unic = [k for k, v in d.items() if v == 1]
        if rep and sum(unic) % 2:
            cnt += 1
print(cnt)  # 322


# https://stepik.org/lesson/797932/step/6?auth=login&unit=819598
cnt = 0
with open('9-210.txt') as fl:
    for el in fl:
        unic, rep = [], []
        d = dict()
        ls = list(map(int, el.split()))
        for n in ls:
            d.setdefault(n, 0)
            d[n] += 1
        ls_rep = [k for k, v in d.items() if v > 1]
        rep = [el for el in ls if el in ls_rep]
        unic = [k for k, v in d.items() if v == 1]
        if rep and max(ls) not in rep:
            if max(ls) + min(ls) > sum(rep):
                cnt += 1
print(cnt)  # 408


# https://stepik.org/lesson/797932/step/8?auth=login&unit=819598
cnt = 0
with open('9-210.txt') as fl:
    for el in fl:
        unic, rep = [], []
        d = dict()
        ls = list(map(int, el.split()))
        for n in ls:
            d.setdefault(n, 0)
            d[n] += 1
        ls_rep = [k for k, v in d.items() if v > 1]
        rep = [el for el in ls if el in ls_rep]
        unic = [k for k, v in d.items() if v == 1]
        if rep and min(ls) not in rep:
            if max(ls) + min(ls) < sum(rep):
                cnt += 1
print(cnt)  # 447


# https://stepik.org/lesson/797932/step/9?auth=login&unit=819598
cnt = 0
with open('9_2024.txt') as fl:
    for el in fl:
        unic, rep = [], []
        d = dict()
        ls = list(map(int, el.split()))
        for n in ls:
            d.setdefault(n, 0)
            d[n] += 1
        rep = [k for k, v in d.items() if v == 2]
        unic = [k for k, v in d.items() if v == 1]
        if len(rep) == 2 and len(unic) == 3:
            if sum(rep) / 2 < sum(ls) / 7:
                cnt += 1
print(cnt)  # 83


# https://stepik.org/lesson/797932/step/10?auth=login&unit=819598
cnt = 0
Mx = None
with open('add/course_57248/9_23193.txt') as fl:
    for f in fl:
        cnt += 1
        d = list(map(int, f.split()))
        one = [i for i in d if d.count(i) == 1]
        rep = [i for i in d if d.count(i) == 3]
        if len(one) == 3 and len(rep) == 3 and rep[0] > sum(one) / 3:
            Mx = cnt
    print(Mx)  # 10493


# https://stepik.org/lesson/797932/step/10?auth=login&unit=819598
from statistics import mean
cnt = 0
res = None
with open('add/course_57248/9_23193.txt') as fl:
    for f in fl:
        cnt += 1
        d = list(map(int, f.split()))
        one = [i for i in d if d.count(i) == 1]
        rep = [i for i in d if d.count(i) == 3]
        if len(one) == 3 and len(rep) == 3 and rep[0] > mean(one):
            res = cnt
    print(res)  # 10493



# https://stepik.org/lesson/797932/step/13?auth=login&unit=819598
from statistics import mean
m = []
with open('add/course_57248/9vitt_23154.txt') as file:
    for fl in file:
        d = list(map(int, fl.split()))
        one = [i for i in d if d.count(i) == 1]
        rep = [i for i in d if d.count(i) == 3]
        if len(one) == 3 and len(rep) == 3 and rep[0] < 2 * min(one):
            m.append(mean(d))
    print(int(mean(m)))  # 53


# https://stepik.org/lesson/797932/step/14?auth=login&unit=819598
from statistics import mean
Mx = 0
with open('add/course_57248/9_z_23248.txt') as fl:
    for f in fl:
        cnt += 1
        d = list(map(int, f.split()))
        one = [i for i in d if d.count(i) == 1]
        rep = [i for i in d if d.count(i) == 2]
        if len(one) == 4 and len(rep) == 2 and rep[0] > mean(one):
            Mx = sum(d)
    print(Mx)  # 367


# https://stepik.org/lesson/797932/step/15?auth=login&unit=819598
# повтор
# https://stepik.org/lesson/797932/step/10?auth=login&unit=819598
from statistics import mean
cnt = 0
res = None
with open('add/course_57248/9_основа.txt') as fl:
    for f in fl:
        cnt += 1
        d = list(map(int, f.split()))
        one = [i for i in d if d.count(i) == 1]
        rep = [i for i in d if d.count(i) == 3]
        if len(one) == 3 and len(rep) == 3 and rep[0] > mean(one):
            res = cnt
    print(res)  # 10493



