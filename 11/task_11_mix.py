# https://stepik.org/lesson/613839/step/4?unit=609257
# https://alex-math.ru/gia/zadaniye-11-informatika-yege-polyakov-4490
from math import ceil
i = 6  # 62 < 2**6
for n in range(1, 100):
    if ceil(n * i / 8) * 1000 > 4 * 1024:
        print(n - 1) # 5
        break
# N = 62,  n = 5  -> 62 * 62 * 62 * 62 * 62
# Каждая позиция, это 62 варианта символов, а всего позиций 5
# Всех возможных созданных модификаторов может быть 62**5
print(62**5)  # 916132832


