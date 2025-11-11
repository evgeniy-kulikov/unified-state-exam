""""""
"""
Task 25
Информатика Подготовка к ЕГЭ 2026
https://stepik.org/course/182932
"""

""" 16.1 Задачи на маски числа """
# https://stepik.org/lesson/1167509/step/1?unit=1179830
from fnmatch import fnmatch
st = 1234568 // 17 * 17
en = 123459968 + 1
for n in range(st, en, 17):
    if fnmatch(str(n), '12345?6?8'):
        print(n, n // 17)
"""
123450668 7261804
123451688 7261864
123456618 7262154
123457638 7262214
123458658 7262274
123459678 7262334
"""


# https://stepik.org/lesson/1167509/step/2?unit=1179830
from fnmatch import fnmatch
en = 12349997 + 1  # 10**8
for n in range(0, en, 141):
    if fnmatch(str(n), '1234*7'):
        print(n, n // 141)
"""
1234737 8757
12341307 87527
12342717 87537
12344127 87547
12345537 87557
12346947 87567
12348357 87577
12349767 87587
"""


# https://stepik.org/lesson/1167509/step/3?unit=1179830
from fnmatch import fnmatch
st = 123005670 // 169 * 169
en = 123995679 + 1  # 10**9
for n in range(0, en, 169):
    if fnmatch(str(n), '123*567?'):
        print(n, n // 169)
"""
12325677 72933
12385672 73288
123165679 728791
123225674 729146
123515678 730862
123575673 731217
123865677 732933
123925672 733288
"""


# https://stepik.org/lesson/1167509/step/4?unit=1179830
from fnmatch import fnmatch
st = 120045 // 51 * 51
en = 129945 + 1  # 10**6
for n in range(0, en, 51):
    if fnmatch(str(n), '12*45*'):
        print(n, n // 51)
"""
122145 2395
122451 2401
124542 2442
124593 2443
127245 2495
"""


# https://stepik.org/lesson/1167509/step/5?unit=1179830
from fnmatch import fnmatch
st = 1021394 // 2023 * 2023
en = 1921399994 + 1  # 10**10
for n in range(0, en, 2023):
    if fnmatch(str(n), '1?2139*4'):
        print(n, n // 2023)
"""
162139404 80148
1321399324 653188
1421396214 702618
1521393104 752048
"""


# https://stepik.org/lesson/1167509/step/6?unit=1179830
from fnmatch import fnmatch
def f(n):
    div = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            div |= {i, n // i}
    return sum(div) % 21

res = []
cnt = 5
for n in range(10**7, 0, -1):
    if fnmatch(str(n), '9?*55*7'):
        res.append((n, f(n)))
        cnt -= 1
    if not cnt:
        break
res.sort()
[print(*i) for i in res]
"""
9995597 18
9996557 12
9997557 12
9998557 17
9999557 0
"""


# https://stepik.org/lesson/1167509/step/7?unit=1179830
from fnmatch import fnmatch
st = 1203456009 // 98591 * 98591
en = 129399456999
for n in range(st, en + 1, 98591):
# for n in range(0, 10**12 + 1, 98591):
    if fnmatch(str(n), '12?3*456??9'):
        print(n, n // 98591)
"""
120313456439 1220329
120383456049 1221039
125351456539 1271429
"""


""" GOOD TASK """
# https://stepik.org/lesson/1167509/step/8?unit=1179830
from itertools import product
res = []
st = ['']
for i in range(1, 4):
    st += [''.join(p) for p in product('13579', repeat=i)]

for a in '02468':
    for b in st:
        n = int(f'1{a}2157{b}4')
        if not n % 133:
            res.append((n, n // 133))
res.sort()
[print(*i) for i in res]
"""
122157574 918478
1021575394 7681018
1421575554 10688538
1821575714 13696058
"""


# https://stepik.org/lesson/1167509/step/9?unit=1179830
from fnmatch import fnmatch
def dv(n):
    d = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            d |= {i, n // i}
    res = [i for i in d if not i % 2]
    if len(res) >= 4:
        return sum(res)

cnt = 7
for n in range(65000, 10**8):
    if fnmatch(str(n), '6*97*5?'):
        if dv(n):
            print(n, dv(n))
            cnt -= 1
    if not cnt:
        break
"""
69750 129792
69752 122080
69756 139536
69758 75152
609750 1103232
609752 1291248
609754 630840
"""
