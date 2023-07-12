from utilities import generate_piece, print_board
from typing import List, Dict

DEV_MODE = False

def shift_left(game_board):
    new_board = []
    for row in range(0,4):
        new_board.append([0] * 4)

    for row in range(0,4):
        pos = 0
        for column in range(0, 4):
            if game_board[row][column] != 0:
                new_board[row][pos] = game_board[row][column]
                pos += 1
    return new_board

def add_duplicates_left(game_board):
    for row in range(0,4):
        for column in range(0,3):
            if (game_board[row][column] == game_board[row][column+1] and game_board[row][column] != 0):
                game_board[row][column] = game_board[row][column] * 2
                game_board[row][column + 1] = 0

def shift_right(game_board):
    new_board = []
    for row in range(0,4):
        new_board.append([0] * 4)

    for row in range(0,4):
        pos = 3
        for column in reversed((range(0,4))):
            if game_board[row][column] != 0:
                new_board[row][pos] = game_board[row][column]
                pos -= 1
    return new_board

def add_duplicates_right(game_board):
    for row in range(0,4):
        for column in reversed(range(0,3)):
            if (game_board[row][column] == game_board[row][column + 1] and game_board[row][column] != 0):
                game_board[row][column + 1] = game_board[row][column] * 2
                game_board[row][column] = 0

def shift_up(game_board):
    new_board = []
    for row in range(0,4):
        new_board.append([0] * 4)

    for column in range(0,4):
        pos = 0
        for row in range(0,4):
            if game_board[row][column] != 0:
                new_board[pos][column] = game_board[row][column]
                pos += 1
    return new_board

def add_duplicates_up(game_board):
    for column in range(0,4):
        for row in range(1,4):
            if (game_board[row - 1][column] == game_board[row][column] and game_board[row][column] != 0):
                game_board[row - 1][column] = game_board[row][column] * 2
                game_board[row][column] = 0

def shift_down(game_board):
    new_board = []
    for row in range(0,4):
        new_board.append([0] * 4)
    
    for column in range(0,4):
        pos = 3
        for row in reversed(range(0,4)):
            if game_board[row][column] != 0:
                new_board[pos][column] = game_board[row][column]
                pos -= 1
    return new_board

def add_duplicates_down(game_board):
    for column in range(0,4):
        for row in reversed(range(0,3)):
            if (game_board[row + 1][column] == game_board[row][column] and game_board[row][column] != 0):
                game_board[row + 1][column] = game_board[row][column] * 2
                game_board[row][column] = 0

def main(game_board: List[List[int]]) -> List[List[int]]:
    """
    2048 main function, runs a game of 2048 in the console

    Uses the following keys: 
    w = shift up
    a = shift left
    s = shift down
    d = shift right
    q = ends the game and returns control of the console
    : param game_board: a 4x4 2D list of integers representing a game of 2048
    : return: returns the ending game board
    """

    # initialize board's first cell
    # TODO: generate a random piece and location using the generate_piece function
    first_cell = generate_piece(game_board, DEV_MODE)

    # TODO: place the piece at the specified location
    game_board[first_cell['row']][first_cell['column']] = first_cell['value']

    # initialize game state trackers

    # game loop
    while True:
        first_cell = generate_piece(game_board, DEV_MODE)
        game_board[first_cell['row']][first_cell['column']] = first_cell['value']
        print_board(game_board)

        # TODO: reset the user input variable
        user_input = input("Enter your move (w/a/s/d) or q to quit: ")
        print("user input", user_input)

        if user_input == 'q':
            print("Goodbye")
            break
        elif user_input == 'a':     # shifts left
            game_board = shift_left(game_board)
            add_duplicates_left(game_board)
            game_board = shift_left(game_board)
        elif user_input == 'w':     # shifts up
            game_board = shift_up(game_board)
            add_duplicates_up(game_board)
            game_board = shift_up(game_board)
        elif user_input == 's':     # shifts down
            game_board = shift_down(game_board)
            add_duplicates_down(game_board)
            game_board = shift_down(game_board)
        elif user_input == 'd':     # shifts right
            game_board = shift_right(game_board)
            add_duplicates_right(game_board)
            game_board = shift_right(game_board)

        if game_over(game_board):
            break
            
    return game_board

def game_over(game_board: List[List[int]]) -> bool:
    """
    Query the provided board's game state

    : param game_board: a 4x4 2D list of integers representing a game of 2048
    : return: Boolean indicating if the game is over (True) or not (False)
    """
    # Check for win condition
    for row in range(0, 4):
        for column in range(0, 4):
            if game_board[row][column] == 2048:
                print("You win!")
                return True

    # Check for empty cells
    for row in range(0, 4):
        for column in range(0, 4):
            if game_board[row][column] == 0:
                return False

    # Check for possible merges
    for row in range(0, 3):
        for column in range(0, 3):
            if game_board[row][column] == game_board[row][column + 1] or game_board[row][column] == game_board[row + 1][column]:
                return False

    for column in range(0, 3):
        if game_board[3][column] == game_board[3][column + 1]:
            return False

    for row in range(0, 3):
        if game_board[row][3] == game_board[row + 1][3]:
            return False

    return True


if __name__ == "__main__":
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])