# Поиск натурального числа
def fn(n):
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True

# Поиск натуральных делителей числа
def fn(n):
    res = set()
    for i in range(1, int(n ** 0.5) + 1):
        if not n % i:
            res.add(i)
            res.add(n // i)
    return sorted(res)


# число, которое является квадратом другого числа, имеет нечетное количество делителей
# Короче: если квадратный корень числа не имеет дробной части, то это число имеет нечетное количество делителей
for i in range(3, 26):
    if i**0.5 == int(i**0.5):  # далее работаем только стеми числами, которые имеют нечетное количество делителей
        print(i, end=' ')  # 4 9 16 25


# Простое число.
# Число > 1 и не имеет болше других делителей (кроме самого себя)
def fn(n):
    if n == 1: return False
    for i in range (2, int(n**0.5) + 1):
        if not n % i:
            return False
    return True

print(fn(17)) # True
print(fn(18)) # False



# Работать с масками можно с помощью библиотеки fnmatch, встроенной в python.
# https://stepik.org/lesson/870004/step/11?unit=874178
# https://sky.pro/media/kak-rabotat-s-modulem-fnmatch-v-python/
# https://docs-python.ru/standart-library/modul-fnmatch-python/
from fnmatch import fnmatch

mask = '123*45?'
mask = '1[02468]3*4[13579]?'
for i in range(0, 10**10, step):
    if fnmatch(str(i), mask):
        print(i, i // step)
# step - на что должно делиться число,
# mask - какой маске удовлетворять.


""" Наименьшее общее кратное """
# Least Common Multiple (LCM)
# наименьшее натуральное число, которое делится и на «а», и на «b»
a, b = 3, 5

product = a * b
while b:
    a, b = b, a % b
print(product // a)  # 15

def nok(a, b):
    mult = a * b
    while b:
        a, b = b, a % b
    return nult // a
print(nok(a, b))  # 15



""" Перемножить элементы списка """
# Перемножить элементы списка - var 1
from math import prod  # С версии Python 3.8

res = prod([2, 3, 4])  # 24

# Перемножить элементы списка - var 2
from functools import reduce
from operator import mul

res = reduce(mul, [2, 3, 4])  # 24




