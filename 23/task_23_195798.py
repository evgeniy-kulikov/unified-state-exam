""""""
"""
Task 23
ЕГЭ информатика 2025. Полный курс
https://stepik.org/course/195798
"""


""" 26.2 Практика (ур. базовый) """
# https://stepik.org/lesson/1229243/step/1?unit=1242784
def f(st,end):
    if st < end:
        return 0
    if st == end:
        return 1
    return f(st-1, end) + f(st // 2, end)

print(f(30,9) * f(9,1))  # 322


def f(st,end):
    if st > end or st == 20:
        return 0
    if st == end:
        return 1
    return f(st+1, end) + f(st+2, end) + f(st*3, end)

print(f(4,10) * f(10,22))  # 715


# https://stepik.org/lesson/1229243/step/4?unit=1242784
def f(st,end):
    if st > end:
        return 0
    if st == end:
        return 1
    return f(st+1, end) + f(st*3, end)

print(f(1,30) * f(30,50) * f(50,150))  # 56




""" 26.3 Практика (ур. усложненный) """
# https://stepik.org/lesson/1229244/step/1?unit=1242785
def f(st,end, fl):
    if st == end:
        return 1
    elif st > end + 1:  # end + 1  т.к. есть команда  st - 1
        return 0
    else:
        if fl:
            return f(st - 1, end, 0) + f(st * 2, end, 1) + f(st * 3, end, 1)
        else:
            return f(st * 2, end, 1) + f(st * 3, end, 1)

print(f(3,15, 1))  # 56


