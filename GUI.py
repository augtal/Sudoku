import pygame
import sys
import random
import sudoku_solver
import board_printer

pygame.font.init()

window_WIDTH, window_HEIGHT = 900, 900
screen = pygame.display.set_mode((window_WIDTH, window_HEIGHT))
pygame.display.set_caption("Sudoku")
screen.fill((255, 255, 255))
FPS = 10


class Cube():
    def __init__(self, col, row, value, width, height):
        self.row = row
        self.col = col
        self.value = value
        self.width = width
        self.height = height
        self.selected = False
        self.temp = None

    def draw(self, screen, board_size):
        font_size = int(((self.width / board_size) / 2)
                        * 0.9)  # 90% of half cell size
        font = pygame.font.SysFont("ariel", font_size)

        gap = self.width / board_size

        x = self.col * gap
        y = self.row * gap

        if not(self.temp == None):
            cube_text = font.render(str(self.temp), 1, (150, 150, 150))
            x_value = gap/2 - cube_text.get_width()/2
            y_value = gap/2 - cube_text.get_height()/2

            screen.blit(cube_text, (x + x_value, y + y_value))
        elif not(self.value == 0):
            cube_text = font.render(str(self.value), 1, (0, 0, 0))
            x_value = gap/2 - cube_text.get_width()/2
            y_value = gap/2 - cube_text.get_height()/2

            screen.blit(cube_text, (x + x_value, y + y_value))

        if self.selected:
            pygame.draw.rect(screen, (0, 0, 255), (x, y, gap, gap), 3)

    def setValue(self, value):
        self.value = value

    def setTempValue(self, value):
        self.temp = value


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

        # draws cube values
        for x in range(self.size_board):
            for y in range(self.size_board):
                self.cubes[x][y].draw(screen, self.size_board)

    def click(self, mouse_pos):
        # check if clicked inside the board
        if mouse_pos[0] < self.width and mouse_pos[1] < self.height:
            gap = self.width / self.size_board
            x_cord = int(mouse_pos[0] // gap)
            y_cord = int(mouse_pos[1] // gap)
            return (x_cord, y_cord)
        else:
            return None

    def selectedCell(self, x_cord, y_cord):
        if self.selected_cell is None:
            self.cubes[x_cord][y_cord].selected = True
            self.selected_cell = (x_cord, y_cord)
        else:
            old_x, old_y = self.selected_cell
            self.cubes[old_x][old_y].selected = False
            self.cubes[x_cord][y_cord].selected = True
            self.selected_cell = (x_cord, y_cord)

    def placeValue(self, value):
        x_cord, y_cord = self.selected_cell
        return None

        if self.cubes[x_cord][y_cord].value == 0:
            self.cubes[x_cord][y_cord].setValue(value)

    def placeTempValue(self, value):
        x_cord, y_cord = self.selected_cell

        if self.cubes[x_cord][y_cord].temp == None:
            self.cubes[x_cord][y_cord].setTempValue(value)
        elif self.cubes[x_cord][y_cord].temp != None:
            self.cubes[x_cord][y_cord].setTempValue(value)


def main():
    pygame.init()
    run = True
    key = None
    clock = pygame.time.Clock()

    demo_board = board_printer.boards()[2]
    size_row, size_col = sudoku_solver.findBoardSize(demo_board)

    board = Board(demo_board, window_WIDTH, window_HEIGHT)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                clicked = board.click(mouse_pos)
                if clicked is not None:
                    board.selectedCell(clicked[0], clicked[1])

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    key = 1
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    key = 2
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    key = 3
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    key = 4
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    key = 5
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    key = 6
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    key = 7
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    key = 8
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    key = 9

                board.placeTempValue(key)
                if event.key == pygame.K_RETURN:
                    board.placeValue(key)

                key = None

        screen.fill((255, 255, 255))
        board.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
