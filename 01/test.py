
# # https://stepik.org/lesson/983014/step/2?unit=990285
# from itertools import permutations
# g = {'А': 'БВГ', 'Б': 'АВЕЖ', 'В': 'БАГ', 'Г': 'АВЕД', 'Д': 'ГЕ', 'Е': 'ЖБГД', 'Ж': 'БЕ'}
# t = '0110100' + '1011001' + '1100100' + '0100001' + '1010011' + '0000101' + '0101110'
# # print(*range(1,8))
# print(*'1234567')
# for p in permutations(g):
#     tn = ''
#     for x in p:
#         for y in p:
#             if y in g[x]:
#                 tn += '1'
#             else:
#                 tn += '0'
#     if tn == t:
#         print(*p)
# # А Б В Ж Г Д Е
# # А Г В Д Б Ж Е
# # В Б А Ж Г Д Е
# # В Г А Д Б Ж Е
# # 26
#
# """ Не сработало!!!"""
# # https://stepik.org/lesson/983014/step/2?unit=990285
# from itertools import permutations
# g = 'БВГ АВЕЖ БАГ АВЕД ГЕ ЖБГД БЕ'
# t = '235 1347 125 27 1367 57 2456'
# num = '1234567'
# head = 'АБВГДЕЖ'
# print(*num)
# g_main = {frozenset(i) for i in g.split()}
# for p in permutations(head):
#     g_repl = t
#     for x, y in zip(num, head):
#         g_repl = g_repl.replace(x, y)
#     g_repl = {frozenset(k) for k in g_repl.split()}
#     if g_main == g_repl:
#         f = 1
#         print(*p)

#
# # https://stepik.org/lesson/983017/step/2?unit=990288
# from itertools import permutations
# g = 'БД ГВА ГБД БВЕК АВЕК ГКД ГЕД'
# t = '2457 136 2567 16 137 234 135'
# head = 'АБВГДЕК'
# num = '1234567'
# print(*num)
# g_set = {frozenset(i) for i in g.split()}
#
# for p in permutations(head):
#     g_per = t
#     for x, y in zip(num, p):
#         g_per = g_per.replace(x , y)
#     g_per = {frozenset(i) for i in g_per.split()}
#     if g_set == g_per:
#         print(*p)
#
# from itertools import permutations
# g = {'А': 'БД', 'Б': 'ГВА', 'В': 'БГД', 'Г': 'БВЕК', 'Д': 'АВЕК', 'Е': 'ГДК', 'К': 'ГЕД'}
# t = '0101101' + '1010010' + '0100111' + '1000010' + '1010001' + '0111000' + '1010100'
# # print(*range(1,8))
# print(*'1234567')
# for p in permutations(g):
#     tn = ''
#     for x in p:
#         for y in p:
#             if y in g[x]:
#                 tn += '1'
#             else:
#                 tn += '0'
#     if tn == t:
#         print(*p)
# # 1 2 3 4 5 6 7
# # Д В Г А Е Б К
# # Д В Г А К Б Е


# rom itertools import permutations


# 110 answer

# https://stepik.org/lesson/1095501/step/1?unit=1106259

# https://stepik.org/lesson/1095501/step/2?unit=1106259
# from itertools import permutations
# g = 'БВ АВ АБДКГ ВК ВЕ ДК ЕВГ'
# t = '56 47 46 236 16 13457 26'
# g = {frozenset(i) for i in g.split()}
#
#
# print(*'1234567')
# for p in permutations('АБВГДЕК'):
#     tp = t
#     for i in range(7):
#         tp = tp.replace(str(i + 1), p[i])
#     tp = {frozenset(i) for i in tp.split()}
#     if tp == g:
#         print(*p)
# 1 2 3 4 5 6 7
# А Е Г К Б В Д
# Б Е Г К А В Д
# 25

# https://stepik.org/lesson/262340/step/1?unit=243232

# https://stepik.org/lesson/262340/step/3?unit=243232
from itertools import permutations
print(*'1234567')
g = 'БВ АВД АБДЕГ ВЕК БВЕ ДВГК ГЕ'
t = '24 146 567 1267 36 23457 346'
g = {frozenset(i) for i in g.split()}

for p in permutations('АБВГДЕК'):
    tmp = t
    for i in range(7):
        tmp = tmp.replace(str(i + 1), p[i])
    tmp = {frozenset(i) for i in tmp.split()}
    if g == tmp:
        print(*p)
# 1 2 3 4 5 6 7
# К Г Б Е А В Д
# 11

