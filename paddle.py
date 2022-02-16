import pygame

WHITE = (245, 246, 255)

class Paddle:
    COLOR = WHITE
    VEL = 8
    
    def __init__(self, x, y, width, height):
        self.x = original_x = x
        self.y = original_y = y
        self.width = width
        self.height = height
        
    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))
        
    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL
            
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y