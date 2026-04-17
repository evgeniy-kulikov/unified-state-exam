# https://stepik.org/lesson/703202/step/8?unit=703535
from itertools import *
c = 0
for p in set(permutations('АББАТИСА')):
    s = ''.join(p)
    s = s.replace('И', 'А')
    s = s.replace('Т', 'Б').replace('С', 'Б')
    c += all(not i in s for i in ('АА', 'ББ'))
print(c)  # 96


