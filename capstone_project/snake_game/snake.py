""" Class that determines all properties of the snake """
import pygame

class Snake():

    def __init__(self):
        self.size = 35
        self.speed = 5
        self.x = 365
        self.y = 500
        self.direction = "UP"
        self.body = [(self.x,self.y)]
        self.length = 1


    def move(self):
        if self.direction is None:
            return  
        
        if self.direction == "UP":
            new_head = (self.x, self.y - self.speed)
        elif self.direction == "DOWN":
            new_head = (self.x, self.y + self.speed)
        elif self.direction == "LEFT":
            new_head = (self.x - self.speed, self.y)
        elif self.direction == "RIGHT":
            new_head = (self.x + self.speed, self.y)
        
        self.body.insert(0, new_head)

        if len(self.body) > self.length:
            self.body.pop()
        
        self.x, self.y = self.body[0]


    def draw_snake(self,screen):
        for segment in self.body:
            pygame.draw.rect(screen,"purple",(segment[0],segment[1],self.size,self.size))
   
        eyes_xy = [(self.x,self.y,12.5,12.5),(self.x + 23,self.y,12.5,12.5)]
        pupils_xy = [(self.x,self.y,7.5,7.5),(self.x + 23,self.y,7.5,7.5)]

        if self.direction == "DOWN":
            eyes_xy = [(self.x,self.y + 23,12.5,12.5),(self.x + 23,self.y + 23,12.5,12.5)]
            pupils_xy = [(self.x,self.y + 23,7.5,7.5),(self.x + 23,self.y + 23,7.5,7.5)]

        if self.direction == "LEFT":
            eyes_xy = [(self.x,self.y + 23,12.5,12.5),(self.x,self.y,12.5,12.5)]
            pupils_xy = [(self.x,self.y + 23,7.5,7.5),(self.x,self.y,7.5,7.5)]

        if self.direction == "RIGHT":
            eyes_xy = [((self.x + 23,self.y,12.5,12.5)),(self.x + 23,self.y + 23,12.5,12.5)]
            pupils_xy = [((self.x + 23,self.y,7.5,7.5)),(self.x + 23,self.y + 23,7.5,7.5)]

        for rect in eyes_xy:
            pygame.draw.rect(screen,"white",rect)
        for rect in pupils_xy:
            pygame.draw.rect(screen,"black",rect)


    def snake_reset(self):
        self.direction = "UP"
        self.length = 1
        self.x = 365
        self.y = 500
        self.body = [(self.x, self.y)]
        
        

  
         

    