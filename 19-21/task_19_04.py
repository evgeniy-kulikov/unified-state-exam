""""""
"""
Task 19-21
ЕГЭ по информатике: варианты
https://stepik.org/course/228948
"""


""" 2.5 тест № 2 (продолжение) """
# https://stepik.org/lesson/1599364/step/6?unit=1621008
# https://stepik.org/lesson/1599364/step/7?unit=1621008
# https://stepik.org/lesson/1599364/step/8?unit=1621008
def fn(st, mv):
    if st >= 67: return not mv % 2
    if mv < 0: return 0
    game = [fn(st + 1, mv - 1), fn(st + 3, mv - 1), fn(st * 2, mv - 1)]
    if not (mv - 1) % 2: return any(game)
    return all(game)

print(*[s for s in range(1, 67) if fn(s, 2)])  # 33
print(*[s for s in range(1, 67) if fn(s, 3) and not fn(s, 1)])  # 30 32
print(min(s for s in range(1, 67) if fn(s, 4)))  # 29

