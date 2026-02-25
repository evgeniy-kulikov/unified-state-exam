"""var 07"""
# from itertools import *
# from math  import ceil, log2
# from ipaddress import *
# from functools import lru_cache
# from re import *

# 24
from re import *
f = open('24var07.txt').readline()
n = r'(?:0|[1-9]\d*)'
reg = rf'{n}(?:[*-]{n})+'
res = findall(reg, f)
print(len(max(res, key=len)))  # 356