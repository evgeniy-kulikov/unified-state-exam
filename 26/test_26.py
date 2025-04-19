
# https://stepik.org/lesson/666351/step/9?unit=664354
with open('26_3_p1.txt') as fl:
    ls = []
    place = int(fl.readline())
    user = int(next(fl).strip())
    for el in fl:
        ls.append(list(map(int, el.split())))
    ls.sort()
    pass

