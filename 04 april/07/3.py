def is_solved(board: list) -> int:
    count = 0
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]

    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]

        count += board[i].count(0)

    return -1 if count > 0 else 0


print(is_solved([[0, 0, 1],
                 [0, 1, 2],
                 [2, 1, 0]]
                )
      )
