""""""
"""
Task 08
Подготовка к ЕГЭ по информатике
https://stepik.org/course/72713/syllabus
"""



# https://stepik.org/lesson/373149/step/5?unit=360764
from itertools import *
cnt = 0
for p in product('ABCX', repeat=5):
    if 'X' not in p[1:]:
    # if not p.count('X') or (p[0] == 'X' and p.count('X') == 1):
        cnt += 1
print(cnt)   # 324


# https://stepik.org/lesson/546210/step/15?unit=539831
from itertools import *
cnt = 0
for p in product(sorted('СВЕТА'), repeat=5):
    if p.count('В') == 1:
        cnt += 1
        if not p.count('А'):
            print(cnt)  # 20
            break



# https://stepik.org/lesson/450409/step/5?unit=440851
from itertools import *
cnt = 0
for p in product(range(8), repeat=5):
    if p[0] and len(set(p)) == 5:
        cnt += all(x%2 != y%2 for x, y in(zip(p,p[1:])))
print(cnt)  # 504


# https://stepik.org/lesson/450409/step/14?unit=440851
from itertools import *
cnt = 0
for p in permutations((1,3,5,7,0,2), 4):  # 4 согласных, 2 гласных
    cnt += all(x%2 != y%2 for x, y in(zip(p,p[1:])))
print(cnt)  # 48


# https://stepik.org/lesson/546720/step/12?unit=540350
from itertools import *
cnt = 0
for p in permutations(range(10), 6):
    if p[0] and p[-2:] == (2, 6):
        cnt += sum(i%2 for i in p) in (2, 3)  # 👍 ✅ 👍
print(cnt)  # 1260


# https://stepik.org/lesson/661017/step/15?unit=658966
from itertools import *
c = 0
for p in permutations('nadpis#', 7):
    c += p[0] != '#' and '#ia' not in ''.join(p)
print(c)  # 4224



