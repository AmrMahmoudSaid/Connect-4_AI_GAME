import copy

EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2
ROWS = 6
COLS = 7
WINNING_LENGTH = 4


def is_valid_move(board, col):
    return board[0][col] == EMPTY


def make_move(board, col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = player
            return


def get_valid_moves(board):
    return [col for col in range(COLS) if is_valid_move(board, col)]


####################################################################################
# Alpha-beta algorithm
def minimax(board, alpha, beta, maximizing_player):
    if maximizing_player:
        max_eval = float("-inf")
        valid_moves = get_valid_moves(board)
        for col in valid_moves:
            next_board = copy.deepcopy(board)
            make_move(next_board, col, PLAYER_1)
            eval_score = minimax(next_board, alpha, beta, False)
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
            eval_score = minimax(next_board, alpha, beta, True)
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if alpha >= beta:
                break
        return min_eval


def make_best(board):
    valid_moves = get_valid_moves(board)
    best_score = float("-inf")
    best_move = None
    for col in valid_moves:
        next_board = copy.deepcopy(board)
        make_move(next_board, col, PLAYER_1)
        eval_score = minimax(
            next_board, float("-inf"), float("inf"), False
        )
        if eval_score > best_score:
            best_score = eval_score
            best_move = col
    return best_move