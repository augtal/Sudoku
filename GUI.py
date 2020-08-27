import tkinter

def make_grid(main_Frame, size_grid, size_row, size_column):
    frames={}
    for row in range(3):
        for col in range(3):
            frame = tkinter.Frame(mainFrame,bd=1)
            frame.grid(row=row,column=col)
            frames[(row, col)] = frame

    entries = {}
    for row in range(size_grid):
        for col in range(size_grid):
            entry = tkinter.Label(frames[(row // size_row, col//size_column)],bd=2, width=3, justify="center", text=f"({row},{col})")
            #entry = tkinter.Entry(frames[(row // size_row, col//size_column)],bd=2, width=3, justify="center")
            entry.grid(row=row % size_row, column=col % size_column)
            entries[(row, col)] = entry

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Sudoku solver")
    size_grid = 4
    size_row = 2
    size_column = 2

    mainFrame = tkinter.Frame(root, bg='white',bd=5)
    mainFrame.place(relx=.5, rely=.5, anchor="center")

    make_grid(mainFrame,size_grid, size_row, size_column)

    root.mainloop()