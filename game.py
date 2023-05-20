from board import Board
import time
from Alphabeta import mbestMove
from MiniMax import minimax

# GAME LINK
# http://kevinshannon.com/connect4/


#####################################################################################
def main():
    board = Board()
    algo = input("To Alphabeta enter 1 or MiniMax enter 2")
    diff = input("To Easy enter 1 or Midme  enter 2 or hard enter 3")
    time.sleep(4)
    game_end = False
    while not game_end:
        (game_board, game_end) = board.get_game_grid()
        # FOR DEBUG PURPOSES
        board.print_grid(game_board)
        if game_end:
            break
        # # YOUR CODE GOES HERE
        if algo == 1:
            if diff == 1:
                column = mbestMove(game_board, 3)
            elif diff == 2:
                column = mbestMove(game_board, 5)
            elif diff == 3:
                column = mbestMove(game_board, 6)

        elif algo == 2:
            if diff == 1:
                column = minimax(game_board, 3, 1)
            elif diff == 2:
                column = minimax(game_board, 5, 1)
            elif diff == 3:
                column = minimax(game_board, 6, 1)

        print(column)
        # print(column)
        print(game_board)
        # print(random_column)
        board.select_column(column)
        time.sleep(2)


if __name__ == "__main__":
    main()
