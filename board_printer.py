def __printer(board,sizeRow,sizeCol):
    lineBreaker = 0
    for row in enumerate(board):
        row_string = "| "
        lineBreaker += 1
        for i in range(0, len(row[1])):
            row_string = row_string + str(row[1][i]) +  " "

            if (i+1)%sizeCol == 0:
                row_string = row_string + "| "

        if row[0] == 0:
            print("-"*(len(row_string)-1))

        print(row_string)

        if lineBreaker%sizeRow == 0:
            print("-"*(len(row_string)-1))

def printBoard(board):
    size = len(board)
    if size == 4:
        __printer(board, size/2, size/2)
    elif size == 6:
        __printer(board, size/3, size/2)
    elif size == 9:
        __printer(board, size/3, size/3)
    else:
        print("Unsupported board")

def boards():
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

    return (board4x4,board6x6,board9x9)