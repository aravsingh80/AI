cp = "X"
ai = "X"
me = "O"
board2 = "OXOXXOOOX"
players = ["X", "O"]
def swap(p):
    temp = p[0]
    p[0] = p[1]
    p[1] = temp

def g2(board):
    actualBoard = []
    count = 1
    b = []
    for x in board:
        b.append(x)
        if count % 3 == 0:
            temp = b.copy()
            actualBoard.append(temp)
            b.clear()
        count += 1
    c = ""
    count = 0
    for x in actualBoard:
        c = x[0]
        for y in x:
            if y == c and y != ".": count += 1
        if count == 3: return [True, c]
        else: count = 0
    columns = dict()
    count = 1
    columns[0] = set()
    columns[1] = set()
    columns[2] = set()
    for x in board:
        columns[count % 3].add(x)
        count += 1
    for x in columns:
        if len(columns[x]) == 1 and "." not in columns[x]: return [True, list(columns[x])[0]]
    if board[0] != "." and board[0] == board[4] == board[8]: return [True, board[0]]
    if board[2] != "." and board[2] == board[4] == board[6]: return [True, board[2]]
    return [False, -2]

def game_over(board):
    if "." not in board:
        g3 = g2(board)
        if g3[0]: 
            num = -2
            if g3[1] == "X": num = 1
            else: num = -1
            return [True, num]
        else: return [True, 0]
    else:
        g3 = g2(board)
        if g3[0]: 
            num = -2
            if g3[1] == "X": num = 1
            else: num = -1
            return [True, num]
        else: return [False, -2]
print(game_over(board2))