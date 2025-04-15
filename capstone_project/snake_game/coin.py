""" Class that determines all properties of the coin """
import pygame
import random

class Coin():

    def __init__(self):
        self.x = 365
        self.y = 140
        self.size = 35

    def random_xy(self,snake_loc):        
        while True:
            random_x = random.randint(0,16) * 45 + 5
            random_y = random.randint(0,16) * 45 + 5

            if (random_x,random_y) in snake_loc:
                continue
            else:
                break

        self.x = random_x
        self.y = random_y            

    def draw_coin(self,screen):
        pygame.draw.rect(screen, (255, 191, 28), (self.x, self.y, self.size, self.size))
        pygame.draw.rect(screen, "yellow", (self.x + 5,self.y + 5,self.size - 10,self.size - 10))
        
    def coin_reset(self):
        self.x = 365
        self.y = 140

