""" https://kompege.ru/task """
"""
17532 
"""


# 17532 Основная волна 07.06.24 (Уровень: Базовый)
def f(a,b,m):
    if a+b >= 65:
        return not m % 2
    if not m:
        return False
    g = [f(a+1, b, m-1), f(a*3, b, m-1), f(a, b+1, m-1), f(a, b*3, m-1)]
    if not (m-1) % 2:
        return any(g)
    return all(g)
    # return any(g)

# print([s for s in range(1, 59) if f(6, s, 2)][0])  # 7
print(*[s for s in range(1, 59) if f(6, s, 3) and not f(6, s, 1)][:2])  # 10 19
print([s for s in range(1, 59) if f(6, s, 4) and not f(6, s, 2)][0])  # 18
"""
7
10 19
18
"""