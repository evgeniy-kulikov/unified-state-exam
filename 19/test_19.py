
# https://stepik.org/lesson/765361/step/6?unit=767587
def fn(stn, mv, w=eval('all')):
    if stn >= 29: return not mv % 2
    if not mv: return 0
    rules = [fn(stn + 1, mv - 1), fn(stn * 2, mv - 1)]
    if not (mv - 1) % 2: return any(rules)
    return w(rules)

print(min([s for s in range(1, 29) if fn(s, 1)]), end=' ')  # 15
print(min(s for s in range(1, 29) if fn(s, 2)), end=' ')  # 14
print(min([s for s in range(1, 29) if fn(s, 3) and not fn(s, 1)]), end=' ')  # 7
print(max([s for s in range(1, 29) if fn(s, 3) and not fn(s, 1)]), end=' ')  # 13
print(min([s for s in range(1, 29) if fn(s, 4)]))  # 12
# 15 14 7 13 12

