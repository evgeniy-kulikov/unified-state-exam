# from string import digits, ascii_uppercase
#
# def conv(num, base):
#     alfa = digits + ascii_uppercase
#     res = ''
#     while num:
#         res = alfa[num % base] + res
#         num //= base
#     return res


# def fn(n):
#     res = ''
#     while n:
#         res = str(n % 4) + res
#         n //= 4
#     return res
""""""
# a = '0123456789abcdefghi'

# https://stepik.org/lesson/894887/step/14?unit=899812
for x in range(2030, 0, -1):
    n = 7**91 + 7**160 - x
    s = ''
    while n:
        s += str(n % 7)
        n //= 7
    if s.count('0') == 70:
        print(x)  # 2029
        break




