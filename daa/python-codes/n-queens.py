def print_board(board):
    for row in board:
        print(row)
    print()


def is_safe(board, row, col, n):

    for i in range(row):
        if board[i][col] == 1:
            return False


    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):

    if row == n:
        print("Final N-Queens Matrix:")
        print_board(board)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens(board, row + 1, n):
                return True
            board[row][col] = 0  

    return False


def n_queens_with_first_queen(n, first_row, first_col):

    board = [[0 for _ in range(n)] for _ in range(n)]


    board[first_row][first_col] = 1


    if not solve_n_queens(board, first_row + 1, n):
        print("No solution possible with the given first queen position.")



n = 4
first_row, first_col = 0, 1  
n_queens_with_first_queen(n, first_row, first_col)
