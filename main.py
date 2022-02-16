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
BALL_RADIUS = 8

FPS = 60

# Paddle dimensions
PADDLE_HEIGHT = 100
PADDLE_WIDTH = 20

#color variables
DARKBLUE = (44, 60, 148)
LIGHTBLUE = (120, 135, 224)
WHITE = (245, 246, 255)
GOLD = (224, 200, 121)

WINNING_SCORE = 7

SCORE_FONT  = pygame.font.SysFont('javanesetext', 40)

def draw(win, paddles, ball, left_score, right_score):
    win.fill(DARKBLUE)
    
    left_score_text = SCORE_FONT.render(f"{left_score}", 1, GOLD)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, GOLD)
    win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
    win.blit(right_score_text, (WIDTH * (3/4) - right_score_text.get_width()//2, 20))
    
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
        
def handle_collision(ball, left_p, right_p):
    # ceiling collision
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1
        
    
    if ball.x_vel < 0:
        if ball.y >= left_p.y and ball.y <= left_p.y + left_p.height:
            if ball.x - ball.radius <= left_p.x + left_p.width:
                 ball.x_vel *= -1
                 
                 middle_y = left_p.y + left_p.height / 2
                 difference_in_y = middle_y - ball.y
                 reduction_factor = (left_p.height / 2) / ball.MAX_VEL
                 y_vel = difference_in_y / reduction_factor
                 ball.y_vel = -1 * y_vel
    else:
        if ball.y >= right_p.y and ball.y <= right_p.y + right_p.height:
            if ball.x + ball.radius >= right_p.x:
                ball.x_vel *= -1
                
                middle_y = right_p.y + right_p.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_p.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel
            
def main():
    run = True
    clock = pygame.time.Clock()
    
    ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS)
    
    left_p = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_p = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    
    left_score = 0
    right_score = 0
    
    while run:
        # set frames so each computer is running on same speed
        clock.tick(FPS)
        
        draw(WIN, [left_p, right_p], ball, left_score, right_score)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
                
        keys = pygame.key.get_pressed()        
        handle_paddle_movement(keys, left_p, right_p)
        handle_collision(ball, left_p, right_p)
        
        ball.move()
        
        if ball.x < 0:
            right_score +=1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()
        
        gameover = False
        
        if left_score >= WINNING_SCORE:
            gameover = True
            win_text = "PLayer One Won!"
         
        elif right_score >= WINNING_SCORE:
            gameover = True
            win_text = "Player Two won!"
            
        if gameover:
            text = SCORE_FONT.render(win_text, 1, GOLD)
            WIN.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(4000)
            ball.reset()
            left_p.reset()
            right_p.reset()
            left_score = 0 
            right_Score = 0    
        
    pygame.quit()
    
if __name__ == '__main__':
    main()