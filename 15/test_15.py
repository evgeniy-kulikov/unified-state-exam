""""""

# # https://stepik.org/lesson/623846/step/3?unit=619531
# # pic_005
#
# d = [*range(155, 178)]
# b = [*range(111, 161)]
# a_min = [*range(100, 200)]
#
# def fn(ls: list):
#     while ls:
#         n = ls.pop()
#         for x in range(1, 1000):
#             f = any([x not in d, x in b, x in ls])
#             if not f:
#                 ls.append(n)
#                 return ls
#
# a_min = fn(a_min)
# a_min.reverse()
# a_min = fn(a_min)
# print(a_min[::-1])  # [161, 162, 163, 164, ..., 175, 176, 177]
# print(len(a_min))  # 17

""""""
# https://stepik.org/lesson/623846/step/6?unit=619531
# pic_008

# a = [*range(60, 91)]
# b = [*range(30, 51)]
# cnt = 30  # 30 чисел дает отрезок A
# for n in range(100):
#     flag = True
#     c = [*range(35, 35 + n)]
#     for x in range(30, 51):
#         # f = x in a or (x in b or x in c)
#         f = x in b or x in c
#         if not f:
#             flag = False
#             break
#     if flag:
#         cnt += 1
#     if cnt == 35:
#         print(35 + n)  # 39
#         break

""""""

# https://stepik.org/lesson/623846/step/10?unit=619531
# def fn(a):  # сокращаем лишние итерации вложенных циклов
#     for x in range(1, 500):
#         for y in range(1, 500):
#             f = (3 * y - x > a) or (2 * x + 3 * y < 30) or (2 * y - x < -31)
#             if not f:
#                 return False
#     return True


# https://stepik.org/lesson/623846/step/12?unit=619531
# for a in range(1, 1000):
#     flag = True
#     for x in range(1, 100000):
#         # f = not ((x % a == 0) and (x % 36 == 0)) or (x % 324 == 0 and a > 100)
#         f = x % a or x % 36 or (not x % 324 and a > 100)
#         if not f:
#             flag = False
#             break
#     if flag:
#         print(a)  # 162
#         break



#  https://stepik.org/lesson/667646/step/1?unit=668403
# pic_010.jpg



# print(bin(0b1000100 - 0b1011)[2:])
# print(oct(0o457 + 0o73)[2:])
# print(hex(0x75d010 - 0x75ceb8)[2:].upper())

# print(oct(int(0xaf9e)))