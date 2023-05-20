from board import Board
import time
import random
from Alphabeta import make_best_move
from MiniMax import make_best

# GAME LINK
# http://kevinshannon.com/connect4/


#####################################################################################
def main():
    board = Board()

    time.sleep(5)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()
        # FOR DEBUG PURPOSES
        board.print_grid(game_board)
        # print(board.board+"\n")
        # # YOUR CODE GOES HERE
        column = make_best(game_board)
        print(column)
        # print(column)
        print(game_board)
        # print(random_column)
        board.select_column(1)
        time.sleep(2)


if __name__ == "__main__":
    main()