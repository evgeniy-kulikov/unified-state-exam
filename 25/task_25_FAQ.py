# Работать с масками можно с помощью библиотеки fnmatch, встроенной в python.
# https://stepik.org/lesson/870004/step/11?unit=874178
# https://sky.pro/media/kak-rabotat-s-modulem-fnmatch-v-python/
# https://docs-python.ru/standart-library/modul-fnmatch-python/
from fnmatch import fnmatch

mask = '123*45?'
mask = '1[02468]3*4[13579]?'  # учесть четность / нечётность разряда
step = 1  # или больше
for i in range(0, 10**10, step):
    if fnmatch(str(i), mask):  # True or False
        print(i, i // step)
# step - на что должно делиться число,
# mask - какой маске удовлетворять.

"""
У нечетного числа не может быть четных делителей.
Все делители нечетного числа также будут нечетными. 15 --> 1, 3, 5, 15

У Четного числа могут быть делители разной четности.  6 -->  1, 2, 3, 6

нетривиальными считаются все делители, кроме 1 и самого числа


Простое число — это натуральное число больше единицы, которое имеет ровно два делителя: 1 и само себя. 
Например, 2, 3, 5, 7 — простые числа, поскольку они делятся только на 1 и на самих себя. 
Число 1 не является простым, а числа, имеющие более двух делителей, называются составными (например, 4, 6)

Простые множители числа — это простые числа (делители, которые делятся только на 1 и на самих себя, 
например 2, 3, 5, 7, 11...), 
которые при перемножении дают исходное число.


Если сумма чисел числа делится на 3, то и само число делится на 3  --> 174 (1+7+4 = 12)  174 / 3 = 58


Каждое число можно представить произведением простых чисел
Разложение чисел на простые множители:
https://tetrika-school.ru/blog/razlozhenie-chisel-na-prostye-mnozhiteli/
https://skysmart.ru/articles/mathematic/razlozhenie-chisel-na-prostye-mnozhiteli
"""


# Поиск натурального числа (простое число)
def fn(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False  # 0
    return True  # 1

# короче
def fn(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))

# Поиск натуральных делителей числа
def fn(n):
    res = set()
    for i in range(1, int(n ** 0.5) + 1):
        if not n % i:
            res.add(i)
            res.add(n // i)
            # res |= {i, n // i}  # короче
    return res

# Поиск натуральных минимальных и максимальных делителей числа (кроме 1 и самого числа)
def fn(num):
    for i in range(1, int(num ** 0.5) + 1):
        if not num % i:
            return i, num // i


# число, которое является квадратом другого числа, имеет нечетное количество делителей
# Короче: если квадратный корень числа не имеет дробной части, то это число имеет нечетное количество делителей
for i in range(3, 26):
    if i**0.5 == int(i**0.5):  # далее работаем только с теми числами, которые имеют нечетное количество делителей
        print(i, end=' ')  # 4 9 16 25


# Простое число.
# Число > 1 и не имеет больше других делителей (кроме самого себя)
def fn(n):
    if n == 1: return False
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            return False
    return True

print(fn(17)) # True
print(fn(18)) # False

def prime(n, p=2):
    """поиск простых делителей среди всех делителей числа"""
    for i in range(p, int(n**0.5 + 1)):
        if not n % i:
            return [i] + prime(n // i, i)
    return [n]  # само число простой делитель

def f(n):
    res = set()
    for i in range(2, int(n ** 0.5 + 1)):
        if not n % i:
            res |= {i, n // i}
    return res

print(f(12))  # {2, 3, 4, 6}
print(set(prime(12)))  # {2, 3}






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
    return mult // a
print(nok(a, b))  # 15



""" Перемножить элементы списка """
# Перемножить элементы списка - var 1
from math import prod  # С версии Python 3.8

res = prod([2, 3, 4])  # 24

# Перемножить элементы списка - var 2
from functools import reduce
from operator import mul

res = reduce(mul, [2, 3, 4])  # 24




