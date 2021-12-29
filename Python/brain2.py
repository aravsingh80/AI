import sys
import time
from collections import deque
s = sys.argv[1]
s2 = sys.argv[2]
with open(s) as f:
    line_list = [line.strip() for line in f]
    line_list = set(line_list)
with open(s2) as f:
    line_list2 = [line.strip().split() for line in f]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_children(word):
    w = set()
    count = 0
    for x in word:
        for y in letters:
            if y != x:
                w.add(word[0 : count : 1] + y + word[count + 1 : len(word) : 1])
        count += 1
    return w

start = time.perf_counter()
d = dict()
for s in line_list:
    d[s] = get_children(s)
end = time.perf_counter()
s3 = "%s" % (end - start)
print("Time to create the data structure was:", s3, "seconds")
print("There are", len(d), "words in this dict.")
def bfs(startnode, endnode):
    fringe = deque()
    visited = set()
    fringe.append((startnode, 0, [startnode]))
    visited.add(startnode)
    while len(fringe) > 0:
        v, moves, path = fringe.popleft()
        if v == endnode:
            return [moves + 1, path]
        for c in d[v]:
            if c not in visited and c in line_list:
                c_path = path.copy()
                c_path.append(c)
                fringe.append((c, moves + 1, c_path))
                visited.add(c)
    return None

#1 Answer : 1568
# count = 0
# b = False
# for x in line_list:
#     for y in line_list:
#         if x != y:
#             l = bfs(x, y)
#             if l != None:
#                 b = True
#                 break
#     if b == False:
#         count += 1
#     b = False
# print("There are", count, "singletons")
    

def bfs2(startnode):
    fringe = deque()
    visited = set()
    fringe.append((startnode, 0))
    visited.add(startnode)
    while len(fringe) > 0:
        v, moves = fringe.popleft()
        for c in d[v]:
            if c not in visited and c in line_list:
                fringe.append((c, moves + 1))
                visited.add(c)
        if len(fringe) == 0:
            return moves
    return None
s = "abased"
x = bfs2(s)
print(x)
# m = []
# m2 = []
# def bfs3(startnode):
#     fringe = deque()
#     l2 = []
#     count = 1 
#     temp = ""
#     for j in d[startnode]:
#         l2.append(j)
#         if count == 1:
#             temp = j
#     visited = {startnode : temp}
#     fringe.append((startnode, 0))
#     visited2 = []
#     temp = ""
#     count = 1
#     while len(fringe) > 0:
#         v, moves = fringe.popleft()
#         for c in d[v]:
#             if count == 1:
#                 visited[v] = c
#             if c not in visited and c in line_list:
#                 fringe.append((c, moves + 1))
#                 visited[c] = v
#                 if moves == x:
#                     temp = v
#         count += 1
#         if moves == x:
#             m.append(v)
#             visited[v] = "s"
#             visited2.append(visited)
#             visited[v] = temp
#         if len(fringe) == 0:
#             return visited2
#     return None
# def bfs4(startnode, endnode):
#     fringe = deque()
#     visited = set()
#     fringe.append((startnode, [startnode]))
#     visited.add(startnode)
#     while len(fringe) > 0:
#         v, path = fringe.popleft()
#         if startnode == endnode:
#             return path
#         for c in d[v]:
#             if c not in visited and c in line_list:
#                 c_path = path.copy()
#                 c_path.append(c)
#                 fringe.append((c, c_path))
#                 visited.add(c)
#     return None

# max =  0
# i = set()
# for x in line_list:
#     for y in line_list:
#         if x != y:
#             l = bfs(x, y)
#             if l != None:
#                 if len(l) > 2:
#                     i.add(l)
# print(len(i))