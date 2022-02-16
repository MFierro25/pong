import pygame
from paddle import Paddle
from ball import Ball
pygame.init()


WIDTH = 900
HEIGHT = 600

# window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

#ball radius
BALL_RADIUS = 12

FPS = 60

# Paddle dimensions
PADDLE_HEIGHT = 100
PADDLE_WIDTH = 20

#color variables
DARKBLUE = (44, 60, 148)
LIGHTBLUE = (120, 135, 224)
WHITE = (245, 246, 255)
GOLD = (224, 200, 121)

def draw(win, paddles, ball):
    win.fill(DARKBLUE)
    
    for paddle in paddles:
        paddle.draw(win)
        
    for i in range(0, HEIGHT, HEIGHT//20):
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 2.5, i, 5, HEIGHT//20))
        
    ball.draw(win)
    
    pygame.display.update()
      
def handle_paddle_movement(keys, left_p, right_p):
    if keys[pygame.K_UP] and right_p.y - right_p.VEL >= 0:
        right_p.move(up=True)
    if keys[pygame.K_DOWN] and right_p.y + right_p.VEL + right_p.height <= HEIGHT:
        right_p.move(up=False)

    if keys[pygame.K_w] and left_p.y - left_p.VEL >= 0:
        left_p.move(up=True)
    if keys[pygame.K_s] and left_p.y + left_p.VEL + left_p.height <= HEIGHT:
        left_p.move(up=False)
        
def main():
    run = True
    clock = pygame.time.Clock()
    
    ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS)
    
    left_p = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_p = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    
    while run:
        # set frames so each computer is running on same speed
        clock.tick(FPS)
        
        draw(WIN, [left_p, right_p], ball)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
                
        keys = pygame.key.get_pressed()        
        handle_paddle_movement(keys, left_p, right_p)
        
    pygame.quit()
    
if __name__ == '__main__':
    main()