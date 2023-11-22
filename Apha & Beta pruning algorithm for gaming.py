import math

def evaluate(board):
    
    if 'X' in board and 'O' in board:
        return 
    elif 'X' in board:
        return 1  
    elif 'O' in board:
        return -1  
    else:
        return 0 

def is_terminal(board):
    return evaluate(board) != 0 or len([cell for cell in board if cell == ' ']) == 0

def minimax(board, depth, maximizing_player, alpha, beta):
    if depth == 0 or is_terminal(board):
        return evaluate(board)

    if maximizing_player:
        max_eval = -math.inf
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth - 1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break 
        return max_eval
    else:
        min_eval = math.inf
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth - 1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  
        return min_eval

def find_best_move(board):
    best_val = -math.inf
    best_move = -1

    for i in range(len(board)):
        if board[i] == ' ':
            board[i] = 'X'
            move_val = minimax(board, 3, False, -math.inf, math.inf)
            board[i] = ' '
            if move_val > best_val:
                best_move = i
                best_val = move_val

    return best_move

def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("-" * 9)

def main():
    board = [' '] * 9

    print("Initial Board:")
    print_board(board)

    for _ in range(4): 
        move = find_best_move(board)
        board[move] = 'X'

        print(f"\nAfter X's move:")
        print_board(board)

        if is_terminal(board):
            break
        empty_cells = [i for i, cell in enumerate(board) if cell == ' ']
        o_move = empty_cells[0]
        board[o_move] = 'O'

        print(f"\nAfter O's move:")
        print_board(board)

        if is_terminal(board):
            break

    print("\nGame Over.")
    print("Final Board:")
    print_board(board)

if __name__ == "__main__":
    main()
