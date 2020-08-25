def print_board(board):
    lineBreaker = 0
    for row in board:
        row_string = "| "
        lineBreaker += 1
        for i in range(0, len(row)):
            row_string = row_string + str(row[i]) +  " "

            if (i+1)%3 == 0:
                row_string = row_string + "| "

        print(row_string)
        if lineBreaker%3 == 0:
            print("-"*(len(row_string)-1))

def solve(board):
    pass


board = [
    [5,3,0, 0,7,0, 0,0,0],
    [6,0,0, 1,9,5, 0,0,0],
    [0,9,8, 0,0,0, 0,6,0],
    #---------------------
    [8,0,0, 0,6,0, 0,0,3],
    [4,0,0, 8,0,3, 0,0,1],
    [7,0,0, 0,2,0, 0,0,6],
    #---------------------
    [0,6,0, 0,0,0, 2,8,0],
    [0,0,0, 4,1,9, 0,0,5],
    [0,0,0, 0,8,0, 0,7,9],
    ]

solvedBoard = solve(board)
print_board(board)