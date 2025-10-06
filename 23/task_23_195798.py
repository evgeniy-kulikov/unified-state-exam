""""""
"""
Task 23
ЕГЭ информатика 2025. Полный курс
https://stepik.org/course/195798
"""


""" 26.2 Практика (ур. базовый) """
# https://stepik.org/lesson/1229243/step/1?unit=1242784
def f(st,end):
    if st < end:
        return 0
    if st == end:
        return 1
    return f(st-1, end) + f(st // 2, end)

print(f(30,9) * f(9,1))  # 322


def f(st,end):
    if st > end or st == 20:
        return 0
    if st == end:
        return 1
    return f(st+1, end) + f(st+2, end) + f(st*3, end)

print(f(4,10) * f(10,22))  # 715


# https://stepik.org/lesson/1229243/step/4?unit=1242784
def f(st,end):
    if st > end:
        return 0
    if st == end:
        return 1
    return f(st+1, end) + f(st*3, end)

print(f(1,30) * f(30,50) * f(50,150))  # 56




""" 26.3 Практика (ур. усложненный) """
# https://stepik.org/lesson/1229244/step/1?unit=1242785
def f(st,end, fl):
    if st == end:
        return 1
    elif st > end + 1:  # end + 1  т.к. есть команда  st - 1
        return 0
    else:
        if fl:
            return f(st - 1, end, 0) + f(st * 2, end, 1) + f(st * 3, end, 1)
        else:
            return f(st * 2, end, 1) + f(st * 3, end, 1)

print(f(3,15, 1))  # 6



# https://stepik.org/lesson/1229244/step/2?unit=1242785
from functools import lru_cache
res = set()

@lru_cache()
def f(st, cnt):
    if not cnt:
        res.add(st)
        return 0
    return f(st + 3, cnt - 1) + f(st - 2, cnt - 1)
f(1, 68)
print(len(res))  # 69


# https://stepik.org/lesson/1229244/step/3?unit=1242785)
def f(st, en, cnt):
    if st > en:
        return 0
    if st == en and cnt == 1:
        return 1
    return f(st + 1, en, cnt) + f(st + 2, en, cnt) + f(st * 2, en, cnt + 1) + f(st * 3, en, cnt + 1)

print(f(1, 11, 0))  # 152


# https://stepik.org/lesson/1229244/step/4?unit=1242785
res = set()

def f(st, cnt):
    if cnt == 0:
        res.add(st)
        return 0
    return f(st + 10, cnt - 1) + f(st - 5, cnt - 1)

f(1, 15)
print(len(res))  # 16


# https://stepik.org/lesson/1229244/step/5?unit=1242785
def f(st, en, fl):
    if st == en:
        return 1
    if st > en:
        return 0
    if not fl:
        return f(st + 2, en, 1) + f(st * 3, en, 1)
    return f(st**2, en, 0) + f(st + 2, en, 1) + f(st * 3, en, 1)

print(f(2, 64, 1))  # 55


# https://stepik.org/lesson/1229244/step/6?unit=1242785
def f(st, en, cnt):
    cnt += sum([st == 15, st == 21])
    if st == en:
        if cnt == 1:
            return 1
        return 0
    if st > en or cnt > 1:
        return 0
    return f(st + 1, en, cnt) + f(st + 2, en, cnt) + f(st * 3, en, cnt)
print(f(6, 25, 0))  # 2700

# variant
def f(st, en, c=0):
    if st == en:
        return 1
    elif st > en or st == c:
        return 0
    return f(st + 1, en, c) + f(st + 2, en, c) + f(st * 3, en, c)
print(f(6, 15) * f(15, 25, 21) + f(6, 21, 15) * f(21, 25))  # 2700


# https://stepik.org/lesson/1229244/step/7?unit=1242785
res = set()
def f(st, cnt=0):
    if cnt == 4:
        res.add(st)
        return None
    f(st + 2, cnt + 1)
    f(st * 3, cnt + 1)

f(1)
print(len(res))  # 8
