import sys
import time
import random
def get_next_unassigned_var(state):
    count = 0
    for x in state:
        if x is None: return count
        count += 1

def checkAvailable(state, var):
    count = 0
    test = state[var]
    for x in state:
        if x != None and count != var:
            if x == test or abs(count - var) == abs(x - test): return False
        count += 1
    return True

def goal_test(state):
    for x in state:
        if x == None: return False
    return True

def get_sorted_values(state, var):
    l = set()
    for x in range(0, len(state)):
        temp = state[0 : var : 1]
        temp.append(x) 
        for y in state[var + 1 : len(state) : 1]: temp.append(y)
        if checkAvailable(temp, var) == True: l.add(x)
    return l

def csp_backtracking(state):
    if goal_test(state): return state
    var = get_next_unassigned_var(state)
    x = get_sorted_values(state, var)
    while len(x) > 0:
        val = random.choice(list(x))
        new_state = state.copy()
        new_state[var] = val
        x.remove(val)
        result = csp_backtracking(new_state)
        if result is not None:
            return result
    return None

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
for x in range(0, 30):
    s.append(None)
for x in range(0, 40):
    s3.append(None)
start = time.perf_counter()
s2 = csp_backtracking(s)
end = time.perf_counter()
t = "%s" % (end - start)
start = time.perf_counter()
s4 = csp_backtracking(s3)
end = time.perf_counter()
t2 = "%s" % (end - start)
e = time.perf_counter()
print(s2, "solved in", t, "seconds")
print(test_solution(s2))
print(s4, "solved in", t2, "seconds")
print(test_solution(s4))
t3 = "%s" % (e - s5)
print("Total time:", t3, "seconds")