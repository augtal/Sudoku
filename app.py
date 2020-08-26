import board_printer

def find_empty(board):
    emptyCell = [-1,-1]
    for row in enumerate(board):
        for col in enumerate(row[1]):
            if col[1]==0:
                emptyCell[0] = row[0]
                emptyCell[1] = col[0]
                return emptyCell
    return emptyCell

def solve_board(board):
    emptyCells = find_empty(board)



    print(emptyCells)

if __name__=="__main__":
    board4x4, board6x6, board9x9 = board_printer.boards()

    mainBoard = board4x4
    print("Unsolved grid:")
    board_printer.print_board(mainBoard)

    solvedBoard = solve_board(mainBoard)
    print(" ")

    print("Solved grid:")
    board_printer.print_board(mainBoard)