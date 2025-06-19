# https://stepik.org/lesson/504398/step/1?unit=496246
from itertools import product
def fn(ls:list, n):
    mx = 0
    for p in product(ls, repeat=n):
        v = set(p)
        n = sum(v)
        if not n % 25:
            mx = max(mx, n)
    return mx


# def fn(ls:list):
#     sm = 0
#     for i in range(1, n):
#         for j in range(i, n):
#             t = ls[:i] + [ls[j]]
#             r = sum(t)
#             if not r % 25:
#                 sm = max(sm, r)
#     return sm



# with open('add/test.txt') as fl:
#     n = int(fl.readline())
#     ls = list(map(int, fl))
#     print(fn(ls, n))


with open('add/course_57248/27-60a.txt') as fl:
    n = int(fl.readline())
    ls = list(map(int, fl))
    print(fn(ls, n), end=' ')
#
# with open('add/course_57248/27-60b.txt') as fl:
#     n = int(fl.readline())
#     ls = list(map(int, fl))
#     print(fn(ls))
# 650 4999775
# 925 5036375






