import string
digs = string.digits + string.ascii_letters


def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[x % base])
        x = x // base

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)


def any_base_to_decimal(number, base):
    return int(number, base)

#print(int2base(66,8))
mult = any_base_to_decimal("66", 8)
#print("mult={}".format(mult))


for i in range(4, 36):
    first = any_base_to_decimal(int2base(i, 8), 8)
    second = any_base_to_decimal("13", i)
    if first * second == mult:
        print(i)
        break

