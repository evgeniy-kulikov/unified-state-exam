# https://stepik.org/lesson/1670114/step/14?unit=1693136
from math import dist

# определение центроида кластера
def centroid(cl):
    res = []
    for i in cl:
        res.append((sum(dist(i, k) for k in cl), i))
    return min(res)[-1]

# Три кластера разделены прямыми x = 8 и y = 0.5 и y = 9.5 - x
with open('add/course_100138/27-20b.txt') as fl:
    data = [tuple(map(float, i.replace(',', '.').split())) for i in fl]
    clasters = [[] for _ in range(3)]
    for i in data:
        if i[1] > 0.5 and i[0] < 8:
            clasters[0].append(i)
        elif i[1] > 9.5 - i[0]:
            clasters[1].append(i)
        else:
            clasters[2].append(i)

res = [centroid(i) for i in clasters]

cx = int(sum(i[0] for i in res) / 3 * 10_000)
cy = int(sum(i[1] for i in res) / 3 * 10_000)
print(cx, cy)  # 81775 7384

