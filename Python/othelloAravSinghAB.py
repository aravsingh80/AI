#from othello_imports import possible_moves, make_move
import time
import sys
board = sys.argv[1]
mainplayer = sys.argv[2]
if mainplayer == "x": otherplayer = "o"
else: otherplayer = "x"
def possible_moves(board, token):
    possibles = set()
    if token == "x": other_token = "o"
    else: other_token = "x"
    for x in range(0, 64):
        if board[x] == ".":
            count = 1          
            while x + count < (int(x / 8) + 1) * 8:
                if board[x + count] == other_token: count += 1
                elif board[x + count] == token:
                    if count > 1: possibles.add(x)
                    break
                else: break
            count = 1            
            while x - count >= int(x / 8) * 8:
                if board[x - count] == other_token: count += 1
                elif board[x - count] == token:
                    if count > 1: possibles.add(x)
                    break
                else: break
            count = 8         
            while x + count < 64:
                if board[x + count] == other_token: count += 8
                elif board[x + count] == token:
                    if count > 8: possibles.add(x)
                    break
                else: break
            count = 8            
            while x - count >= 0:
                if board[x - count] == other_token: count += 8
                elif board[x - count] == token:
                    if count > 8: possibles.add(x)
                    break
                else: break
            count = 9         
            while x + count < 64 and (x + count) % 8 != 0:
                if board[x + count] == other_token: count += 9
                elif board[x + count] == token:
                    if count > 9: possibles.add(x)
                    break
                else: break
            count = 9        
            while x - count >= 0 and (x - count + 9) % 8 != 0:
                if board[x - count] == other_token: count += 9
                elif board[x - count] == token:
                    if count > 9: possibles.add(x)
                    break
                else: break
            count = 7         
            while x + count < 64 and (x + count + 1) % 8 != 0:
                if board[x + count] == other_token: count += 7
                elif board[x + count] == token:
                    if count > 7: possibles.add(x)
                    break
                else: break
            count = 7
            while x - count >= 0 and (x - count) % 8 != 0:
                if board[x - count] == other_token: count += 7
                elif board[x - count] == token:
                    if count > 7: possibles.add(x)
                    break
                else: break
    return list(possibles)

