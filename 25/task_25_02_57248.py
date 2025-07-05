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
        if len(d) > 3: return 0
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


# https://stepik.org/lesson/598432/step/9?auth=login&unit=610936
def fn(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
        if len(d) > 3: return 0  # оптимизация
    return d

# for n in range(106732567, 152673836 + 1):
for n in range(112550881, 141158161 + 1, 2):  # оптимизация на основе результата
    if n**0.5 == int(n**0.5):
        r = fn(n)
        if r and len(r) == 3:
            print(n, max(r))
# 112550881 1092727
# 131079601 1225043
# 141158161 1295029















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


# https://stepik.org/lesson/598432/step/2?auth=login&unit=610936
def fn(n):
    dv = set()
    for i in range(1, int(n ** 0.5 + 1)):
        if not n % i:
            dv.add(i)
            dv.add(n // i)
    return dv

for n in range(11275, 16329):
    if n ** 0.5 == int(n ** 0.5):
        r = fn(n)
        if len(r) == 5:
            print(*sorted(r))  # 1 11 121 1331 14641


# https://stepik.org/lesson/598432/step/3?auth=login&unit=610936
def fn(n):
    dv = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            dv.add(i)
            dv.add(n // i)
    return dv

mx = []
for n in range(268220, 270336):
    res = fn(n)
    if len(res) <= 4:
        mx.append((sum(res), len(res), *sorted(res, reverse=1)))
mx.sort(reverse=1)
print(*mx[0])  # 405456 4 270302 135151 2 1


# https://stepik.org/lesson/598432/step/4?auth=login&unit=610936
def fn(n:int):
    for i in range(2, int(n**0.5 + 1)):
        if not n % i: return 0
    return 1
cnt = 0
for n in range(1547341, 1547410):
    if fn(n):
        cnt += 1
        print(cnt, n)
# 1 1547347
# 2 1547383
# 3 1547389
# 4 1547407


""" коварное условие """
# https://stepik.org/lesson/598432/step/6?auth=login&unit=610936
def fn(n):
    dv = set()
    for i in range(2, int(n ** 0.5 + 1)):
        if not n % i:
            dv.add(i)
            dv.add(n // i)
    return dv

sm = 0
for n in range(4099, 26986):
    d = list(fn(n))
    if len(d) == 1:
        sm += sum(map(int, str(n)))
print(sm)  # 377



# https://stepik.org/lesson/598432/step/7?auth=login&unit=610936
def fn(n):
    dv = set()
    for i in range(2, int(n ** 0.5 + 1)):
        if not n % i:
            dv.add(i)
            dv.add(n // i)
    return dv

for n in range(81234, 134689 + 1):
    if n**0.5 == int(n**0.5):  # три различных натуральных делителя
        d = sorted(fn(n))
        if len(d) == 3:
            print(d[0], d[2])
# 17 4913
# 19 6859



# https://stepik.org/lesson/598432/step/8?auth=login&unit=610936
from itertools import permutations
def fn(n):
    dv = set()
    for i in range(1, int(n ** 0.5 + 1)):
        if not n % i:
            dv.add(i)
            dv.add(n // i)
    return dv

def smpl(n:int):
    if n == 1: return 0
    for i in range(2, int(n ** 0.5 + 1)):
        if not n % i: return 0
    return 1

#  в принципе лишняя функция: в данном примере во всех делителях нет более 2-х простих чисел
def mlp(d:tuple, n):
    for p in permutations(d, r=2):
        if p[0] * p[1] == n:
            return 1
    return 0

cnt = mx = 0
for n in range(125697, 190235):
    d = list(fn(n))
    dv = [i for i in d if smpl(i)]
    if len(dv) >= 2 and mlp(dv, n):
        cnt += 1
        mx = max(mx, n)
print(cnt, mx)  # 14047 190231


# https://stepik.org/lesson/598432/step/10?auth=login&unit=610936
def fn(n):
    d = set()
    for i in range(2, int(n**0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
    return d

def smpl(n):
    for i in range(2, int(n ** 0.5 + 1)):
        if not n % i: return 0
    return 1

cnt = 0
nmin = 50_001
for n in range(10_001, 50_001):
        d = fn(n)
        s = [i for i in d if smpl(i)]
        if len(s) == 3:
            cnt += 1
            nmin = min(nmin, n)
print(cnt, nmin)  # 15652 10002



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


# https://stepik.org/lesson/698690/step/6?auth=login&unit=698986
for a in range(10):
    for b in range(10):
        n = int(f'12345{a}6{b}8')
        if not n % 17:
            print(n, n // 17)
# 123450668 7261804
# 123451688 7261864
# 123456618 7262154
# 123457638 7262214
# 123458658 7262274
# 123459678 7262334


# https://stepik.org/lesson/698690/step/7?auth=login&unit=698986
# !!! НЕ РЕШЕНО. ВСЕ ЧИСЛА ДАЮТ ПАЛИНДРОМ
from fnmatch import *
def b7(n):
    s = ''
    while n:
        s += str(n % 7)
        n //= 7
    return s

# вариант '*' - пустая строка
mask = '1*586?6'
for n in range(158606, 158696 + 1):
    if fnmatch(str(n), mask):
        r = b7(n)
        if r == r[::-1]:
            print(n, sum(map(int, r)))


# # ОЧЕНЬ МНОГО !!!!!!!
for a in range(0, 9999 + 1):
    for b in range(10):
        n = int(f'1{a}586{b}6')
        r = b7(n)
        if r != r[::-1]:
            print(n, sum(map(int, r)))


# https://stepik.org/lesson/698690/step/8?auth=login&unit=698986
def b7(n):
    s = ''
    while n:
        s += str(n % 9)
        n //= 9
    return s[::-1]

def dwn(s:str):
    return all(s[i] >= s[i + 1] for i in range(len(s) - 1))

d = [''] + [*range(1000)]  # 394589993
for a in range(10):
    for b in d:
        n = int(f'3{a}458{b}3')
        b = b7(n)
        if dwn(b):
            print(n, sum(map(int, b)))
# 39458583 15
# 39458673 17


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


# https://stepik.org/lesson/698690/step/10?auth=login&unit=698986
from fnmatch import fnmatch
def fn(n):
    d = set()
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            d.add(i)
            d.add(n // i)
    return str(sum(d))

cnt = 0
for n in range(500_000, 600_000):
    d = fn(n)
    if fnmatch(d, '*7?'):
        cnt += 1
        print(n, d)
        if cnt == 5:
            break
# 500001 666672
# 500048 968874
# 500069 500070
# 500079 666776
# 500114 750174
