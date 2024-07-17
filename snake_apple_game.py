import pygame
import time
from pygame.locals import *

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block  = pygame.image.load("resources/block.jpg").convert()
        self.x =100
        self.y =100

    def draw(self):
        self.surface.fill((110,110,5))
        self.parent_screen.bilt(self.block, (self.x,self.y))
        pygame.display.flip()

    def move_left(self):
        self.x -= 10
        self.draw()
    def move_right(self):
        self.x += 10
        self.draw()
    def move_up(self):
        self.y -= 10
        self.draw()
    def move_down(self):
        self.y += 10
        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        self.surface.fill((110,110,5))
        self.snake = Snake(self.surface)
        self.snake.draw()


    def run():
        pass
          

        



def draw_block():
    surface.fill((110,110,5))
    
    surface.blit(block, (block_x,block_y))
    pygame.display.flip()



if __name__ == "__main__":
    

    
    surface.fill((110,110,5))
    
    block_x = 100
    block_y = 100
    surface.blit(block, (block_x,block_y))




    pygame.display.flip()


    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()

            elif event.type == QUIT:
                running = False