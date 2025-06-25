# variant 01
from itertools import *
def fn(x,y,w,z):
    return not (y <= (x==z)) and (w <= x)

for a1, a2, a3, a4, a5, a6, a7 in product((0, 1), repeat=7):
    t = [(a1, 0, 0, a2),(0, a3, 0, a4),(a5, 1, a6, a7)]  # строки таблицы
    if len(set(t)) == 3:  # все строки разные
        for p in permutations('xywz'):
            if [fn(**dict(zip(p, r))) for r in t] == [1,1,1]: #  fn({'x': 0, 'y': 0, ...})
                print(p)  # ('z', 'x', 'w', 'y')


# variant 02
print(*'zxwy')
for z,x,w,y in product((0,1), repeat=4):
    f = not (y <= (x==z)) and (w <= x)
    if f: print(z,x,w,y)
# z x w y
# 0 1 0 1
# 0 1 1 1
# 1 0 0 1


# variant 03
print(*'zxwy')
for i in range(2**4):
    z, x, w, y = map(int, f'{i:b}'.zfill(4))
    f = not (y <= (x==z)) and (w <= x)
    if f: print(z,x,w,y)
# z x w y
# 0 1 0 1
# 0 1 1 1
# 1 0 0 1
