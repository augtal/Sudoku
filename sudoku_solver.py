def __findEmpty(board):
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

def __checkGrid(board, cur_pos, number, size_row, size_col):
    row, col = cur_pos

    x_box = row // size_row #sizeRow   0
    y_box = col // size_col #sizeCol   1

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
    empty_cell = __findEmpty(board) #returns false if it can't find an empty value

    if not empty_cell:
        return True #found the solution because we have no more empty cells
    else: 
        row_empty, col_empty = empty_cell

    for i in range(1,len(board)+1):
        if(__validNumber(board, empty_cell, i, size_row, size_col)):
            board[row_empty][col_empty] = i

            if __solveBoard(board, size_row, size_col):
                return True

            board[row_empty][col_empty] = 0 #resets value to try again

    return False

def __fixBoard(board):
    """
    fix_board = []
    for i in range(len(board)):
        fix_board.append(list(map(int, board[i])))
    """

    fix_board = [ list(map(int, i)) for i in board ]
    return fix_board

def solve(board):
    size = len(board)
    board = __fixBoard(board)
    if size == 4:
        __solveBoard(board, int(size/2), int(size/2))
    elif size == 6:
        __solveBoard(board, int(size/3), int(size/2))
    elif size == 9:
        __solveBoard(board, int(size/3), int(size/3))
    else:
        print("Unsupported board")
    return board
