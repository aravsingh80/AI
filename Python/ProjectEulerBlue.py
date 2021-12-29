import sys
#Blue
def is_prime(x):
    count = 0
    if x > 1:
        if x == 2:
            return True
        for y in range(3, round(x ** 0.5) + 1, 2):
            if x % y == 0:
                count = 1
                break
    else:
        return False
    if count == 0:
        if x % 2 == 1:
            return True
        else:
            return False
    else:
        return False

#1
print(sum({x for x in range(1000) if x % 3 == 0 or x % 5 == 0}))

#2
def fibonacci(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x-2)
def fibonacci(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x-2)
sum2 = 0
over = False
for x in range(1, 4000000):
    y = fibonacci(x)
    if y % 2 == 0:
        if y > 4000000: 
            over = True
        else:
            sum2 += y
    if over == True:
        break
print(sum2)

#3
if is_prime(600851475143) == True:
    print(600851475143)
else:
    x = []
    y = 600851475143
    count = 2
    while is_prime(y) == False:
        if y % count == 0:
            y = y // count
            x.append(count)
            count = 2
        else:
            count += 1
            while is_prime(count) == False:
                count += 1
    x.append(y)
    print(max(x))

#4
pal = 0
for x in range(100, 1000):
    for y in range(100, 1000):
        z = x * y
        if str(z) == str(z)[::-1]:
            if z > pal:
                pal = z
print(pal)

#5
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
product = 1
for x in range(1, 20):
    x = x // gcd(product, x)
    product *= x
print(product)

#6
print(int(sum([x for x in range(1, 101)]) ** 2) - int(sum([x**2 for x in range(1, 101)])))

#7 
count2 = 0
x2 = 1
while count2 < 10001:
    x2 += 1
    if is_prime(x2):
        count2 += 1
print(x2)

#8
x = str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
y = 13
max2 = 0
while y < 1000:
    m = 1
    s = x[y - 13: y: 1]
    for h in s:
        m *= int(h)
    if m > max2:
        max2 = m
    y += 1
print(max2)

#9
def pythagorean(x, y, z):
    if (x**2) + (y**2) == (z**2):
        return True
prod = False
for x in range(1, 999):
    for y in range(1, 999):
        for z in range(1, 999):
            if x + y + z == 1000 and pythagorean(x, y, z) == True:
                    print((x*y*z))
                    prod = True
            if prod == True:
                break
        if prod == True:
            break
    if prod == True:
        break

#29
print(len({a ** b for a in range(2, 101) for b in range(2, 101)}))
