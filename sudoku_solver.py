import random as rnd
import copy


def __findEmpty(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                return (row, col)
    return False


def __checkRow(board, cur_pos, number):
    row, col = cur_pos
    for i in range(len(board[row])):
        if i == col:
            continue

        if number == board[row][i]:
            return False
    return True


def __checkCol(board, cur_pos, number):
    row, col = cur_pos
    for i in range(len(board[row])):
        if i == row:
            continue

        if number == board[i][col]:
            return False
    return True


def __checkGrid(board, cur_pos, number, size_row, size_col):
    row, col = cur_pos

    x_box = row // size_row  # sizeRow   0
    y_box = col // size_col  # sizeCol   1

    for x in range(x_box*size_row, x_box*size_row+size_row):
        for y in range(y_box*size_col, y_box*size_col+size_col):
            if x == row and y == col:
                continue

            if number == board[x][y]:
                return False
    return True


def __validNumber(board, cur_pos, number, size_row, size_col):
    if not __checkRow(board, cur_pos, number):
        return False
    elif not __checkCol(board, cur_pos, number):
        return False
    elif not __checkGrid(board, cur_pos, number, size_row, size_col):
        return False
    else:
        return True


def __solveBoard(board, size_row, size_col):
    # returns false if it can't find an empty value
    empty_cell = __findEmpty(board)

    if not empty_cell:
        return True  # found the solution because we have no more empty cells
    else:
        row_empty, col_empty = empty_cell

    for i in range(1, len(board)+1):
        if(__validNumber(board, empty_cell, i, size_row, size_col)):
            board[row_empty][col_empty] = i

            if __solveBoard(board, size_row, size_col):
                return True

            board[row_empty][col_empty] = 0  # resets value to try again

    return False


def __fixBoard(board):
    """
    fix_board = []
    for i in range(len(board)):
        fix_board.append(list(map(int, board[i])))
    """

    fix_board = [list(map(int, i)) for i in board]
    return fix_board


def findBoardSize(size):
    if size == 4:
        return (int(size/2), int(size/2))
    elif size == 6:
        return (int(size/3), int(size/2))
    elif size == 9:
        return (int(size/3), int(size/3))
    else:
        print("Unsupported board")
        return


def solve(board):
    board = __fixBoard(board)
    size_row, size_col = findBoardSize(len(board))
    if __solveBoard(board, size_row, size_col) is False:
        print("Unsolvable board")
        raise NotImplementedError  # throwing an error to stop the program in main file
    return board

def __makeBoard(size):
    board = []

    # makes empty board based on size
    for i in range(size):
        board_row = []
        for j in range(size):
            board_row.append(0)
        board.append(board_row)

    return board


def generateBoard(size, dificulty="normal"):
    dificulty_dict = {
        "easy": 1,
        "normal": 2,
        "hard": 3,
    }

    dificulty_modifier = 1 - (dificulty_dict[dificulty]) / 4
    # easy = 3/4 | normal = 2/4 | hard = 1/4 of board visible lower number = harder
    size_row, size_col = findBoardSize(size)
    full_size = size**2
    run = True
    
    while run:
        try:
            board = __makeBoard(size)
            counter = 0
            # inserts a small amount of numbers in random places to generate unique board
            while counter < size:
                pos = (rnd.randint(0, size-1), rnd.randint(0, size-1))

                number = rnd.randint(1, size)

                if __validNumber(board, pos, number, size_row, size_col):
                    board[pos[0]][pos[1]] = number
                    counter += 1

            # tries to solve generated board
            solved_board = solve(board)
            
            for i in range(size-3-1):
                number_1 = solved_board[0][i]
                number_2 = solved_board[0][i+1]
                number_3 = solved_board[0][i+2]
                
                #boards first row has increasing numbers
                #doens't serve any other purpose then to not annoy me 
                #triggers on 1,2,3 2,3,4 3,4,5 etc.
                if number_1+1 == number_2 and number_2+1 == number_3:
                    raise NotImplementedError

            run = False
        except NotImplementedError: #catches unsolvable boards
            run = True

    # removes random amount of cell values for user to solve
    counter = 0
    #need to use deep copy because other methods change solved_board too
    generated_board = copy.deepcopy(solved_board)
    remove_amount = int(dificulty_modifier*(full_size))
    while counter < remove_amount:
        pos = (rnd.randint(0, size-1), rnd.randint(0, size-1))

        generated_board[pos[0]][pos[1]] = 0
        counter += 1

    return generated_board, solved_board


if __name__ == "__main__":
    generateBoard(9, dificulty="hard")
