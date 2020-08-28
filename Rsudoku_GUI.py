import tkinter


def __makeGrid(board, main_Frame, size_grid, size_row, size_column):
    frames = {}
    for row in range(3):
        for col in range(3):
            frame = tkinter.Frame(main_Frame, borderwidth=1, padx=0, pady=0)
            frame.grid(row=row, column=col)
            frames[(row, col)] = frame

    cells = {}
    for row in range(size_grid):
        for col in range(size_grid):
            if board[row][col] == 0:
                cell = tkinter.Entry(frames[(row // size_row, col//size_column)], borderwidth=0.5,
                                     width=3, justify="center", relief="solid")
            else:
                cell = tkinter.Label(frames[(row // size_row, col//size_column)], borderwidth=0.5,
                                     width=3, justify="center", relief="solid", background="white", text=str(board[row][col]))

            cell.grid(row=row % size_row, column=col % size_column)
            cells[(row, col)] = cell


def __evaluateBoard(board):
    size = len(board)
    if size == 4:
        return (size, int(size/2), int(size/2))
    elif size == 6:
        return (size, int(size/3), int(size/2))
    elif size == 9:
        return (size, int(size/3), int(size/3))


def draw(board):
    root = tkinter.Tk()
    root.title("Sudoku solver")

    size_grid, size_row, size_column = __evaluateBoard(board)

    mainFrame = tkinter.Frame(root, bg='white', bd=5)
    mainFrame.place(relx=.5, rely=.5, anchor="center")

    __makeGrid(board, mainFrame, size_grid, size_row, size_column)

    root.mainloop()
