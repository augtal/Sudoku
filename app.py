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
        #user_decision = str(input("Would you like to input a board(Yes/No): "))
        user_decision = 'y'

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
            while True:
                user_first_line = input("> ")
                first_line = re.findall(r'\d+', user_first_line)
                if checkInput(first_line, 9):
                    board.append(first_line)
                    break

            i = 1
            board_size = len(first_line)
            while i < board_size:
                user_line = input("> ")
                line = re.findall(r'\d+', user_line)
                if checkInput(line, board_size):
                    board.append(line)
                    i+=1

            mainBoard = board


        if mainBoard is not None:
            print("Unsolved grid:")
            board_printer.printBoard(mainBoard)

            solver.solve(mainBoard)
            print(" ")

            print("Solved grid:")
            board_printer.printBoard(mainBoard)
            break