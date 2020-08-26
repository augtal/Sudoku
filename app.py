import board_printer

def findEmpty(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]==0:
                return (row,col)
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

def __checkGrid(board, cur_pos, number):
    row, col = cur_pos
    size = 3

    x_box = row // size #sizeRow   0
    y_box = col // size #sizeCol   1

    for x in range(x_box*size, x_box*size+size):
        for y in range(y_box*size, y_box*size+size):
            if x == row and y == col:
                continue

            if number == board[x][y]:
                return False

    return True

def validNumber(board, cur_pos, number):
    if not __checkRow(board, cur_pos, number):
        return False
    elif not __checkCol(board, cur_pos, number):
        return False
    elif not __checkGrid(board, cur_pos, number):
        return False
    else:
        return True

def solveBoard(board):
    empty_cell = findEmpty(board) #returns false if it can't find an empty value

    if not empty_cell:
        return True #found the solution because we have no more empty cells
    else: 
        row_empty, col_empty = empty_cell

    for i in range(1,10):
        if(validNumber(board, empty_cell, i)):
            board[row_empty][col_empty] = i

            if solveBoard(board):
                return True

            board[row_empty][col_empty] = 0 #resets value to try again

    return False

if __name__=="__main__":
    board4x4, board6x6, board9x9 = board_printer.boards()
    mainBoard = board9x9
    print("Unsolved grid:")
    board_printer.printBoard(mainBoard)

    solveBoard(mainBoard)
    print(" ")

    print("Solved grid:")
    board_printer.printBoard(mainBoard)