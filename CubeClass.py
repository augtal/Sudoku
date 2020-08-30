import pygame

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
