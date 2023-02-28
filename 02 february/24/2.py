def check_win(board, player):
    # Check for horizontal wins
    for y in range(4):
        for z in range(4):
            if all(board[x][y][z] == player for x in range(4)):
                return True
    # Check for vertical wins
    for x in range(4):
        for z in range(4):
            if all(board[x][y][z] == player for y in range(4)):
                return True
    # Check for depth wins
    for x in range(4):
        for y in range(4):
            if all(board[x][y][z] == player for z in range(4)):
                return True
    # Check for diagonal wins
    if all(board[i][i][i] == player for i in range(4)):
        return True
    if all(board[3 - i][i][i] == player for i in range(4)):
        return True
    if all(board[i][3 - i][i] == player for i in range(4)):
        return True
    if all(board[i][i][3 - i] == player for i in range(4)):
        return True
    if all(board[i][3 - i][3 - i] == player for i in range(4)):
        return True
    if all(board[3 - i][3 - i][i] == player for i in range(4)):
        return True
    if all(board[3 - i][i][3 - i] == player for i in range(4)):
        return True
    return False


def xo_3d(moves):
    board = [[[None for z in range(4)] for y in range(4)] for x in range(4)]
    players = ['O', 'X']
    current_player = players[0]
    for i, move in enumerate(moves):
        x, y, z = move
        board[x][y][z] = current_player
        if check_win(board, current_player):
            return f"{current_player} wins after {i + 1} moves"
        current_player = players[(players.index(current_player) + 1) % 2]
    return "No winner"


# print(xo_3d([]))
print(xo_3d([[0, 2, 1], [0, 2, 2], [1, 2, 1], [1, 2, 2], [2, 2, 1], [2, 2, 2] , [3, 2, 1]]))
# print(xo_3d([[0, 1, 1], [0, 0, 0], [0, 2, 2], [1, 1, 1], [1, 2, 2], [2, 2, 2] , [2, 1, 2], [3, 3, 3], [0, 2, 1]]))
