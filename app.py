import board_printer
import sudoku_solver as solver
import re

def checkInput(number_list, board_size):
    for number in number_list:
        if(int(number) > board_size):
            print(f"Number {number} is too big")
            return False
    return True

if __name__=="__main__":
    mainBoard = None

    while True:
        user_decision = str(input("Would you like to input a board(Yes/No): "))

        if user_decision[0].lower() == 'n':
            user_board_size = str(input("What size sudoku board?(4x4/6x6/9x9): "))
            if user_board_size[0] == '4':
                mainBoard = board_printer.boards()[0]
            elif user_board_size[0] == '6':
                mainBoard = board_printer.boards()[1]
            elif user_board_size[0] == '9':
                mainBoard = board_printer.boards()[2]
            else:
                print(f"Incorrect size {user_board_size}")
                break

        elif user_decision[0].lower() == 'y':
            board = []
            print("Empty cell should be marked as 0")
            print("Seperate cell values with a space or delimeter(,/./;)")
            i = 1
            board_size = 9
            while i < board_size-1:
                if len(board) == 1:             #if user already inputed first sudoku board line
                    if len(board[0]) < 9:       #if the board is smaller then 9x9
                        i = 9-len(board[0])     #add the size difference to the i

                user_line = input("> ")
                line = re.findall(r'\d+', user_line)
                if checkInput(line, board_size):
                    board.append(line)
                    i+=1
            
            mainBoard = board

        if mainBoard is not None:
            print("Unsolved grid:")
            board_printer.printBoard(mainBoard)

            solvedBoard = solver.solve(mainBoard)
            print(" ")

            print("Solved grid:")
            board_printer.printBoard(solvedBoard)
            break