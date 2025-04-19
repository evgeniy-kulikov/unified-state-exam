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
cnt = 0
with open('9-170.txt') as fl:
    for el in fl:
        unic, rep = [], []
        d = sorted(map(int, el.split()))
        for i in range(5):
            if d[i] == d[i + 1] or d[i] in rep:
                rep.append(d[i])
            else:
                unic.append(d[i])
        if d[-1] in rep:
            rep.append(d[-1])
        else:
            unic.append(d[-1])
        if len(unic) == 2:
            cnt += prod(rep)**(1/len(rep)) >= prod(unic)
            # prod(rep)**(1/len(rep)) - среднее ГЕОМЕТРИЧЕСКОЕ
print(cnt)  # 12


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

