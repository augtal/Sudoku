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
FPS = 30


class Cube():
    def __init__(self, col, row, value, width, height):
        self.row = row
        self.col = col
        self.value = value
        self.width = width
        self.height = height
        self.selected = False
        self.temp = []

    def draw(self, screen, board_size):
        font_size = int(((self.width / board_size) / 2)
                        * 0.9)  # 90% of half cell size
        font = pygame.font.SysFont("ariel", font_size)

        gap = self.width / board_size

        x = self.col * gap
        y = self.row * gap

        if len(self.temp) != 0 and self.value == 0:
            cube_text = font.render(str(self.temp[0]), 1, (128, 128, 128))
            screen.blit(cube_text, (x+5, y+5))
        elif not(self.value == 0):
            cube_text = font.render(str(self.value), 1, (0, 0, 0))
            screen.blit(cube_text, (x + (gap/2 - cube_text.get_width()/2),
                                    y + (gap/2 - cube_text.get_height()/2)))

        if self.selected:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, gap, gap), 2)


class Board():
    def __init__(self, board, width, height):
        self.board = board
        self.width = width
        self.height = height

        self.size_rows, self.size_cols, self.size_board = self.__getBoardParameters(
            board)

        self.model = None
        self.selected = None

        self.cubes = self.__makeCubes()

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
        gap = int(self.width / self.size_board)

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


def main():
    pygame.init()
    run = True
    clock = pygame.time.Clock()

    demo_board = board_printer.boards()[2]
    size_row, size_col = sudoku_solver.findBoardSize(demo_board)

    board = Board(demo_board, window_WIDTH, window_HEIGHT)

    board.draw(screen)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()


if __name__ == '__main__':
    main()
