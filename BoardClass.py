from CubeClass import Cube
import pygame

class Board():
    def __init__(self, board, width, height):
        self.board = board
        self.width = width
        self.height = height

        self.size_rows, self.size_cols, self.size_board = self.__getBoardParameters(board)

        self.cubes = self.__makeCubes()
        self.selected_cell = None

    #make a 2D list with cube classes in it for a given size board 
    def __makeCubes(self):
        cubes_all = []
        for x in range(self.size_board):
            cubes_row = []
            for y in range(self.size_board):
                cube = Cube(x, y, self.board[x][y], self.width, self.height)
                cubes_row.append(cube)
            cubes_all.append(cubes_row)
        return cubes_all

    # gets given board size and it's parameters(number of rows and cols(important for 6x6 grid))
    #because it has 2 rows and 3 cols per grid
    def __getBoardParameters(self, board):
        board_size = len(board)
        size = len(board)

        if size == 4:
            return (int(size/2), int(size/2), size)
        elif size == 6:
            return (int(size/3), int(size/2), size)
        elif size == 9:
            return (int(size/3), int(size/3), size)

    #draws the whole game board with lines and cube values
    def draw(self, screen):
        gap_x = self.width / self.size_board
        gap_y = self.height / self.size_board

        # draws cube values
        for x in range(self.size_board):
            for y in range(self.size_board):
                self.cubes[x][y].draw(screen, self.size_board)

        # draws vertical lines
        for i in range(self.size_board+1):
            if i % self.size_cols == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(screen, (0, 0, 0), (i * gap_x, 0),
                                                (i * gap_x, self.height), thick)

        # draws horizontal lines
        for j in range(self.size_board+1):
            if j % self.size_rows == 0 and j != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(screen, (0, 0, 0), (0, j*gap_y),
                                                (self.width, j*gap_y), thick)

    # check if clicked inside the board and returns clicked cube cordinates
    def click(self, mouse_pos):
        if mouse_pos[0] < self.width and mouse_pos[1] < self.height:
            gap = self.width / self.size_board
            x_cord = int(mouse_pos[0] // gap)
            y_cord = int(mouse_pos[1] // gap)
            return (y_cord, x_cord)
        else:
            return None

    #paints helper cubes relative to selected cube
    def setHelperCells(self, y_cord, x_cord, condition):
        # paints row
        for x in range(self.size_board):
            self.cubes[y_cord][x].helper = condition

        # paints column
        for y in range(self.size_board):
            self.cubes[y][x_cord].helper = condition

        # paints grid
        x_box = x_cord // self.size_rows
        y_box = y_cord // self.size_cols
        for i in range(y_box*self.size_cols, y_box*self.size_cols+self.size_cols):
            for j in range(x_box*self.size_rows, x_box*self.size_rows+self.size_rows):
                self.cubes[i][j].helper = condition

    #finds selected cube
    def selectedCell(self, y_cord, x_cord):
        selected_cube = self.cubes[y_cord][x_cord]
        old_y, old_x = self.selected_cell
        selected_old_cube = self.cubes[old_y][old_x]

        # first selected cell
        if self.selected_cell is None:
            selected_cube.selected = True
            self.selected_cell = (y_cord, x_cord)
            self.setHelperCells(y_cord, x_cord, True)
        # other selected cell after the first one
        else:
            selected_old_cube.selected = False
            selected_old_cube.correct = None
            self.setHelperCells(old_y, old_x, False)

            selected_cube.selected = True
            self.selected_cell = (y_cord, x_cord)
            self.setHelperCells(y_cord, x_cord, True)

    # when pressed a key(enter) on a cube with a temp value it checks if it can placed
    # by comparing it to a value in the same place on a solved board 
    def placeValue(self, solved_board):
        y_cord, x_cord = self.selected_cell
        selected_cube = self.cubes[y_cord][x_cord]

        if selected_cube.value == 0:
            value = selected_cube.temp

            if value == solved_board[y_cord][x_cord]:
                selected_cube.setValue(value)
                selected_cube.correct = True
            else:
                selected_cube.temp = None
                selected_cube.correct = False

    #sketches a temporary value on a selected cube
    def placeTempValue(self, value):
        y_cord, x_cord = self.selected_cell
        selected_cube = self.cubes[y_cord][x_cord]

        # can't sketch over an existing value
        if selected_cube.value != 0:
            return

        # if the cell value is empty
        if selected_cube.temp == None:  
            selected_cube.setTempValue(value)
        # if the cell already has a temp value
        elif selected_cube.temp != None:
            selected_cube.setTempValue(value)