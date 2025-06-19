""""""
"""
Task 14
ЕГЭ по информатике: варианты
https://stepik.org/course/228948
"""


""" 2.5 тест № 2 (продолжение) """
# https://stepik.org/lesson/1599364/step/1?unit=1621008
def fn(n):
    r = ''
    while n:
        r += str(n % 6)
        n //= 6
    return r[::-1]

m = 6**260 + 6**160 + 6**60
for n in range(2030, 0, -1):
    if fn(m - n).count('0') == 202:
        print(n)  # 1944
        break

