# print(*'zyxw')
# for i in range(16):
#     b = bin(i)[2:].zfill(4)
#     z,y,x,w = map(int, b)
#     if not (((x <= y) == (z <= w)) or x * w):
#         print(z,y,x,w)

# https://stepik.org/lesson/421642/step/2?unit=411296

# https://stepik.org/lesson/421642/step/5?unit=411296
print(*'cab')
for i in range(2 ** 3):
    c,a,b = map(int, bin(i)[2:].zfill(3))
    # if (a and not c) or (not a and b and c):
    if not ((a and not c) or (not a and b and c)):
        print(c,a,b)




