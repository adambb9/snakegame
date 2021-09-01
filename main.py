#The aim is to recreate the traditional snake game with some new features

#requires a colour package
#box drawing package
import pygame



#GLOBAL VARIABLES
#width/height of container
WIDTH, HEIGHT = 900, 500

#Container
CONTAINER = pygame.Rect(WIDTH//2-5, 0, 10, HEIGHT)

#colours
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

FPS = 60

def draw_window(snake_points, apple, snake_head, snake_body=[]):
    #container
    #snake_score
    #surface.blit(snake_points)
    #apple
    #surface.blit(apple)
    #snake_head
    #surface.blit(snake_head)
    #snake_body
    #surface.blit(snake_body)
    #pygame.display.update()
    pass

def snake_movement(keys_pressed, snake):
    #if keys_pressed[pygame.K_LEFT]: # LEFT
        #snake.x -= VEL
    #if keys_pressed[pygame.K_RIGHT]: # RIGHT
        #snake.x += VEL
    #if keys_pressed[pygame.K_UP]: # UP
        #snake.y -= VEL
    #if keys_pressed[pygame.K_DOWN]: # DOWN
        #snake.y += VEL
    pass

while True:
    #draw container 
    #draw apple
    #draw snake
    pass


#Main game loop
#game speed/time