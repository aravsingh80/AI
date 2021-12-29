import sys; args = sys.argv[1:]
height = int(args[0][0: args[0].index("x")])
width = int(args[0][args[0].index("x") + 1:])
requirement = int(args[1])
s = ""
def checkLegal(puzzle):
    rows = []
    columns = []
    count = 0
    for x in range(0, height):
        row = []
        for y in range(0, width): 
            row.append([puzzle[count], count])
            count += 1
        rows.append(row)

    for y in range(0, width):
        column = []
        count = y
        for y in range(0, height): 
            column.append([puzzle[count], count])
            count += width
        columns.append(column)
    
    dataStruct = dict()
    for x in range(0, len(puzzle)): 
        if puzzle[x] != "#": dataStruct[x] = 0

    for x in rows:
        count = 0
        for y in x:
            if y[0] != "#": count += 1
            else:
                if count >= 3: 
                    for x2 in range(1, count): dataStruct[y[1] - x2] += 1
                count = 0
        if count >= 3: 
            for x2 in range(0, count): dataStruct[x[len(x) - 1][1] - x2] += 1

    for x in columns:
        count = 0
        for y in x:
            if y[0] != "#": count += 1
            else:
                if count >= 3: 
                    for x2 in range(1, count): dataStruct[y[1] - (width * x2)] += 1
                count = 0
        if count >= 3: 
            for x2 in range(0, count): dataStruct[x[len(x) - 1][1] - (width * x2)] += 1

    for x in dataStruct.values():
        if x == 0: return False
    
    for x in range(0, len(puzzle)):
        if puzzle[x] != "#":
            activeSpaces = 0
            count = 0
            if x - 1 >= 0: 
                if puzzle[x - 1] == "#": count += 1
                activeSpaces += 1
            if x + 1 < (int(x / width) + 1) * width: 
                if puzzle[x + 1] == "#": count += 1
                activeSpaces += 1
            if x - width >= 0: 
                if puzzle[x - width] == "#": count += 1
                activeSpaces += 1
            if x + width < len(puzzle): 
                if puzzle[x + width] == "#": count += 1
                activeSpaces += 1
            if count == activeSpaces and count != 0: return False
            if x - 1 >= 0 and x - width >= 0 and puzzle[x - 1] == "#" and puzzle[x - width] == "#":
                if puzzle[x - width - 1]  != "#": return False
            if x - 1 >= 0 and x + width < len(puzzle) and puzzle[x - 1] == "#" and puzzle[x + width] == "#":
                if puzzle[x + width - 1]  != "#": return False
            if x + 1 < (int(x / width) + 1) * width and x - width >= 0 and puzzle[x + 1] == "#" and puzzle[x - width] == "#":
                if puzzle[x - width + 1]  != "#": return False
            if x + 1 < (int(x / width) + 1) * width and x + width < len(puzzle) and puzzle[x + 1] == "#" and puzzle[x + width] == "#":
                if puzzle[x + width + 1]  != "#": return False

    return True

def get_children(puzzle): return {puzzle[0: x: 1] + "#" + puzzle[x + 1: len(puzzle): 1] for x in range(0, len(puzzle)) if puzzle[x] == "-" and checkLegal(puzzle[0: x: 1] + "#" + puzzle[x + 1: len(puzzle): 1])}

def getBlockCount(puzzle):
        blockCount = 0
        for x in puzzle:
            if x == "#": blockCount += 1
        return blockCount

def bfs(startnode):
    fringe = []
    visited = set()
    fringe.append((startnode, [startnode]))
    visited.add(startnode)
    v = startnode
    while len(fringe) > 0 and getBlockCount(v) <= requirement:
        v, path = fringe[0]

        # count = 0
        # for x in range(0, height):
        #     s2 = ""
        #     for y in range(0, width): 
        #         s2 += v[count] + " "
        #         count += 1
        #     print(s2)
        # print()

        fringe.remove(fringe[0])
        if checkLegal(v) and getBlockCount(v) == requirement: return path
        #print(len(get_children(v)))
        for c in get_children(v):


            count = 0
            for x in range(0, height):
                s2 = ""
                for y in range(0, width): 
                    s2 += c[count] + " "
                    count += 1
                print(s2)
            print()


            if c not in visited:
                c_path = path.copy()
                c_path.append(c)
                fringe.append((c, c_path))
                visited.add(c)
    return None

if requirement == (height * width):
    for x in range(0, requirement): s += "#"
else:
    for x in range(0, height * width): s += "-"
    if len(args) > 2: 
        for x in args[2:]:
            first = x[0]
            r = int(x[1: x.index("x"): 1])
            count = x.index("x") + 1
            b = False
            for y in x[x.index("x") + 1:]:
                if y.isalpha() or y == "#": 
                    b = True
                    break
                count += 1
            c = int(x[x.index("x") + 1: count: 1])
            pos = (r * width) + c
            if not b: s = s[0: pos: 1] + "#" + s[pos + 1:]
            else:
                word = x[count:]
                if first == "H":
                    for y in word:
                        s = s[0: pos: 1] + y + s[pos + 1:]
                        pos += 1
                else:
                    for y in word:
                        s = s[0: pos: 1] + y + s[pos + 1:]
                        pos += width
    if requirement != 0:
        s2 = bfs(s)
        s = s2[len(s2) - 1]
count = 0
for x in range(0, height):
    s2 = ""
    for y in range(0, width): 
        s2 += s[count] + " "
        count += 1
    print(s2)
# Arav Singh, 2, 2023