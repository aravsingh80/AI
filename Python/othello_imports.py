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