def make_move(board, token, index):
    if token == "x": other_token = "o"
    else: other_token = "x"
    count = 1   
    spaces = set()       
    temp1 = board[0: index: 1] 
    temp2 = board[index + 1: len(board) : 1]
    board = ""
    board += temp1 + token + temp2
    while index + count < (int(index / 8) + 1) * 8:
        if board[index + count] == other_token: 
            spaces.add(index + count)
            count += 1
        elif board[index + count] == token:
            if count > 1: 
                for x2 in spaces: 
                    temp1 = board[0: x2: 1] 
                    temp2 = board[x2 + 1: len(board) : 1]
                    board = ""
                    board += temp1 + token + temp2
            break
        else: break
    count = 1 
    spaces.clear()           
    while index - count >= int(index / 8) * 8:
        if board[index - count] == other_token: 
            spaces.add(index - count)
            count += 1
        elif board[index - count] == token:
            if count > 1:
                for x2 in spaces: 
                    temp1 = board[0: x2: 1] 
                    temp2 = board[x2 + 1: len(board) : 1]
                    board = ""
                    board += temp1 + token + temp2
            break
        else: break
    count = 8 
    spaces.clear()        
    while index + count < 64:
        if board[index + count] == other_token: 
            spaces.add(index + count)
            count += 8
        elif board[index + count] == token:
            if count > 8: 
                for x2 in spaces: 
                    temp1 = board[0: x2: 1] 
                    temp2 = board[x2 + 1: len(board) : 1]
                    board = ""
                    board += temp1 + token + temp2
            break
        else: break
    count = 8  
    spaces.clear()          
    while index - count >= 0:
        if board[index - count] == other_token: 
            spaces.add(index - count)
            count += 8
        elif board[index - count] == token:
            if count > 8: 
                for x2 in spaces: 
                    temp1 = board[0: x2: 1] 
                    temp2 = board[x2 + 1: len(board) : 1]
                    board = ""
                    board += temp1 + token + temp2
            break
        else: break
    count = 9  
    spaces.clear()       
    while index + count < 64 and (index + count) % 8 != 0:
        if board[index + count] == other_token: 
            spaces.add(index + count)
            count += 9
        elif board[index + count] == token:
            if count > 9: 
                for x2 in spaces: 
                    temp1 = board[0: x2: 1] 
                    temp2 = board[x2 + 1: len(board) : 1]
                    board = ""
                    board += temp1 + token + temp2
            break
        else: break
    count = 9  
    spaces.clear()      
    while index - count >= 0 and (index - count + 9) % 8 != 0:
        if board[index - count] == other_token: 
            spaces.add(index - count)
            count += 9
        elif board[index - count] == token:
            if count > 9: 
                for x2 in spaces: 
                    temp1 = board[0: x2: 1] 
                    temp2 = board[x2 + 1: len(board) : 1]
                    board = ""
                    board += temp1 + token + temp2
            break
        else: break
    count = 7         
    spaces.clear()
    while index + count < 64 and (index + count + 1) % 8 != 0:
        if board[index + count] == other_token: 
            spaces.add(index + count)
            count += 7
        elif board[index + count] == token:
            if count > 7:
                for x2 in spaces: 
                    temp1 = board[0: x2: 1] 
                    temp2 = board[x2 + 1: len(board) : 1]
                    board = ""
                    board += temp1 + token + temp2
            break
        else: break
    count = 7
    spaces.clear()
    while index - count >= 0 and (index - count) % 8 != 0:
        if board[index - count] == other_token: 
            spaces.add(index - count)
            count += 7
        elif board[index - count] == token:
            if count > 7:
                for x2 in spaces: 
                    temp1 = board[0: x2: 1] 
                    temp2 = board[x2 + 1: len(board) : 1]
                    board = ""
                    board += temp1 + token + temp2
            break
        else: break
    return board
    
def game_over(board, token): 
    if token == "x": other_token = "o"
    else: other_token = "x"
    if len(possible_moves(board, token)) == 0: 
        countToken = 0
        countOther = 0
        for x in board:
            if x == token: countToken += 1
            if x == other_token: countOther += 1
        if countToken > countOther: return [True, float("inf")]
        elif countToken < countOther: return [True, -float("inf")]
        else: return [True, 0]
    return [False, -float("inf")]

