import sys
if sys.argv[1] == "A":
    print(int(sys.argv[2]) + int(sys.argv[3]) + int(sys.argv[4]))
sum = 0
if sys.argv[1] == "B":
    for x in range(2, len(sys.argv)):
        sum += int(sys.argv[x])
    print(sum)
if sys.argv[1] == "C":
    for x in range(2, len(sys.argv)):
        if int(sys.argv[x]) % 3 == 0:
            print(int(sys.argv[x]))
def fibonacci(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x-2)
if sys.argv[1] == "D":
    num = int(sys.argv[2])
    for x in range(1, num + 1):
        print(fibonacci(x))
if sys.argv[1] == "E":
    for x in range(int(sys.argv[2]), int(sys.argv[3]) + 1):
        print(int(x*x) - int(3*x) + 2) 
if sys.argv[1] == "F":  
    tri = [float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])]
    s = "Error"
    if tri[0] + tri[1] <= tri[2]:
        print(s)
    elif tri[0] + tri[2] <= tri[1]:
        print(s)
    elif tri[2] + tri[1] <= tri[0]:
        print(s)
    else:
        nOne = (tri[0] + tri[1] + tri[2]) * 0.5
        area = nOne * (nOne - tri[0]) * (nOne - tri[1]) *  (nOne - tri[2])
        area = area ** 0.5            
        print(area)
if sys.argv[1] == "G": 
    word = sys.argv[2]
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    vowels = "aeiou"
    for x in word:
        if x == "a" or x == "A":
            a += 1
        if x == "e" or x == "E":
            e += 1
        if x == "i" or x == "I":
            i += 1
        if x == "o" or x == "O":
            o += 1  
        if x == "u" or x == "U":
            u += 1 
    print("A: " + str(a))
    print("E: " + str(e))  
    print("I: " + str(i))  
    print("O: " + str(o))  
    print("U: " + str(u))  



