import pygame
import sys
import random
import sudoku_solver
from ButtonClass import Button
from BoardClass import Board
from CubeClass import Cube


pygame.font.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 900, 900
GAME_NAME = "Sudoku"

SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(GAME_NAME)
SCREEN.fill((255, 255, 255))

GRIDS = ["GRID 4X4", "GRID 6X6", "GRID 9X9"]
FPS = 10
GREEN, YELLOW, ORANGE, BLACK = (146, 208, 80), (255, 217, 102), (244, 176, 132), (0,0,0)

#checks what input was gived
def gameControls(event, board, solved_board):
    key = None

    #checks mouse input and determins if the user click on a cube
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        clicked = board.click(mouse_pos)
        if clicked is not None:
            board.selectedCell(clicked[0], clicked[1])

    #checks what key a user pressed
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

        #only if a user pressed a number key scrible in a temporary value at that place
        if key != None:
            board.placeTempValue(key)

        #tries to place temporary value into the board to make a permenant value
        if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
            board.placeValue(solved_board)

        key = None

#game window
def game(clock, size, difficulty):
    run = True

    sudoku_board, solved_board = sudoku_solver.generateBoard(size, difficulty)
    board = Board(sudoku_board, WINDOW_WIDTH, WINDOW_HEIGHT)

    while run:
        clock.tick(FPS)
        SCREEN.fill((255, 255, 255))

        
        for event in pygame.event.get():
            #if the user pressed X or esc they return back to main menu
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            gameControls(event, board, solved_board)

        board.draw(SCREEN)
        pygame.display.update()

# draws the main menu and returns buttons list
def drawMenu():
    SCREEN.fill((250, 250, 250))

    gap_x = WINDOW_WIDTH / 20
    gap_y = WINDOW_HEIGHT / 20

    # menu
    menu_font = pygame.font.SysFont('ariel', int(gap_y*2))
    menu_text = menu_font.render(GAME_NAME.capitalize(), 1, (0, 0, 0))
    SCREEN.blit(menu_text, (WINDOW_WIDTH/2 - menu_text.get_width()/2, gap_y+gap_y/2))#dictionary for buttons
    
    # game options
    colors = {
        0: [GREEN, "EASY"],
        1: [YELLOW, "NORMAL"],
        2: [ORANGE, "HARD"]
    }

    grid_font = pygame.font.SysFont('ariel', int(gap_y))

    buttons = []
    # draws 3 rectangles because we have 3 grids
    for i in range(1,len(GRIDS)+1):
        rect_cords = pygame.rect.Rect(
            ((WINDOW_WIDTH/2) - (gap_x * 8)),
            (gap_y*(5*i)),  # this is the reason it starts at one
            (WINDOW_WIDTH-(gap_x*4)),
            (gap_y*4)
        )
        grid_rect = pygame.draw.rect(SCREEN, BLACK, rect_cords, 4)

        grid_text = grid_font.render(GRIDS[i-1], 1, BLACK)
        SCREEN.blit(grid_text, (WINDOW_WIDTH/2 - grid_text.get_width()/2, rect_cords.y+gap_y/4))

        size = int(GRIDS[i-1][-1])

        
        # draws 3 buttons
        for j in range(3):
            button_cords = [
                (rect_cords.x + (gap_x + (gap_x*(5*j)))),
                (rect_cords.y+gap_y*2),
                (gap_x*4),
                (gap_y)
            ]
            button = Button(colors[j][0], button_cords[0], button_cords[1], button_cords[2], 
                            button_cords[3], size, text=colors[j][1])

            button.draw(SCREEN)

            buttons.append(button)

    return buttons


def main():
    pygame.init()
    run = True
    clock = pygame.time.Clock()
    
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
                    if buttons[i].click(mouse_pos):
                        game(clock, buttons[i].board_size, buttons[i].text.lower())

        pygame.display.update()


if __name__ == '__main__':
    main()
