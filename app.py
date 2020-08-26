import board_printer

def find_empty(board):
    emptyCells = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            emptyList = []
            if board[row][col]==0:
                emptyList.append(row)
                emptyList.append(col)
                emptyCells.append(emptyList)
    return emptyCells

def solve(board):
    emptyCells = find_empty(board)

    print(emptyCells)

board4x4 = [
    [0,2, 0,1],
    [1,4, 0,3],
    #---------
    [2,3, 1,0],
    [0,0, 0,0]
    ]

board6x6 = [
    [4,5,1, 3,0,0],
    [3,0,0, 0,1,5],
    #-------------
    [0,0,4, 0,5,3],
    [0,0,5, 0,0,1],
    #-------------
    [1,2,0, 5,0,4],
    [0,0,3, 1,0,6]
    ]

board9x9 = [
    [0,0,0, 0,6,0, 0,3,0],
    [7,5,9, 0,0,3, 6,4,0],
    [1,0,3, 4,8,0, 9,0,0],
    #---------------------
    [8,7,1, 5,3,2, 4,6,9],
    [0,9,0, 0,7,0, 2,0,0],
    [0,0,0, 9,4,0, 0,8,1],
    #---------------------
    [0,0,7, 0,5,8, 0,0,4],
    [3,0,8, 0,2,0, 0,9,6],
    [0,0,6, 3,0,0, 8,7,0]
    ]

#solvedBoard = solve(board4x4)
board_printer.print_board(board9x9)
