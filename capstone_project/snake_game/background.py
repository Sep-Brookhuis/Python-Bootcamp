""" Function that draws the background layout"""
import pygame

def create_background():

    screen_width = 765
    screen_height = 765
    block_size = 45

    background = pygame.Surface((screen_width,screen_height))

    for row in range(int(screen_width/block_size)):           
        for col in range(int(screen_width/block_size)):
            x = block_size * col
            y = block_size * row

            if (col + row) % 2 == 0:
                color = (45, 156, 23)
            else:
                color = (72, 207, 45)
        
            pygame.draw.rect(background,color,(x,y,block_size,block_size))
    
    return background

    