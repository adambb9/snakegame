#The aim is to recreate the traditional snake game with some new features

#requires a colour package



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

    def snake_movement(self, keypressed):
        #use keyboard strokes to guide direction of snake

        pass

    def eat_apple(self):
        pass

    def draw_body_sqaures(self):
        pass

    def snake_dies(self):
        #if position of snake head is the same as another part of snake body or of boarder
        #snake dies
        pass



