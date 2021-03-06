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
        print("task1={}".format(i))
        break


#171
lst =[]
for i in range(4, 36):
    second = any_base_to_decimal("123", i)
    if second <= 171:
        lst.append(i)
print("task3=[{};{}]".format(min(lst),max(lst)))


print("task5={}".format(2**13))

start = "ABBA"

workstr = start

while len(workstr) <= 40000:
    workstr = workstr.replace("A", "CBC")
    if len(workstr) > 40000:
        break
    workstr = workstr.replace("C", "ABA")
    if len(workstr) > 40000:
        break
print("task10={} {} {}".format(workstr[887], workstr[10000], workstr[50001]))

k=0
for n in range(10,301):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    if res == 15:
        k+=1
print("task12={}".format(k))


v = 384
tmlist=[]
szlist=[]

size = 5
for size in range(1, 384):
    kol = v // size
    rem = v % size
    #print(kol, rem)
    tm = 0.0
    tm_bef = tm
    for i in range(kol):
        tm_bef = tm
        tm += size + 1 # sluj info
        if tm_bef < 60.5 and tm > 60.5:
            tm += size + 1 + 1 # repeat send and check again
        if tm_bef < 116.5 and tm > 116.5:
            tm += size + 1 + 1 # repeat send and check again
        if tm_bef < 337.5 and tm > 337.5:
            tm += size + 1 + 1 # repeat send and check again
        tm += 1  # time 4 check
    tm +=(rem+1)
    tmlist.append(tm)
    szlist.append(size)
    #print(size, tm)
ind = tmlist.index(min(tmlist))
print(szlist[ind], int(min(tmlist)))
