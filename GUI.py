import pygame
import sys
import random
import sudoku_solver
from ButtonClass import Button
from BoardClass import Board
from CubeClass import Cube


pygame.font.init()

window_WIDTH, window_HEIGHT = 900, 900
GAME_NAME = "Sudoku"
screen = pygame.display.set_mode((window_WIDTH, window_HEIGHT))
pygame.display.set_caption(GAME_NAME)
screen.fill((255, 255, 255))

FPS = 10
GREEN, YELLOW, ORANGE = (146, 208, 80), (255, 217, 102), (244, 176, 132)


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
    

    while run:
        clock.tick(FPS)
        
        buttons = drawMenu()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                for i in range(len(buttons)):
                    for j in range(len(buttons[i])):
                        if buttons[i][j].click(mouse_pos):
                            game(clock, buttons[i][j].board_size, buttons[i][j].text.lower())

        pygame.display.update()


if __name__ == '__main__':
    main()
