import numpy as np
import math
import random
import pygame

FPS = 60

BLACK = (0, 0, 0)
RED = 0xFF0000
WHITE = 0xFFFFFF

WIDTH = 1000
HEIGHT = 800

class Ball:
    def __init__(self, screen):
        self.screen = screen
        self.x = 200
        self.y = 200
        self.r = 10
        self.vx = random.randint(- 10, 10)
        self.vy = random.randint(- 10, 10)
        
    def move(self, motion):
        
        new_x = self.x + self.vx
        new_y = self.y + self.vy
        if self.r < new_x < WIDTH - self.r:
            self.x = new_x
        else:
            self.vx = - self.vx
        self.x += self.vx
        if self.r < new_y < HEIGHT - self.r:
            self.y = new_y
        else:
            self.vy = - self.vy

        self.vx += motion[0]
        self.vy += motion[1]
        
    def draw(self):
        pygame.draw.circle(
            self.screen,
            BLACK,
            (self.x, self.y),
            self.r
        )
    
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

finished = False

ball = Ball(screen)

motion = [0, 0]

while not finished:
    screen.fill(WHITE)
    ball.draw()
        
    pygame.display.update()
    clock.tick(FPS)

    pygame.key.set_repeat(True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                motion[0] = - 0.4
            elif event.key == pygame.K_RIGHT:
                motion[0] = + 0.4
            else:
                motion[0] = 0
            if event.key == pygame.K_UP:
                motion[1] = - 0.4
            elif event.key == pygame.K_DOWN:
                motion[1] = + 0.4
            else:
                motion[1] = 0
                
    ball.move(motion)
    motion = [0, 0]
                
pygame.quit()
