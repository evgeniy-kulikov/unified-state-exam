""""""
"""
Task 13
Подготовка к ЕГЭ по информатике. Базовый курс
https://stepik.org/course/123759
"""


from ipaddress import *
# Для узла с IP-адресом 117.191.138.37 адрес сети равен 117.191.136.0
# Чему равно наименьшее возможное значение третьего слева байта маски?
# 136 - 10000101
# 138 - 10001010
for mask in range(32):
    try:
        net = ip_network(f"117.191.136.0/{mask}")
        ip = ip_address("117.191.138.37")
        if ip in net:
            print(net.netmask)
        else:
            print(f"При маске {mask} IP не входит в сеть")
    except:
        # pass
        print(f"Маска {mask} невозможна")



# https://stepik.org/lesson/1276001/step/4?unit=1290302
from ipaddress import *

for mask in range(17, 25):
    net = ip_network(f'213.84.123.45/{mask}', False)
    if "213.84.112.0" in net.exploded:
        print(str(net.netmask).split('.')[2]) # 240
        print(net, net.netmask)
# print(int('11110000', 2))  # 240


# https://stepik.org/lesson/1276001/step/5?unit=1290302
from ipaddress import *

for mask in range(17, 33):
    try:
        net = ip_network(f'127.110.168.0/{mask}')
        print(mask)  # 21
        break
    except:
        pass

# Variant
"""
xxxx-xxxx-10101000-00000000  - net
xxxx-xxxx-11111000-00000000 - mask
xxxx-xxxx-10101010-00010111 - node

2*8 + 5 = 11
"""


# https://stepik.org/lesson/1276001/step/6?unit=1290302
from ipaddress import *

# mask - сколько разрядов слева занимают единицы
for mask in range(1, 33):
    try:
        net = ip_network(f'57.179.192.32/{mask}')
        print(mask - 1)  # 26
        break
    except:
        pass

# Variant
"""
# . # . # . 0000 0000 - net
# . # . # . 1100 0000 - mask
# . # . # . 0010 0000 - node
8 * 3 + 2 = 26
"""


# https://stepik.org/lesson/1276001/step/7?unit=1290302
from ipaddress import *
net = ip_network(f"192.168.1.168/255.255.255.248")
# net = ip_network(f"192.168.1.168/29")
cnt = 0
for el in net:
    ip = bin(int(el))[2:].zfill(32)  # если нужно дополнить нулями слева
    if ip.count("1") % 2 == 0:
        cnt += 1
print(cnt)  # 4
# print(net.num_addresses)  # 8
# print(bin(248)[2:]) # 11111000
# print(bin(255)[2:]) # 11111111


# https://stepik.org/lesson/1276001/step/8?unit=1290302
from ipaddress import *
# net = ip_network(f"192.168.32.0/255.255.240.0")
net = ip_network(f"192.168.32.0/20")
cnt = 0
for el in net:
    ip = bin(int(el))[2:].zfill(32)  # если нужно дополнить нулями слева
    if ip.count("1") % 4 == 0:
        cnt += 1
print(cnt)  # 1056
print(net.num_addresses)  # 4096
# print(bin(240)) # 1111 0000
# print(bin(255)) # 1111 1111


# https://stepik.org/lesson/1276001/step/9?unit=1290302
from ipaddress import *
net = ip_network(f"192.168.32.128/255.255.255.224")
# net = ip_network(f"192.168.32.128/27")
cnt = 0
for el in net:
    ip = bin(int(el))[2:]
    if ip.count("1") < 10:
        cnt += 1
print(cnt)  # 16
# print(net.num_addresses)  # 32
# print(bin(224)) # 1110 0000
# print(bin(255)) # 1111 1111

