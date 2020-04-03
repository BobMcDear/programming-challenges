moves = {'K': ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)), 
        'N': ((-1, -2), (-2, -1), (-1, 2), (-2, 1), (1, -2), (2, -1), (1, 2), (2, 1)),
        'P': ((-1, -1), (-1, 1)),
        'p': ((1, -1), (1, 1)),
        'B': ((-1, -1), (-1, 1), (1, -1), (1, 1)),
        'R': ((-1, 0), (0, -1), (0, 1), (1, 0))}
moves['k'] = moves['K']
moves['n'] = moves['N']
moves['b'] = moves['B']
moves['r'] = moves['R']
moves['q'] = moves['Q'] = moves['B'] + moves['R']
single_moves = ['K', 'k', 'N', 'n', 'P', 'p']

def fen_to_board(f):
    board = []
    f = f.split('/')
    for i in f:
        curr_row = ''
        for j in i:
            if 49 <= ord(j) <= 57:
                curr_row += ' ' * int(j)
            else:
                curr_row += j
        board.append(curr_row)
    return board

def isOk(pos):
    return (0 <= pos[0] <= 7) and (0 <= pos[1] <= 7)

ans = []
while True:
    try:
        fen = input()
        board = fen_to_board(fen)
        # False means not attacked, True means attacked
        attacked_board = [[False for i in range(8)] for j in range(8)]  
        for i in range(8):
            for j in range(8):
                if board[i][j] != ' ':
                    curr_piece_moves = moves[board[i][j]]
                    if board[i][j] in single_moves:
                        for k in curr_piece_moves:
                            curr_pos = (i + k[0], j + k[1])
                            if isOk(curr_pos) and board[curr_pos[0]][curr_pos[1]] == ' ':
                                attacked_board[curr_pos[0]][curr_pos[1]] = True
                    else:
                        for k in curr_piece_moves:
                            curr_pos = [i + k[0], j + k[1]]
                            while isOk(curr_pos) and (board[curr_pos[0]][curr_pos[1]] == ' '):
                                attacked_board[curr_pos[0]][curr_pos[1]] = True
                                curr_pos[0] += k[0]
                                curr_pos[1] += k[1]
        r = 0
        for i in range(8):
            for j in range(8):
                if (not attacked_board[i][j]) and board[i][j] == ' ':
                    r += 1
        ans.append(r)

    except EOFError:
        for i in ans:
            print(i)
        break