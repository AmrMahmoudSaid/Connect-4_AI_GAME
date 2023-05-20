import copy

EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2
ROWS = 6
COLS = 7
LENGTH = 4

###################################################################################
# Alpha-beta algorithm

def alphabeta(board, depth, alpha, beta, maximizing_player):
    if depth == 0:
        return evaluate_board(board)
    elif isWinner(board, PLAYER_1):
        return evaluate_board(board)
    elif isWinner(board, PLAYER_2):
        return evaluate_board(board)
    if maximizing_player:
        max_eval = float("-inf")
        valid_moves = get_valid_moves(board)
        for col in valid_moves:
            next_board = copy.deepcopy(board)
            make_move(next_board, col, PLAYER_1)
            eval_score = alphabeta(next_board, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if alpha >= beta:
                break
        return max_eval
    else:
        min_eval = float("inf")
        valid_moves = get_valid_moves(board)
        for col in valid_moves:
            next_board = copy.deepcopy(board)
            make_move(next_board, col, PLAYER_2)
            eval_score = alphabeta(next_board, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if alpha >= beta:
                break
        return min_eval


def mbestMove(board, depth):
    valid_moves = get_valid_moves(board)
    best_score = float("-inf")
    best_move = None
    for col in valid_moves:
        next_board = copy.deepcopy(board)
        make_move(next_board, col, PLAYER_1)
        eval_score = alphabeta(
            next_board, depth - 1, float("-inf"), float("inf"), False
        )
        if eval_score > best_score:
            best_score = eval_score
            best_move = col
    return best_move

def is_valid_move(board, col):
    return board[0][col] == EMPTY


def make_move(board, col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = player
            return


def get_valid_moves(board):
    return [col for col in range(COLS) if is_valid_move(board, col)]


def isWinner(board, player):
    for row in range(ROWS):
        for col in range(COLS - LENGTH + 1):
            if all(board[row][col + i] == player for i in range(LENGTH)):
                return True
    for col in range(COLS):
        for row in range(ROWS - LENGTH + 1):
            if all(board[row + i][col] == player for i in range(LENGTH)):
                return True

    for row in range(ROWS - LENGTH + 1):
        for col in range(COLS - LENGTH + 1):
            if all(board[row + i][col + i] == player for i in range(LENGTH)):
                return True
    for row in range(LENGTH - 1, ROWS):
        for col in range(COLS - LENGTH + 1):
            if all(board[row - i][col + i] == player for i in range(LENGTH)):
                return True

    return False


def is_board_full(board):
    return all(board[0][col] != EMPTY for col in range(COLS))


def evaluate_board(board):
    if isWinner(board, PLAYER_1):
        return 1
    elif isWinner(board, PLAYER_2):
        return -1
    else:
        return 0