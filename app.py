import board_printer

def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]==0:
                return (row,col)
    return (-1,-1)


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