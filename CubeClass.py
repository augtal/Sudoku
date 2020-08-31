import pygame

HELPER_COLOR = (230, 230, 230)
SELECTED_COLOR = (0, 0, 255)
WRONG_COLOR = (255, 0, 0)
CORRECT_COLOR = (0, 255, 0)
VALUE_COLOR = (0,0,0)
TEMP_VALUE_COLOR = (150, 150, 150)

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
        font_size = int(((self.width / board_size) / 2)* 0.9)  # 90% of half cell size
        font = pygame.font.SysFont("ariel", font_size)

        gap_x = self.width / board_size
        gap_y = self.height / board_size

        x = self.col * gap_x
        y = self.row * gap_y

        rectan = pygame.rect.Rect(
            (x, 
            y, 
            gap_x, 
            gap_y
            )
        )

        #highlights helper cubes for example row, col, grid of selected cube
        if self.helper:
            pygame.draw.rect(screen, HELPER_COLOR, rectan)

        # draws value if the cube has a value or entered temporary value is correct
        if self.value != 0 or self.correct:
            cube_text = font.render(str(self.value), 1, VALUE_COLOR)

            x_value = gap_x/2 - cube_text.get_width()/2
            y_value = gap_y/2 - cube_text.get_height()/2

            screen.blit(cube_text, (x + x_value, y + y_value))
        # draws a temporary value
        elif self.temp != None:
            cube_text = font.render(str(self.temp), 1, TEMP_VALUE_COLOR)

            x_value = gap_x/2 - cube_text.get_width()/2
            y_value = gap_y/2 - cube_text.get_height()/2

            screen.blit(cube_text, (x + x_value, y + y_value))

        if self.selected:
            pygame.draw.rect(screen, SELECTED_COLOR, rectan, 3)

        # if the entered value is correct paint border (green)
        if self.correct:  
            pygame.draw.rect(screen, CORRECT_COLOR, rectan, 3)
        # if the entered value is wrong paint border (red)
        elif self.correct == False:  
            pygame.draw.rect(screen, WRONG_COLOR, rectan, 3)

    def setValue(self, value):
        self.value = value

    def setTempValue(self, value):
        self.temp = value
