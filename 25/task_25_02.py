"""
Task 25
Подготовка к ЕГЭ информатика
https://stepik.org/course/57248
"""

""" 7.39 ЕГЭ Тренировка 25 """

# https://stepik.org/lesson/459358/step/1?auth=login&unit=449865
def f(n):
    d = set()
    for i in range(1, int(n**0.5) + 1):
        if not n % i:
            d.add(i)
            d.add(n // i)
    if len(d) == 4: return sorted(d)

for n in range(126849, 126872):
    d = f(n)
    if d: print(*d)


# https://stepik.org/lesson/459358/step/4?auth=login&unit=449865
def f(n):
    d = set()
    for i in range(1, int(n**0.5) + 1):
        if not n % i:
            d.add(i)
            d.add(n // i)
    ls = [i for i in d if not i % 2]
    if len(ls) == 4: return sorted(ls, reverse=True)

for n in range(190201, 190281):
    d = f(n)
    if d: print(*d)



# https://stepik.org/lesson/459358/step/5?auth=login&unit=449865
""" хитрое условие """
def f(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            d.add(i)
            d.add(n // i)
    return n > sum(d) + 1  # единицу учитываем, а само число нет

cnt = 0
for n in range(2, 30001):
    cnt += f(n)
print(cnt)  # 22567


# https://stepik.org/lesson/459358/step/6?auth=login&unit=449865
""" хитрое условие """
def f(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            d.add(i)
            d.add(n // i)
    r = sum(d) + 1  # единицу учитываем, а само число нет
    return n, r

ls = []
for n in range(2, 30001):
    ls.append(f(n))

for i in range(len(ls) - 1):
    a, b  = ls[i][0], ls[i][1]
    if a < b < len(ls):
        if b == ls[b - 2][0] and a == ls[b - 2][1]:
            print(*ls[i])


# https://stepik.org/lesson/459358/step/7?auth=login&unit=449865
""" хитрое условие """
# ... имеют хотя бы 6 различных простых делителей (т.е. эти делители являются простыми числами)
def dv(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            d.add(i)
            d.add(n // i)
    return d

def prim(n):
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i: return 0
    return 1

for num in range(25317, 51238):
    pr = list()
    for n in dv(num):
        if prim(n):
            pr.append(n)
    if len(pr) >= 6:
        print(num, max(pr))
# 30030 13
# 39270 17
# 43890 19
# 46410 17


# https://stepik.org/lesson/459358/step/8?auth=login&unit=44986565
""" очень долгий перебор. Как-то нужно ещё ускорить """
def dv(n):
    d = set()
    for i in range(3, int(n ** 0.5) + 1, 2): # ищем только среди нечетных чисел
        if not n % i:
            d.add(i)
            d.add(n // i)
        if len(d) > 3: return False
    if len(d) == 3:
        return max(d)

# ищем только среди нечетных чисел
for num in range(525_784_203, 728_943_762, 2):
    r = dv(num)
    if r: print(num, r)
# 607573201 3869893
# 705911761 4330747

# Костыль
# ls = [607_573_201, 705_911_761]
# for num in ls:
#     r = dv(num)
#     if r: print(num, r)



""" 7.40 ЕГЭ Тренировка 25 """
# https://stepik.org/lesson/598432/step/1?auth=login&unit=610936
def dv(n):
    d = set()
    for i in range(1, int(n ** 0.5) + 1):
        if not n % i:
            d.add(i)
            d.add(n // i)
        if len(d) > 6: return False
    if len(d) == 6:
        return sorted(d)

for num in range(164700, 164753):
    r = dv(num)
    if r: print(*r)
# 1 2 4 41177 82354 164708
# 1 3 9 18301 54903 164709
# 1 2 4 41179 82358 164716
# 1 2 4 41183 82366 164732



""" 7.41 ЕГЭ Тренировка 25 """
# https://stepik.org/lesson/698690/step/1?auth=login&unit=698986
a = '0123456789ABCDEF'[::-1]
for i in a:
    for k in a:
        n = int(f'1{i}DED{k}CED', 16)
        if not n % int('79', 16):
            print(n, n // int('79', 16))
# 8555171053 70703893
# 6407666925 52955925
# 5065538797 41863957


# https://stepik.org/lesson/698690/step/3?auth=login&unit=698986
a = '01234567'[::-1]
for i in a:
    for k in a:
        n = int(f'1{i}345{k}700', 8)
        if not n % int('114', 8):
            print(n, n // int('114', 8))
# 30299072 398672
# 26106304 343504
# 21913536 288336


# https://stepik.org/lesson/698690/step/4?auth=login&unit=698986
from fnmatch import fnmatch
dv = int('101101', 2)
for n in range(int('111111111111', 2), int('101010101001', 2) - 1, -1):  # 4095 - 2729
    if fnmatch(f'{n:b}', '1?1?1?1?1??1'):
        if not n % dv:
            print(n, n // dv)
# 4095 91
# 2745 61


# https://stepik.org/lesson/698690/step/5?auth=login&unit=698986
from fnmatch import fnmatch
def tr(n):
    s = ''
    while n:
        s = str(n % 3) + s
        n //= 3
    return s

for n in range(int('22122212221', 3), int(' 20102010201', 3) - 1, -1):
    if fnmatch(tr(n), '2?1?2?1?2?1'):
        if not n % 148:
            print(n, n // 148)
# 170200 1150
# 128464 868
# 126244 853


# https://stepik.org/lesson/698690/step/9?auth=login&unit=698986
# Долго
from fnmatch import fnmatch
for n in range(124579, 12499579 + 1):
    if fnmatch(str(n), '124*5*79'):
        dv = sum(int(i) for i in str(n) if i in '13579')
        if not n % dv:
            print(n, sum(map(int, str(n))))

# Быстро
ls = []
""" Нужно учесть варианты: '',   [0-9],   00, 01 ... 09,   10-99  """
for i in [''] + [*range(10)] + [str(i).zfill(2) for i in range(100)]:
    for k in [''] + [*range(10)] + [str(i).zfill(2) for i in range(100)]:
        n = f'124{i}5{k}79'
        if len(n) <= 8:
            dv = sum(int(i) for i in n if i in '13579')
            if not int(n) % dv:
                ls.append((int(n), sum(map(int, str(n)))))
[print(*i) for i in sorted(ls)]
# 1249579 37
# 12409579 37
# 12452979 39
# 12456179 35
