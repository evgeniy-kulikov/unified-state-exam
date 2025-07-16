"""
Task 19
Подготовка к ЕГЭ по информатике. Базовый курс.
https://stepik.org/course/123759
"""

# https://stepik.org/lesson/775990/step/9?unit=778436
def fn(a, b, mv, w=eval('all')):
    if a + b >= 255: return not mv % 2
    if not mv: return 0
    rules = [fn(a + 1, b, mv - 1), fn(a * 2, b, mv - 1), fn(a, b + 1, mv - 1), fn(a, b * 2, mv - 1)]
    if not (mv - 1) % 2:
        return any(rules)
    return w(rules)

print(min([s for s in range(1, 238) if fn(17, s, 2, w=eval('any'))]))  # 60
print(*([s for s in range(1, 238) if fn(17, s, 3) and not fn(17, s, 1)]))  # 110 118
print(min([s for s in range(1, 238) if fn(17, s, 4) and not fn(17, s, 2)]))  # 109