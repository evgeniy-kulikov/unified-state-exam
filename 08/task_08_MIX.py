# https://stepik.org/lesson/703202/step/8?unit=703535
from itertools import *
c = 0
for p in set(permutations('АББАТИСА')):
    s = ''.join(p)
    s = s.replace('И', 'А')
    s = s.replace('Т', 'Б').replace('С', 'Б')
    c += all(not i in s for i in ('АА', 'ББ'))
print(c)  # 96


# https://stepik.org/lesson/564219/step/5?unit=558467
# ❗❗❗ Чёное в нечёнтной системе счисления не определяется чётностью последнего числа ❗❗❗
from itertools import product
c = 0
for p in product('0123456', repeat=6):
    c +=  p[0] == '4' and not int(''.join(p), 7) % 2
print(c)  # 8404


# https://stepik.org/lesson/564219/step/9?unit=558467
from itertools import product
c = 0
for p in product(range(10), repeat=5):
    if all([p[0], p[-1] in (0, 5),  len(set(p)) == 5]):
        c += all(a%2 != b%2 for a,b in zip(p, p[1:]))
print(c)

# variant
c = 0
for n in range(10000, 100000, 5):
    p = [*map(int, str(n))]
    if len(set(p)) == 5:
        c += all(a%2 != b%2 for a,b in zip(p, p[1:]))
print(c)  # 480


# https://stepik.org/lesson/564219/step/6?unit=558467
from itertools import permutations
c = 0
for p in permutations(range(10), 6):
    if all(a>b for a, b in zip(p, p[1:])):
        c += all(a%2 != b%2 for a, b in zip(p, p[1:]))
print(c)  # 35

