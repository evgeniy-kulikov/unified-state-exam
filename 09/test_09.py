
# https://stepik.org/lesson/797932/step/9?auth=login&unit=819598
# cnt = 0
# with open('9_2024.txt') as fl:
#     for el in fl:
#         unic, rep = [], []
#         d = dict()
#         ls = list(map(int, el.split()))
#         for n in ls:
#             d.setdefault(n, 0)
#             d[n] += 1
#         rep = [k for k, v in d.items() if v == 2]
#         unic = [k for k, v in d.items() if v == 1]
#         if len(rep) == 2 and len(unic) == 3:
#             if sum(rep) / 2 < sum(ls) / 7:
#                 cnt += 1
# print(cnt)  # 83




