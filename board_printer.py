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

def print_board(board):
    size = len(board)
    if size == 4:
        __printer(board, size/2, size/2)
    elif size == 6:
        __printer(board, size/3, size/2)
    elif size == 9:
        __printer(board, size/3, size/3)
    else:
        print("Unsupported board")