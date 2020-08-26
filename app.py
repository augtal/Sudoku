import board_printer
import re

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

def validNumber(board, cur_pos, number, size_row, size_col):
    if not __checkRow(board, cur_pos, number):
        return False
    elif not __checkCol(board, cur_pos, number):
        return False
    elif not __checkGrid(board, cur_pos, number, size_row, size_col):
        return False
    else:
        return True

def __solveBoard(board, size_row, size_col):
    empty_cell = findEmpty(board) #returns false if it can't find an empty value

    if not empty_cell:
        return True #found the solution because we have no more empty cells
    else: 
        row_empty, col_empty = empty_cell

    for i in range(1,len(board)+1):
        if(validNumber(board, empty_cell, i, size_row, size_col)):
            board[row_empty][col_empty] = i

            if __solveBoard(board, size_row, size_col):
                return True

            board[row_empty][col_empty] = 0 #resets value to try again

    return False

def solve(board):
    size = len(board)
    if size == 4:
        __solveBoard(board, int(size/2), int(size/2))
    elif size == 6:
        __solveBoard(board, int(size/3), int(size/2))
    elif size == 9:
        __solveBoard(board, int(size/3), int(size/3))
    else:
        print("Unsupported board")

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

            solve(mainBoard)
            print(" ")

            print("Solved grid:")
            board_printer.printBoard(mainBoard)
            break