import sys
import time
import random

def numConflicts(state):
    conflicts = 0
    max = []
    for var in range(0, len(state)):
        conflicts2 = 0
        count = 0
        test = state[var]
        for x in state:
            if count != var: 
                 if x == test or abs(count - var) == abs(x - test): conflicts2 += 1
            count += 1
        conflicts += conflicts2
        if var == 0:
            max.append([0, conflicts2])
        else:
            if conflicts2 > max[0][1]:
                max.clear()
                max.append([var, conflicts2])
            if conflicts2 == max[0][1]: max.append([var, conflicts2])
    if len(max) == 1: max2 = max[0][0]
    else:
        max3 = random.choice(max)
        max2 = max3[0]
    temp = state.copy()
    return (int(conflicts / 2), max2)

def minNumConflicts(state, var):
    count = 0
    test = state[var]
    c = 0
    for x in state:
        if count != var:
            if x == test or abs(count - var) == abs(x - test): c += 1
        count += 1
    return c

def findMin(max, state):
    min = []
    temp = state.copy()
    for x in range(0, len(state)):
        temp[max] = x
        c = minNumConflicts(temp, max)
        if len(min) == 0:
            min.append([x, c])
        else:
            if c < min[0][1]:
                min.clear()
                min.append([x, c])
            if c == min[0][1]:
                min.append([x, c])
    if len(min) == 1:
        return min[0][0]
    else:
        m = random.choice(min)
        return m[0]
def goal_test(state):
    c, max = numConflicts(state)
    if c == 0: return True
    else: return False

def csp_incrementalrepair(state):
    x = goal_test(state)
    count = 0
    while x == False:
        count += 1
        c, max = numConflicts(state)
        min = findMin(max, state)
        print(c)
        print(state)
        state[max] = min
        x = goal_test(state)
    print()
    print()
    print("END")
    print()
    print()
    return state

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

s5 = time.perf_counter()
s = []
s3 = []
a = 40
b = 42
# count = 0
# count2 = 0
# start = time.perf_counter()
# solution_list = []
# for x in range(8, 201):
#     s = []
#     count = 0
#     for y in range(0, x):
#         s.append(count)
#         count+=2
#         if count > x - 1:
#             count = 1
#     solution_list.append(csp_incrementalrepair(s))
#     print(solution_list[count2])
#     count2+=1
# end = time.perf_counter()
# print(end-start, "seconds")
    
    
count = 0
for x in range(0, a):
    s.append(count)
    count+=2
    if count > a - 1:
        count = 1
count = 0
for x in range(0, b):
    s3.append(count)
    count+=2
    if count > b - 1:
        count = 1
start = time.perf_counter()
s2 = csp_incrementalrepair(s)
end = time.perf_counter()
t = "%s" % (end - start)
start = time.perf_counter()
s4 = csp_incrementalrepair(s3)
end = time.perf_counter()
t2 = "%s" % (end - start)
e = time.perf_counter()
print(s2, "solved in", t, "seconds")
print(test_solution(s2))
print(s4, "solved in", t2, "seconds")
print(test_solution(s4))
t3 = "%s" % (e - s5)
print("Total time:", t3, "seconds")
