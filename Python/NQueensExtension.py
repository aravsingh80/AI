import time
start = time.perf_counter()
solutionList = []
def swap(l2, x, y):
    temp = l2[x]
    l2[x] = l2[y]
    l2[y] = temp
def moveToEnd(l2, x):
    l3 = l2[0 : x : 1]
    l4 = l2[x + 1: len(l2) : 1]
    for x2 in l4: l3.append(x2)
    l3.append(l2[x])
    l2 = l3
    return l2
for x in range(8, 201):
    if x % 6 != 2 and x % 6 != 3:
       l = []
       for y in range(1, x, 2): l.append(y)
       for y in range(0, x, 2): l.append(y)
       solutionList.append(l)
    else:
       even = []
       odd = []
       for y in range(1, x, 2): odd.append(y)
       for y in range(0, x, 2): even.append(y)
       if x % 6 == 2:
           swap(even, 0, 1)
           even = moveToEnd(even, 2)
       if x % 6 == 3:
           odd = moveToEnd(odd, 0)
           even = moveToEnd(even, 0)
           even = moveToEnd(even, 0)
       for x2 in even:
           odd.append(x2)
       solutionList.append(odd)
def test_solution(state):
    for var in range(len(state)):
        left = state[var]
        middle = state[var]
        right = state[var]
        for compare in range(var + 1, len(state)):
            left -= 1
            right += 1
            if state[compare] == middle:
                print(var, "middle", compare)
                return False
            if left >= 0 and state[compare] == left:
                print(var, "left", compare)
                return False
            if right < len(state) and state[compare] == right:
                print(var, "right", compare)
                return False
    return True
count = 0
for x in solutionList:
    print(x)
    print(test_solution(x))
end = time.perf_counter()
print("Time to solve and print:", end - start, "seconds")

