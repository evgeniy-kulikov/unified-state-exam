""" https://kompege.ru/task """

"""
21400 21696 29951 31108 31139 31209 31347 31498
"""



# 21696 ЕГКР 19.04.25 (Уровень: Базовый)
from itertools import *
g = 'hg gc cf fa ae eh fd ed db bh bg'.split()
t = '13_(23) 168 158 578 347 27 456 234'.split()
print(*'12345678')
for p in permutations('abcdefgh'):
    if all(str(p.index(x) + 1) in t[p.index(y)] for x, y in g):
        print(*p)
# 1 2 3 4 5 6 7 8
# a f e b h c g d
# c->g  + h->e  ==  14 + 17  ==  31


# 21400 Досрочная волна 2025 (Уровень: Базовый)
from itertools import permutations
g = 'ab bg ge ef fa fd dc ce da cb'.split()
t = '457 567 45 136 123 247 126'.split()
print(*'1234567')
for p in permutations('abcdefg'):
    if all(str(p.index(x) + 1) in t[p.index(y)] for x, y in g):
        print(*p)
"""
1 2 3 4 5 6 7
c a g e b f d
c f g b e a d
a->b  + e->f  == 18 + 4  == 22
"""



# 29951 Апробация 14.05.26(Уровень: Базовый)
# 29951.gif
from itertools import *
print(*'12345678')
g = 'BH HF FD DC CE EA AB AH GF GC GE'.split()
t = '567 348 278 27 168 15 134 235'.split()
for p in permutations('ABCDEFGH'):
    if all(str(p.index(a) + 1) in t[p.index(b)] for a, b in g):
        print(' '.join(p))
"""
1 2 3 4 5 6 7 8
H C G D A B F E
15 + 11 = 26
"""


# 31108 Основная волна 18.06.26(Уровень: Базовый)
# 31108.gif
from itertools import *
print(*'12345678')
g = 'DA AC CB BH HD GA GC GE FH FE'.split()
t = '258 17 56 68 138 347 26 145'.split()
for p in permutations('ABCDEFGH'):
    if all(str(p.index(a) + 1) in t[p.index(b)] for a, b in g):
        print(' '.join(p))
"""
1 2 3 4 5 6 7 8
G E B D C H F A
G E D B A H F C
5 + 30 = 35
"""


# 31139 Основная волна 19.06.26(Уровень: Базовый)
# 31139.gif
from itertools import *
print(*'1234567')
g = 'DF FA AE EB BG GD CA CF CG'.split()
t = '47 35 246 136 567 345 15'.split()
for p in permutations('ABCDEFG'):
    if all(str(p.index(a) + 1) in t[p.index(b)] for a, b in g):
        print(' '.join(p))
"""
1 2 3 4 5 6 7
E D F A G C B
39 + 13 = 52
"""


# 31209 Резерв 22.06.26(Уровень: Базовый)
# 31209.gif
from itertools import *
print(*'1234567')
g = 'DA AF FB BE ED CB CA CG GD GE'.split()
t = '367 346 124 237 67 125 145'.split()
for p in permutations('ABCDEFG'):
    if all(str(p.index(a) + 1) in t[p.index(b)] for a, b in g):
        print(' '.join(p))
"""
1 2 3 4 5 6 7 8
H G F B A E C D
5 + 3 = 8
"""


# 31347 Пересдача 08.07.26(Уровень: Базовый)
# 31347.gif
from itertools import *
print(*'12345678')
g = 'HA AD DF FB BC CH EH EB EA GF GD'.split()
t = '567 38 248 367 168 145 14 235'.split()
for p in permutations('ABCDEFGH'):
    if all(str(p.index(a) + 1) in t[p.index(b)] for a, b in g):
        print(' '.join(p))
"""
1 2 3 4 5 6 7 8
H G F B A E C D
8 + 5 = 13
"""



# 31498 Демоверсия 2027(Уровень: Базовый)
# 31498.gif
from itertools import *
print(*'123456')
g = 'CB BE EA AF FC DF DE DB'.split()
t = '256 13 245 356 134 14'.split()
for p in permutations('ABCDEF'):
    if all(str(p.index(a) + 1) in t[p.index(b)] for a, b in g):
        print(' '.join(p))
"""
1 2 3 4 5 6
F A E B D C
F C B E D A
21 + 5 = 26
"""
