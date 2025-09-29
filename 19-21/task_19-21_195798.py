""""""
"""
Task 19-21
ЕГЭ информатика 2025. Полный курс
https://stepik.org/course/195798
"""



""" 24.2 Практика (ур. базовый) """
# https://stepik.org/lesson/1227743/step/1?unit=1241264
def f(a, b, mv):
    if a+b >= 342:
        return not mv % 2
    if not mv:
        return 0
    g = [f(a+2, b, mv-1), f(a*5, b, mv-1), f(a, b+2, mv-1), f(a, b*5, mv-1)]
    # if not (mv - 1) % 2:
    #     return any(g)
    return any(g)

print(min(s for s in range(1, 326) if f(11, s, 2)))  # 14


# https://stepik.org/lesson/1227743/step/2?unit=1241264
def f(a, b, mv):
    if a+b >= 342:
        return not mv % 2
    if not mv:
        return 0
    g = [f(a+2, b, mv-1), f(a*5, b, mv-1), f(a, b+2, mv-1), f(a, b*5, mv-1)]
    if not (mv - 1) % 2:
        return any(g)
    return all(g)

print(*[s for s in range(1, 326) if f(11, s, 3)][:2])  # 57 64



# https://stepik.org/lesson/1227743/step/3?unit=1241264
def f(a, b, mv):
    if a+b >= 342:
        return not mv % 2
    if not mv:
        return 0
    g = [f(a+2, b, mv-1), f(a*5, b, mv-1), f(a, b+2, mv-1), f(a, b*5, mv-1)]
    if not (mv - 1) % 2:
        return any(g)
    return all(g)

print(*[s for s in range(1, 326) if f(11, s, 4) and not f(11, s, 2)])  # 65


# https://stepik.org/lesson/1227743/step/4?unit=1241264
def f(s, mv):
    if s >= 273:
        return not mv % 2
    if not mv:
        return 0
    g = [f(s+2, mv-1), f(s+5, mv-1), f(s*4, mv-1)]
    return any(g)

print([s for s in range(1, 273) if f(s, 2)][0])  # 18


# https://stepik.org/lesson/1227743/step/5?unit=1241264
def f(s, mv):
    if s >= 273:
        return not mv % 2
    if not mv:
        return 0
    g = [f(s+2, mv-1), f(s+5, mv-1), f(s*4, mv-1)]
    if not (mv-1) % 2:
        return any(g)
    return all(g)

print(*[s for s in range(1, 273) if f(s, 3)][:2])  # 17 62


# https://stepik.org/lesson/1227743/step/6?unit=1241264
def f(s, mv):
    if s >= 273:
        return not mv % 2
    if not mv:
        return 0
    g = [f(s+2, mv-1), f(s+5, mv-1), f(s*4, mv-1)]
    if not (mv-1) % 2:
        return any(g)
    return all(g)

print([s for s in range(1, 273) if f(s, 4) and not f(s, 2)][0])  # 60


# https://stepik.org/lesson/1227743/step/7?unit=1241264
# https://stepik.org/lesson/1227743/step/8?unit=1241264
# https://stepik.org/lesson/1227743/step/9?unit=1241264
def f(s, mv):
    if s >= 37:
        return not mv % 2
    if not mv:
        return 0
    g = [f(s+1, mv-1), f(s+2, mv-1), f(s*3, mv-1)]
    if not (mv - 1) % 2:
        return any(g)
    return all(g)

print(*[s for s in range(1, 37) if f(s, 2)])  # 12
print(*[s for s in range(1, 37) if f(s, 3) and not f(s, 1)][:2])  # 4 10
print(*[s for s in range(1, 37) if f(s, 4) and not f(s, 2)])  # 9


# https://stepik.org/lesson/1227743/step/10?unit=1241264
# https://stepik.org/lesson/1227743/step/11?unit=1241264
# https://stepik.org/lesson/1227743/step/12?unit=1241264
def f(a,b, mv):
    if a >= 50 or b >= 50:
        return not mv % 2
    if not mv:
        return 0
    g = [f(a+3, b, mv-1), f(a*2, b, mv-1), f(a, b+3, mv-1), f(a, b*2, mv-1)]
    if not (mv - 1) % 2:
        return any(g)
    return all(g)

