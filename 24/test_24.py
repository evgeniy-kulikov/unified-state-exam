# https://stepik.org/lesson/1688395/step/6?unit=1711683
from re import *
with open('add/course_100138/24-300.txt') as fl:
    f = fl.read()

num = '([1-9]\d*|0)'  # НЕотрицательное число (ноль или положительное)
mul = f'(({num}\*)*0(\*{num})*)'  # Произведение чисел, среди которых ОБЯЗАТЕЛЬНО есть ноль
reg = rf'{mul}(\+{mul})*'  # сумма из произведений, равных нулю (либо только произведение равное нулю)

res = 0
for i in finditer(reg, f):
    res = max(res, len(i.group()))
print(res)  # 126

