height = 10
width = 15
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
        if x == 0: 
            print('f')
            return False
    
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
            if count == activeSpaces and count != 0: 
                print("e")
                return False
            if x - 1 >= 0 and x - width >= 0 and puzzle[x - 1] == "#" and puzzle[x - width] == "#":
                if puzzle[x - width - 1]  != "#":
                    print("a")
                    return False
            if x - 1 >= 0 and x + width < len(puzzle) and puzzle[x - 1] == "#" and puzzle[x + width] == "#":
                if puzzle[x + width - 1]  != "#": 
                    print("b")
                    return False
            if x + 1 < (int(x / width) + 1) * width and x - width >= 0 and puzzle[x + 1] == "#" and puzzle[x - width] == "#":
                if puzzle[x - width + 1]  != "#": 
                    print("c")
                    return False
            if x + 1 < (int(x / width) + 1) * width and x + width < len(puzzle) and puzzle[x + 1] == "#" and puzzle[x + width] == "#":
                if puzzle[x + width + 1]  != "#": 
                    print("d")
                    return False

    return True


print(checkLegal("----------D--------------e--------------d--------------u#-------------c--------------t----#---------i--------------b--------------l-------#------e----"))