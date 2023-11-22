def is_safe(board, row, col):
    if any(board[row][c] == 1 for c in range(col)):
        return False

    if any(board[i][col - i] == 1 for i in range(row, -1, -1)):
        return False

    if any(board[i][col + i] == 1 for i in range(row, len(board))):
        return False

    return True

def solve_queens(board, col):
    if col == len(board):
        return True  

    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1 

            if solve_queens(board, col + 1):
                return True 

            board[row][col] = 0


def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))

if __name__ == "__main__":
    chessboard = [[0] * n for _ in range(n)]

    if solve_queens(chessboard, 0):
        print("Solution found:")
        print_solution(chessboard)
    else:
        print("No solution found.")
