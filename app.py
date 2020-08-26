import board_printer

def findEmpty(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]==0:
                return (row,col)
    return False

def checkRow(board, cur_pos):
    row, col = cur_pos
    for i in range(len(board[row])):
        if i == col:
            continue

        if board[row][col] == board[row][i]:
            return False
    return True

def checkCol(board, cur_pos):
    row, col = cur_pos
    for i in range(len(board[row])):
        if i == row:
            continue

        if board[row][col] == board[i][col]:
            return False
    return True

def checkGrid(board, cur_pos):
    row, col = cur_pos
    size = 2

    x_box = row // size #sizeRow   0
    y_box = col // size #sizeCol   1

    for x in range(x_box*size, x_box*size+size):
        for y in range(y_box*size, y_box*size+size):
            if x == row and y == col:
                continue

            if board[row][col] == board[x][y]:
                return False

    return True


def solveBoard(board):
    empty_cell = findEmpty(board)
    row_empty, col_empty = empty_cell

    boardWorking = board
    boardWorking[row_empty][col_empty] = 8

    board_printer.printBoard(boardWorking)
    print(f"row does't have duplicate: {checkRow(boardWorking, empty_cell)}")
    print(f"col does't have duplicate: {checkCol(boardWorking, empty_cell)}")
    print(f"grid does't have duplicate: {checkGrid(boardWorking, empty_cell)}")

if __name__=="__main__":
    board4x4, board6x6, board9x9 = board_printer.boards()

    mainBoard = board4x4
    print("Unsolved grid:")
    #board_printer.printBoard(mainBoard)

    solveBoard(mainBoard)
    print(" ")

    #print("Solved grid:")
    #board_printer.printBoard(mainBoard)