print([s for s in range(28) if f(22, s, 2)][0])  # 22
print(*[s for s in range(28) if f(22, s, 3) and not f(22, s, 1)])  # 11 21 (min <> max)
print([s for s in range(28) if f(22, s, 4) and not f(22, s, 2)][-1])  # 18



# https://stepik.org/lesson/1227744/step/1?unit=1241265
# https://stepik.org/lesson/1227744/step/2?unit=1241265
# https://stepik.org/lesson/1227744/step/3?unit=1241265
def f(a,b, mv):
    if a * b >= 455:
        return not mv % 2
    if not mv:
        return 0
    g = [f(a+1, b, mv-1), f(a*2, b, mv-1), f(a, b+1, mv-1), f(a, b*2, mv-1)]
    if not (mv - 1) % 2:
        return any(g)
    return all(g)

# print([s for s in range(1, 91) if f(5, s, 2)][0])  # 23  (return any(g))
print(*[s for s in range(1, 91) if f(5, s, 3) and not f(5, s, 1)][-2:])  # 37 44
print([s for s in range(1, 91) if f(5, s, 4) and not f(5, s, 2)][0])  # 36


# https://stepik.org/lesson/1227744/step/4?unit=1241265
# https://stepik.org/lesson/1227744/step/5?unit=1241265
# https://stepik.org/lesson/1227744/step/6?unit=1241265
def f(a,b,mv):
    if a < 10 or b < 10:
        return not mv % 2
    if not mv:
        return 0
    g = [f(a-1, b, mv-1), f(a-3, b, mv-1), f(a, b-1, mv-1), f(a, b-3, mv-1)]
    if not (mv - 1) % 2:
        return any(g)
    return all(g)

print(*[s for s in range(10,50) if f(s,s,2)])  # 13
print(*[s for s in range(10,50) if f(13,s,3) and not f(13,s,1)])  # 14 16
print(*[s for s in range(10,50) if f(13,s,4) and not f(13,s,2)])  # 15 17


# https://stepik.org/lesson/1227744/step/7?unit=1241265
# https://stepik.org/lesson/1227744/step/8?unit=1241265
# https://stepik.org/lesson/1227744/step/9?unit=1241265
def f(s,mv):
    if s >= 60:
        return not mv % 2
    if not mv:
        return 0
    g = [f(s+1, mv-1), f(s+5, mv-1), f(s*5, mv-1)]
    if not (mv-1) % 2:
        return any(g)
    return all(g)

print([s for s in range(1, 60) if f(s,2)][0])  # 11
print(*[s for s in range(1, 60) if f(s,3)][:2])  # 6 10
print([s for s in range(1, 60) if f(s,4) and not f(s,2)][0])  # 5


# https://stepik.org/lesson/1227744/step/9?unit=1241265
# https://stepik.org/lesson/1227744/step/10?unit=1241265
# https://stepik.org/lesson/1227744/step/11?unit=1241265
def f(a,b,mv):
    if a+b >= 159:
        return not mv % 2
    if not mv:
        return 0
    g = [f(a+1, b, mv-1), f(a+3, b, mv-1), f(a*2, b, mv-1),
         f(a, b+1, mv-1), f(a, b+3, mv-1), f(a, b*2, mv-1)]
    if not (mv-1) % 2:
        return any(g)
    return all(g)

# print([s for s in range(1, 131) if f(7,s,2)][0])  # 38  (return any(g))
print(*[s for s in range(1, 131) if f(7,s,3)][:2])  # 72 74
print([s for s in range(1, 131) if f(7,s,4)][0])  # 71




""" 25.5 Закрепление (ч. 2) """
# https://stepik.org/lesson/1228544/step/9?unit=1242081
""" Задача пока не решенная. """
# Интересное условие. Нужно подумать...
def f(s, mv):
    if s >= 151 and s % 3:
        return not mv % 2
    if not s % 3:
        return 0
    if not mv:
        return 0
    g = [f(s+1 if (s+1)%3 else 0, mv-1),
         f(s+2 if (s+2)%3 else 0, mv-1),
         f(s*2 if (s*2)%3 else 0, mv-1)]
    if not (mv-1) % 2:
        return any(g)
    return all(g)

print([s for s in range(1,150) if f(s, 2) and s % 3])
# print([s for s in range(65,150) if s % 3])