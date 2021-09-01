#The aim is to recreate the traditional snake game with some new features

import pygame

#box drawing package


#Create a 2D container to hold the game
    #class 
    #Container has a width and a height
    #Container needs to be drawn
    #Lines of container have a colour, a thickness
    #Container will need to be redrawn every time the loop starts

class Container:

    def __init__(self, width, height):
        self.width = width
        self.height = height


    def draw_container(self):
        pass