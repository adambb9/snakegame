#The aim is to recreate the traditional snake game with some new features

#requires a colour package
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

#Create a snake
    #class
    #Snake has a head made out of a rectangle
    #snake has a position on the board
    #Snake eats apples
    #Snake has a changing body size
    #as the snake grows its body follows the tracks of its head
        #create a list keeping track of the last head locations and draw the body sqaures at those positions
    #snake has a starting point on the board
    #if snake bump head first into the wall or its own body the snake dies


class Snake:

    def __init__(self, x_position=0, y_position= 0, colour):
        self.length = 1
        self.colour = colour
        self.x_position = x_position
        self.y_position = y_position
        self.body = [(,)]

    def draw_snake_head(self):
        pass

    def head_xlocation(self):
        pass

    def head_ylocation(self):
        pass

    def eat_apple(self):
        pass

    def draw_body_sqaures(self):
        pass

    def snake_dies(self):
        #if position of snake head is the same as another part of snake body or of boarder
        #snake dies
        pass


#Creat an apple
    #class
    #apple is a rectangle possibly green
    #apple appears around the board at a random location 
    #apple appears around the board at a given time interval
    #apple gets eaten

class Apple:

    def __init__(self, x_position=0, y_position= 0, colour):
        self.colour = colour

    def draw_apple(self):
        pass

#apple disappears from board
    def is_eten(self):
        #position of apple set to none?
        pass



#Main game loop
#game speed/time
