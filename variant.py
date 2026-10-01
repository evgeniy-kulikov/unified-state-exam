# # В стадии решения
# # https://stepik.org/lesson/1400060/step/15?unit=1417013
# # 20970 (Уровень: Средний)
# f = open('26.txt')
# N, K = map(int, f.readline().split())  # кол-во устройств / кол-во мастерских
# d = [[*map(int, i.split())] for i in f]  # время поступления / время ремонта / номер мастерской ((0 любая мастерская)
# s = set(i[2] for i in d)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
# d.sort(key=lambda x: x[0] + x[1])  # по времени завершения работы
# ls = [[] for _ in range(len(s))]
# basket = 0
# for el in d:
#     t1, t2 , m = el
#     if m:  # указана мастерская
#         if len(ls[m]) < 5:  # начальное заполнение очереди в мастерскую
#             ls[m].append(el)
#             ...
#         else:
#             if t1 >= ls[m][-5][0] + ls[m][-5][1]:  # можно встать в очередь
#                 ls[m].append(el)
#             else:
#                 basket += 1
#     else:  # любая мастерская
#         queue = [10]  # длины актуальных очередей  (10 - заглушка на нулевой индекс)
#         for i in range(1, len(ls)):
#             q = 0  # длина очереди
#             for k in range(len(ls[i])):
#                 if t1 >= ls[i][k][0] + ls[i][k][1]:
#                     q += 1
#             queue.append(q)
#         idx = min(queue)
#         if idx < 5:
#             ls[queue.index(idx)].append(el)
#         else:
#             basket += 1
# print(basket)  #
# # 72 218

