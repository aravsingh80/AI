from othello_imports import possible_moves, make_move
import random
import sys
board = sys.argv[1]
mainplayer = sys.argv[2]
if mainplayer == "x": otherplayer = "o"
else: otherplayer = "x"

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
    returnScore += (len(p1) * 7)
    returnScore -= (len(p2) * 7)
    # p3 = possible_next_boards(board, player)
    # p4 = possible_next_boards(board, nextplayer)
    for x in corners:
        if board[x] == player: returnScore += 260
        if board[x] == nextplayer: returnScore -= 260
    for x in nextToCorners:
        if board[x] != ".":
            if x in zeroCorners:
                if board[0] == ".":
                    if board[x] == player: returnScore -= 160
                    if board[x] == nextplayer: returnScore += 160
                else:
                    if board[0] == player: 
                        if board[x] == player: returnScore += 70
                        if board[x] == nextplayer: returnScore += 30
                    if board[0] == nextplayer:
                        if board[x] == player: returnScore -= 30
                        if board[x] == nextplayer: returnScore -= 70
            if board[x] in sevenCorners:
                if board[7] == ".":
                    if board[x] == player: returnScore -= 160
                    if board[x] == nextplayer: returnScore += 160
                else:
                    if board[7] == player: 
                        if board[x] == player: returnScore += 70
                        if board[x] == nextplayer: returnScore += 30
                    if board[7] == nextplayer:
                        if board[x] == player: returnScore -= 30
                        if board[x] == nextplayer: returnScore -= 70
            if board[x] in fiftysixCorners:
                if board[56] == ".":
                    if board[x] == player: returnScore -= 160
                    if board[x] == nextplayer: returnScore += 160
                else:
                    if board[56] == player: 
                        if board[x] == player: returnScore += 70
                        if board[x] == nextplayer: returnScore += 30
                    if board[56] == nextplayer:
                        if board[x] == player: returnScore -= 30
                        if board[x] == nextplayer: returnScore -= 70
            if board[x] in sixtythreeCorners:
                if board[63] == ".":
                    if board[x] == player: returnScore -= 160
                    if board[x] == nextplayer: returnScore += 160
                else:
                    if board[63] == player: 
                        if board[x] == player: returnScore += 70
                        if board[x] == nextplayer: returnScore += 30
                    if board[63] == nextplayer:
                        if board[x] == player: returnScore -= 30
                        if board[x] == nextplayer: returnScore -= 70
    for x in edgePieces:
        if board[x] == player: returnScore += 85
        if board[x] == nextplayer: returnScore -= 85
    return returnScore

def possible_next_boards(board, p):
    possibles = possible_moves(board, p)
    return [(make_move(board, p, x), x) for x in possibles]

def negamax(board, token, curr_depth, static_depth):
    if token == "x": t = "o" 
    else: t = "x"
    results = set()
    p = possible_next_boards(board, t)
    if len(p) == 0 or curr_depth == static_depth: return score(board, token, t)
    else:
        for next_board in p:
            next_board2, index = next_board
            results.add(-1 * negamax(next_board2, t, curr_depth + 1, static_depth))
    return min(results)

def find_next_move(board, player, depth):
    move = None
    maxMove = -float("inf")
    p = possible_next_boards(board, player)
    for next_board in p:
        next_board2, index = next_board
        m = negamax(next_board2, player, 0, depth)
        if m >= maxMove:
            move = index
            maxMove = m
    return move

depth = 1
for count in range(board.count(".")):  
   print(find_next_move(board, mainplayer, depth))
   depth += 1