import pygame

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

        # draws a border around a button
        if thickness:
            pygame.draw.rect(surface, self.color, 
                            (self.x-2,self.y - 2, self.width+4, self.height+4), thickness)

        if self.text != '':
            font = pygame.font.SysFont('calibri', int(self.height))
            text = font.render(self.text, 1, (0, 0, 0))
            surface.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                                self.y + (self.height/2 - text.get_height()/2)+1))

    def click(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False