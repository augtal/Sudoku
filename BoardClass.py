from CubeClass import Cube
import pygame

class Board():
    def __init__(self, board, width, height):
        self.board = board
        self.width = width
        self.height = height

        self.size_rows, self.size_cols, self.size_board = self.__getBoardParameters(
            board)

        self.cubes = self.__makeCubes()
        self.selected_cell = None

    def __makeCubes(self):
        cubes_all = []
        for x in range(self.size_board):
            cubes_row = []
            for y in range(self.size_board):
                cube = Cube(x, y, self.board[x][y], self.width, self.height)
                cubes_row.append(cube)
            cubes_all.append(cubes_row)
        return cubes_all

    def __getBoardParameters(self, board):
        board_size = len(board)
        size = len(board)

        if size == 4:
            return (int(size/2), int(size/2), size)
        elif size == 6:
            return (int(size/3), int(size/2), size)
        elif size == 9:
            return (int(size/3), int(size/3), size)

    def draw(self, screen):
        gap = self.width / self.size_board

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
            pygame.draw.line(screen, (0, 0, 0), (i * gap, 0),
                             (i * gap, self.height), thick)

        # draws horizontal lines
        for j in range(self.size_board+1):
            if j % self.size_rows == 0 and j != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(screen, (0, 0, 0), (0, j*gap),
                             (self.width, j*gap), thick)

    def click(self, mouse_pos):
        # check if clicked inside the board
        if mouse_pos[0] < self.width and mouse_pos[1] < self.height:
            gap = self.width / self.size_board
            x_cord = int(mouse_pos[0] // gap)
            y_cord = int(mouse_pos[1] // gap)
            return (y_cord, x_cord)
        else:
            return None

    def setHelperCells(self, y_cord, x_cord, condition):
        # rows
        for x in range(self.size_board):
            self.cubes[y_cord][x].helper = condition

        # cols
        for y in range(self.size_board):
            self.cubes[y][x_cord].helper = condition

        x_box = x_cord // self.size_rows
        y_box = y_cord // self.size_cols
        for i in range(y_box*self.size_cols, y_box*self.size_cols+self.size_cols):
            for j in range(x_box*self.size_rows, x_box*self.size_rows+self.size_rows):
                self.cubes[i][j].helper = condition

    def selectedCell(self, y_cord, x_cord):
        # first selected cell
        if self.selected_cell is None:
            self.cubes[y_cord][x_cord].selected = True
            self.selected_cell = (y_cord, x_cord)
            self.setHelperCells(y_cord, x_cord, True)
        # other selected cell after the first one
        else:
            old_y, old_x = self.selected_cell
            self.cubes[old_y][old_x].selected = False
            self.cubes[old_y][old_x].correct = None
            self.setHelperCells(old_y, old_x, False)

            self.cubes[y_cord][x_cord].selected = True
            self.selected_cell = (y_cord, x_cord)
            self.setHelperCells(y_cord, x_cord, True)

    def placeValue(self, solved_board):
        y_cord, x_cord = self.selected_cell
        if self.cubes[y_cord][x_cord].value == 0:
            value = self.cubes[y_cord][x_cord].temp

            if value == solved_board[y_cord][x_cord]:
                self.cubes[y_cord][x_cord].setValue(value)
                self.cubes[y_cord][x_cord].correct = True
            else:
                self.cubes[y_cord][x_cord].temp = None
                self.cubes[y_cord][x_cord].correct = False

    def placeTempValue(self, value):
        y_cord, x_cord = self.selected_cell

        if self.cubes[y_cord][x_cord].value != 0:
            return

        if self.cubes[y_cord][x_cord].temp == None:  # if the cell value is empty
            self.cubes[y_cord][x_cord].setTempValue(value)
        # if the cell already has a temp value
        elif self.cubes[y_cord][x_cord].temp != None:
            self.cubes[y_cord][x_cord].setTempValue(value)