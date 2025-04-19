""""""

"""

ip_address(address)
Take an IP string/int and return an object of the correct type.

ip_network(address, strict=True):
Take an IP string/int and return an object of the correct type.

ip_network(address).network_address
формирование IP адреса (маски в записи нет)


ip_network(address).hosts()
Generate Iterator over usable hosts in a network. 
it doesn't return the network or broadcast addresses

"""
"""
'11'.ljust(8, '0')  -->  '11000000'

'11'.rjust(8, '0')  -->  '00000011'
'11'.zfill(8)  -->  '00000011'
"""