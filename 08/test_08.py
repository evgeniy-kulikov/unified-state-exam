
# https://stepik.org/lesson/1107347/step/3?unit=1118585
# Не решено!!!!
# from itertools import permutations
# from re import findall

#  362880  всего вариантоа
# reg = r'[АИЯ]{3}.*[НТС]{3}|[НТС]{3}.*[АИЯ]{3}'  #  276480
# reg = r'[АИЯ]{3,}.*[НТС]{3,}.*|.*[НТС]{3,}.*[АИЯ]{3,}'  #  276480
# reg = r'[АИЯ]{3}[НТС]{3}|[НТС]{3}[АИЯ]{3}'  # 293760
# reg = r'[АИЯ]{3}[НТС]{3}'  #  328320
# reg = r'[НТС]*[АИЯ]{3}[НТС]{3}[АИЯ]*'  #  328320
# reg_1 = r'[НТС]{3}'  #
# reg_2 = r'[АИЯ]{3}'  #  276480
# reg = r'[^АИЯ][АИЯ]{3}[НТС]{3}[^НТС]'  #  328320
# cnt = 0
# for p in permutations('АНАСТАСИЯ'):
#     st = ''.join(p)
#     if  not all([findall(reg_1, st), findall(reg_2, st)]):
#     if  not findall(reg, st):
#         cnt += 1
# print(cnt)  # 276480



# def fn(n):
#     s = ''
#     while n:
#         s = str(n % 5) + s
#         n //= 5
#     return all([len(s) == 6, s[0] == '3', not int(s, 5) % 2])
# cnt = 0
# for n in range(3 * 5 ** 5, 4 * 5 ** 5):
#     # cnt += fn(n)
# print(cnt)  # 1562


# from itertools import product
# import re
# reg = r'[КСН]{0,1}[ЕИЯ]{2,}'
# cnt = 0
# for i in range(3, 8):
#     for p in product('КСЕНИЯ', repeat=i):
#         p = ''.join(p)
#         if re.fullmatch(reg, p):
#             cnt += all([p.count('Е') < 3, p.count('И') < 3, p.count('Я') < 3])
# print(cnt)  # 1059

# https://stepik.org/lesson/552237/step/9?unit=545965
# http://lavinova8.ru/gotovimsja-k-egje/zadanie-8-kombinatorika.html
# from itertools import product
# import re
# reg = r'[МАРИ]{4}[ИНА]{4}'
# ls = []
#
# for p in product('МАРИНА', repeat=8):
#     p = ''.join(p)
#     if re.fullmatch(reg, p) and len(set(p[:4])) == 4:
#         ls += [p]
# ls.sort()
# print(ls.index('МАРИАННА') + 1)  # 6897
# print(len(ls)) # 12288
# print(ls[6896])  # МАРИАННА
# print(ls[0])  # АИМРАААА
# print(ls[-1])  # РМИАНННН
""""""



# https://stepik.org/lesson/424708/step/6?auth=login&unit=414440
from itertools import product
import re
cnt = 0
reg = r'[г][^г]{3}|[^г]{3}[г]'
for p in product('абвгде', repeat=4):
    f = ''.join(p)
    if re.findall(reg, f):
        cnt += 1
print(cnt) # 250
