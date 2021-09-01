#The aim is to recreate the traditional snake game with some new features
#box drawing package

import pygame



pygame.init()

#global width and height variables
WIDTH, HEIGHT = 1300, 700

#draw a surface
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))

#global colour variables
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

#dimensions and position of rectangle, later to be snake/apple body
RECT = pygame.Rect(650, 350, 80, 80)

# Drawing Rectangle
pygame.draw.rect(SURFACE, YELLOW, RECT)
pygame.display.flip()

#Create a 2D container to hold the game
    #class 
    #Container has a width and a height
    #Container needs to be drawn
    #Lines of container have a colour, a thickness
    #Container will need to be redrawn every time the loop starts

#class Container:

    #def __init__(self, width, height):
        #self.width = width
        #self.height = height


    #def draw_container(self):
        #pass