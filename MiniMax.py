WIN_SCORE = 1000000
TIE_SCORE = 0
LOSE_SCORE = -1000000
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2
ROWS = 6
COLS = 7
WINNING_LENGTH = 4
MAX_DEPTH = 6

import copy


def minimax(board, depth, is_maximizing):
    if (
        depth == 0
        or is_winner(board, PLAYER_1)
        or is_winner(board, PLAYER_2)
        or is_board_full(board)
    ):
        return evaluate_board(board)

    if is_maximizing:
        best_score = float("-inf")
        best_move = None
    else:
        best_score = float("inf")
        best_move = None

    moves = get_valid_moves(board)
    for move in moves:
        tempBoard = copy.deepcopy(board)
        if is_maximizing:
            makeMove(tempBoard, move, PLAYER_1)
        else:
            makeMove(tempBoard, move, PLAYER_2)

        score = minimax(tempBoard, depth - 1, not is_maximizing)

        if is_maximizing:
            if score > best_score:
                best_score = score
                best_move = move
        else:
            if score < best_score:
                best_score = score
                best_move = move

    return best_move

def isValidMove(board, col):
    return board[0][col] == EMPTY


def makeMove(board, col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = player
            return


def get_valid_moves(board):
    return [col for col in range(COLS) if isValidMove(board, col)]


def is_winner(board, player):
    for row in range(ROWS):
        for col in range(COLS - WINNING_LENGTH + 1):
            if all(board[row][col + i] == player for i in range(WINNING_LENGTH)):
                return True

    for col in range(COLS):
        for row in range(ROWS - WINNING_LENGTH + 1):
            if all(board[row + i][col] == player for i in range(WINNING_LENGTH)):
                return True

    for row in range(ROWS - WINNING_LENGTH + 1):
        for col in range(COLS - WINNING_LENGTH + 1):
            if all(board[row + i][col + i] == player for i in range(WINNING_LENGTH)):
                return True

    for row in range(WINNING_LENGTH - 1, ROWS):
        for col in range(COLS - WINNING_LENGTH + 1):
            if all(board[row - i][col + i] == player for i in range(WINNING_LENGTH)):
                return True

    return False


def is_board_full(board):
    return all(board[0][col] != EMPTY for col in range(COLS))


def evaluate_board(board):
    if is_winner(board, PLAYER_1):
        return 1
    elif is_winner(board, PLAYER_2):
        return -1
    else:
        return 0