def score(board, player, nextplayer): 
    g = game_over(board, player)
    if g[0]: return g[1]
    returnScore = 0
    corners = [0, 7, 56, 63]
    zeroCorners = [1, 8, 9]
    sevenCorners = [6, 15, 14]
    fiftysixCorners = [57, 48, 49]
    sixtythreeCorners = [62, 55, 54]
    nextToCorners = [1, 8, 9, 6, 15, 14, 57, 48, 49, 62, 55, 54]
    edgePieces = [2, 3, 4, 5, 16, 24, 32, 40, 58, 59, 60, 61, 23, 31, 39, 47]
    firstRow = [0, 7, 1, 2, 3, 4, 5, 6]
    firstColumn = [0, 56, 8, 48, 16, 24, 32, 40]
    lastRow = [56, 63, 57, 58, 59, 60, 61, 62]
    lastColumn = [7, 63, 15, 55, 23, 31, 39, 47]
    count = 0
    p1 = possible_moves(board, player)
    p2 = possible_moves(board, nextplayer)
    for x in board:
        if x == player: returnScore += 18
        else: returnScore -= 18
    returnScore += (len(p1) * 7)
    returnScore -= (len(p2) * 7)
    for x in corners:
        if board[x] == player: returnScore += 260
        if board[x] == nextplayer: returnScore -= 260
    for x in nextToCorners:
        if board[x] != ".":
            if x in zeroCorners:
                if board[0] == ".":
                    if board[x] == player: returnScore -= 143
                    if board[x] == nextplayer: returnScore += 143
                else:
                    if board[0] == player: 
                        if board[x] == player: returnScore += 87
                        if board[x] == nextplayer: returnScore += 0
                    if board[0] == nextplayer:
                        if board[x] == player: returnScore -= 0
                        if board[x] == nextplayer: returnScore -= 87
            if board[x] in sevenCorners:
                if board[7] == ".":
                    if board[x] == player: returnScore -= 143
                    if board[x] == nextplayer: returnScore += 143
                else:
                    if board[7] == player: 
                        if board[x] == player: returnScore += 87
                        if board[x] == nextplayer: returnScore += 0
                    if board[7] == nextplayer:
                        if board[x] == player: returnScore -= 0
                        if board[x] == nextplayer: returnScore -= 87
            if board[x] in fiftysixCorners:
                if board[56] == ".":
                    if board[x] == player: returnScore -= 143
                    if board[x] == nextplayer: returnScore += 143
                else:
                    if board[56] == player: 
                        if board[x] == player: returnScore += 87
                        if board[x] == nextplayer: returnScore += 0
                    if board[56] == nextplayer:
                        if board[x] == player: returnScore -= 0
                        if board[x] == nextplayer: returnScore -= 87
            if board[x] in sixtythreeCorners:
                if board[63] == ".":
                    if board[x] == player: returnScore -= 143
                    if board[x] == nextplayer: returnScore += 143
                else:
                    if board[63] == player: 
                        if board[x] == player: returnScore += 87
                        if board[x] == nextplayer: returnScore += 0
                    if board[63] == nextplayer:
                        if board[x] == player: returnScore -= 0
                        if board[x] == nextplayer: returnScore -= 87
    for x in edgePieces:
        if board[x] == player: returnScore += 87
        if board[x] == nextplayer: returnScore -= 87
    return returnScore

def possible_next_boards(board, p):
    possibles = possible_moves(board, p)
    return [(make_move(board, p, x), x) for x in possibles]

def negamax(board, token, curr_depth, static_depth, a, b):
    if token == "x": t = "o" 
    else: t = "x"
    p = possible_next_boards(board, t)
    initValue = float("inf")
    if len(p) == 0 or curr_depth == static_depth: return score(board, token, t)
    else:
        for next_board in p:
            next_board2, index = next_board
            initValue = min(initValue, -1 * negamax(next_board2, t, curr_depth + 1, static_depth, -b, -a)) #AB Pruning Here
            a = min(a, initValue) #AB Pruning Here
            if a <= b: break #AB Pruning Here
    return initValue

def find_next_move(board, player, depth):
    move = None
    maxMove = -float("inf")
    p = possible_next_boards(board, player)
    for next_board in p:
        next_board2, index = next_board
        m = negamax(next_board2, player, 0, depth, float("inf"), -float("inf"))
        if m >= maxMove:
            move = index
            maxMove = m
    return move

depth = 1
for count in range(board.count(".")):  
   print(find_next_move(board, mainplayer, depth))
   depth += 1
# class Strategy():
#    logging = True  # Optional
#    def best_strategy(self, board, player, best_move, still_running, time_limit):
#        depth = 1
#        for count in range(board.count(".")):  # No need to look more spaces into the future than exist at all
#            best_move.value = find_next_move(board, player, depth)
#            depth += 1

# results = []
# with open("boards_timing.txt") as f:
#     for line in f:
#         board, token = line.strip().split()
#         temp_list = [board, token]
#         print(temp_list)
#         for count in range(1, 7):
#             print("depth", count)
#             start = time.perf_counter()
#             find_next_move(board, token, count)
#             end = time.perf_counter()
#             temp_list.append(str(end - start))
#         print(temp_list)
#         print()
#         results.append(temp_list)
# with open("boards_timing_my_results.csv", "w") as g:
#     for l in results:
#         g.write(", ".join(l) + "\n")