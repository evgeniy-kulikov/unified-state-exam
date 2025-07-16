""" https://kompege.ru/task """

# 21696 ЕГКР 19.04.25 (Уровень: Базовый)
from itertools import *
g = 'hg gc cf fa ae eh fd ed db bh bg'.split()
t = '23 168 158 578 347 27 456 234'.split()
print(*'12345678')
for p in permutations('abcdefgh'):
    if all(str(p.index(x) + 1) in t[p.index(y)] for x, y in g):
        print(*p)
# 1 2 3 4 5 6 7 8
# a f e b h c g d
# c->g  + h->e  ==  14 + 17  ==  31


# № 21400 Досрочная волна 2025 (Уровень: Базовый)
from itertools import permutations
g = 'ab bg ge ef fa fd dc ce da cb'.split()
t = '457 567 45 136 123 247 126'.split()
print(*'1234567')
for p in permutations('abcdefg'):
    if all(str(p.index(x) + 1) in t[p.index(y)] for x, y in g):
        print(*p)
# 1 2 3 4 5 6 7
# c a g e b f d
# c f g b e a d
# a->b  + e->f  == 18 + 4  == 22