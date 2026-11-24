
N = 4

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True

def solve(board, row):
    if row == N:
        print(board)
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1)

            board[row] = -1

board = [-1] * N

print("All possible solutions:")
solve(board, 0)

