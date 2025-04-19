# from math import log2, ceil
#

# https://stepik.org/lesson/648384/step/1?auth=login&unit=645015
from math import log2, ceil
I_1 = ceil(log2(26)) * 15  # 75 bit
I_2 = ceil(log2(9999))  # 14 bit
I_id = ceil((I_1 + I_2) / 8) # 12 byte
res = int(1600 / (I_id + 12))
print(res)  # 66 user






