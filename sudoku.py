board = [
    [0, 0, 0, 8, 7, 5, 0, 2, 0],
    [0, 6, 0, 0, 2, 3, 0, 0, 4],
    [0, 0, 3, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 2, 0, 9],
    [0, 7, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 6, 0, 0],
    [1, 0, 0, 5, 4, 0, 0, 3, 0],
    [0, 5, 0, 6, 1, 9, 0, 0, 0]
]


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


print_board(board)
