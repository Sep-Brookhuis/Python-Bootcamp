""" This script runs a simple snake game with the use of pygame """
from background import create_background
from snake import Snake 
from coin import Coin
import pygame

# Pygame setup
pygame.init()
screen_size = (765,765)
screen = pygame.display.set_mode(screen_size)
background = create_background()
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
latest_key_pressed = None
score = 0
running = True

# Initialize snake
snake = Snake()
# Initialize coin
coin = Coin()


# Kick off game loop
while running:

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_UP and latest_key_pressed != "DOWN":     
                latest_key_pressed = "UP"
            elif event.key == pygame.K_DOWN and latest_key_pressed != "UP":
                latest_key_pressed = "DOWN"
            elif event.key == pygame.K_LEFT and latest_key_pressed != "RIGHT":
                latest_key_pressed = "LEFT"
            elif event.key == pygame.K_RIGHT and latest_key_pressed != "LEFT":
                latest_key_pressed = "RIGHT"
              
    # Fill screen with background
    screen.blit(background,(0,0))

    if snake.x in [xy for xy in range(5,765,45)] and snake.y in [xy for xy in range(5,765,45)]:
        snake.direction = latest_key_pressed
    
    # State snake and coin mechanics
    coin.draw_coin(screen)
    snake.draw_snake(screen)  
    snake.move()

    # Snake and coin collision logic
    coin_rect = pygame.Rect(coin.x,coin.y,coin.size,coin.size)
    snake_rect = pygame.Rect(snake.x,snake.y,snake.size,snake.size)
    if snake_rect.colliderect(coin_rect):
        snake.length += 9
        coin.random_xy(snake.body)
        score += 1

    # Handles restart when player touches screen border
    if snake_rect.y == 0 or snake_rect.y == 730 or snake_rect.x == 0 or snake_rect.x == 730:
        snake.snake_reset()
        coin.coin_reset()
        latest_key_pressed = None
    
    # Handles restart when player head touches snake body
    if snake.body[0] in snake.body[1:]:
        snake.snake_reset()
        coin.coin_reset()
        latest_key_pressed = None
        

    # Put things on the screen
    pygame.display.flip()

    clock.tick(60)
    

pygame.quit()
  
