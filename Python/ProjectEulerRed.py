#Red
#12
def num_of_divisors(x):
    s = set()
    for y in range(1, int(x ** 0.5) + 1):
        if x % y == 0:
            s.add(y)
            s.add(x // y)
    return len(s)
i = False
i2 = 1
i3 = 1
while i == False:
    if num_of_divisors(i3) > 500:
        i = True
        break
    i2 += 1
    i3 += i2
print(i3)

#14
maxlen = 0
max = 1
for x in range(1, 1000001):
    y = []
    y.append(x)
    temp = x
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = (3 * x) + 1
        y.append(x)
    if len(y) > maxlen:
        maxlen = len(y)
        max = temp
print(max)

#17
digits = {0: 0, 1 : 3, 2 : 3, 3 : 5, 4 : 4, 5 : 4, 6 : 3, 7 : 5, 8 : 5, 9 : 4}
placevaluetens = {0: 0, 1 : 4, 2 : 6, 3 : 6, 4 : 5, 5 : 5, 6 : 5, 7 : 7, 8 : 6, 9 : 6}
sum2 = 0
for x in range(1, 1001):
    if len(str(x)) == 1:
        sum2 += digits[x]
    elif len(str(x)) == 2:
        x2 = int((str(x))[1])
        x3 = int((str(x))[0])
        temp = x
        if temp == 10:
            sum2 += 3
        elif temp == 11:
            sum2 += 6
        elif temp == 12:
            sum2 += 6
        elif temp == 13:
            sum2 += 8
        elif temp == 15:
            sum2 += 7
        elif temp == 18:
            sum2 += 8
        else:
            sum2 += digits[x2]
            sum2 += placevaluetens[x3]
    elif len(str(x)) == 3:
        x2 = int((str(x))[2])
        x3 = int((str(x))[1])
        x4 = int((str(x))[0])
        temp = int((str(x))[1:])
        if temp == 10:
            sum2 += 3
        elif temp == 11:
            sum2 += 6
        elif temp == 12:
            sum2 += 6
        elif temp == 13:
            sum2 += 8
        elif temp == 15:
            sum2 += 7
        elif temp == 18:
            sum2 += 8
        else:
            sum2 += digits[x2]
            sum2 += placevaluetens[x3]
        if digits[x2] == 0 and placevaluetens[x3] == 0:
            sum2 += 7 + digits[x4]
        else:
            sum2 += 10 + digits[x4]
    else:
        sum2 += 11
print(sum2)

#21
def sumdivisors(x):
    s = set()
    for y in range(1, int(x ** 0.5) + 1):
        if x % y == 0:
            if y != x:
                s.add(y)
            if (x // y) != x:
                s.add(x // y)
    return sum(s)
print(sum({x for x in range(1, 10000) if sumdivisors(sumdivisors(x)) == x and x != sumdivisors(x)}))

#28
sum2 = 1
for x in range(3, 1002, 2):
    y = x ** 2
    y2 = (((x - 1) ** 2) + 1)
    sum2 += y + y2 + (y - x + 1) + (y2 - x + 1)
print(sum2)

#30
sum3 = 0
for x in range(2, 1000000):
    sum2 = 0
    for y in str(x):
        sum2 += ((int(y)) ** 5)
    if sum2 == x:
        sum3 += x
print(sum3)

