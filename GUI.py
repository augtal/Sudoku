import pygame
import sys
import random
import sudoku_solver
import board_printer

pygame.font.init()

window_WIDTH, window_HEIGHT = 900, 900
GAME_NAME = "Sudoku"
screen = pygame.display.set_mode((window_WIDTH, window_HEIGHT))
pygame.display.set_caption(GAME_NAME)
screen.fill((255, 255, 255))

FPS = 10
GREEN, YELLOW, ORANGE = (146, 208, 80), (255, 217, 102), (244, 176, 132)


class Cube():
    def __init__(self, row, col, value, width, height):
        self.row = row
        self.col = col
        self.value = value
        self.width = width
        self.height = height
        self.selected = False
        self.temp = None
        self.correct = None
        self.helper = None

    def draw(self, screen, board_size):
        font_size = int(((self.width / board_size) / 2)
                        * 0.9)  # 90% of half cell size
        font = pygame.font.SysFont("ariel", font_size)

        gap = self.width / board_size

        x = self.col * gap
        y = self.row * gap

        if self.helper:
            pygame.draw.rect(screen, (230, 230, 230), (x, y, gap, gap))

        if self.value != 0 or self.correct:
            cube_text = font.render(str(self.value), 1, (0, 0, 0))
            x_value = gap/2 - cube_text.get_width()/2
            y_value = gap/2 - cube_text.get_height()/2
            screen.blit(cube_text, (x + x_value, y + y_value))
        elif self.temp != None:
            cube_text = font.render(str(self.temp), 1, (150, 150, 150))
            x_value = gap/2 - cube_text.get_width()/2
            y_value = gap/2 - cube_text.get_height()/2
            screen.blit(cube_text, (x + x_value, y + y_value))

        if self.selected:
            pygame.draw.rect(screen, (0, 0, 255), (x, y, gap, gap), 3)

        if self.correct:  # if the entered value is correct paint border green
            pygame.draw.rect(screen, (0, 255, 0), (x, y, gap, gap), 3)
        elif self.correct == False:  # if the entered value is wrong paint border red
            pygame.draw.rect(screen, (255, 0, 0), (x, y, gap, gap), 3)

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


def gameControls(event, board, solved_board):
    key = None

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

        if key != None:
            board.placeTempValue(key)

        if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
            board.placeValue(solved_board)

        key = None


def game(clock, size, difficulty):
    run = True

    sudoku_board, solved_board = sudoku_solver.generateBoard(size, difficulty)
    board = Board(sudoku_board, window_WIDTH, window_HEIGHT)

    while run:
        clock.tick(FPS)
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            gameControls(event, board, solved_board)

        board.draw(screen)
        pygame.display.update()


class Button():
    def __init__(self, color, x, y, width, height, size, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.board_size = size

    def draw(self, surface, thickness=None):
        pygame.draw.rect(surface, self.color,
                         (self.x, self.y, self.width, self.height))

        if thickness:
            pygame.draw.rect(surface, self.color, (self.x-2,
                                                   self.y - 2, self.width+4, self.height+4), thickness)

        if self.text != '':
            font = pygame.font.SysFont('calibri', int(self.height))
            text = font.render(self.text, 1, (0, 0, 0))
            surface.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                                self.y + (self.height/2 - text.get_height()/2)+1))

    def click(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


def drawMenu():
    screen.fill((250, 250, 250))

    gap_x = window_WIDTH / 20
    gap_y = window_HEIGHT / 20

    # menu
    menu_font = pygame.font.SysFont('ariel', int(gap_y*2))
    menu_text = menu_font.render(GAME_NAME.capitalize(), 1, (0, 0, 0))
    screen.blit(menu_text, (window_WIDTH/2 - menu_text.get_width()/2, gap_y+gap_y/2))

    colors = {
        0: [GREEN, "EASY"],
        1: [YELLOW, "NORMAL"],
        2: [ORANGE, "HARD"]
    }

    grid_font = pygame.font.SysFont('ariel', int(gap_y))

    buttons = []
    button_row = []
    # blank is needed for the next for loop because it starts at 1
    grids = ["BLANK", "GRID 4X4", "GRID 6X6", "GRID 9X9"]
    # draws a rectangle
    for i in range(4):
        if i == 0:
            continue
        rect_cords = pygame.rect.Rect(
            ((window_WIDTH/2) - (gap_x * 8)),
            (gap_y*(5*i)),  # this is the reason it starts at one
            (window_WIDTH-(gap_x*4)),
            (gap_y*4)
        )
        grid_rect = pygame.draw.rect(screen, (0, 0, 0), rect_cords, 4)

        grid_text = grid_font.render(grids[i], 1, (0, 0, 0))
        screen.blit(grid_text, (window_WIDTH/2 - grid_text.get_width()/2, rect_cords.y+gap_y/4))

        size = int(grids[i][-1])

        button_row = []
        # draws a buttons
        for j in range(3):
            button_cords = [
                (rect_cords.x + (gap_x + (gap_x*(5*j)))),
                (rect_cords.y+gap_y*2),
                (gap_x*4),
                (gap_y)
            ]
            button = Button(colors[j][0], button_cords[0], button_cords[1], button_cords[2], 
                            button_cords[3], size, text=colors[j][1])

            button.draw(screen)

            button_row.append(button)
        buttons.append(button_row)

    return buttons


def main():
    pygame.init()
    run = True
    clock = pygame.time.Clock()
    # game(clock)
    buttons = drawMenu()

    while run:
        clock.tick(FPS)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                for i in range(len(buttons)):
                    for j in range(len(buttons[i])):
                        if buttons[i][j].click(mouse_pos):
                            game(clock, buttons[i][j].board_size, buttons[i][j].text.lower())

        drawMenu()
        pygame.display.update()


if __name__ == '__main__':
    main()
