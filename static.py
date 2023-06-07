"""Creates static"""
import pygame
from random import randint

def drawVertex(x, y):
    """Function for drawing a vertex"""
    return pygame.draw.circle(screen, RED, (x,y), 3)

def plotPoints():
    listofPoints = []
    for i in range(50000):
        listofPoints.append(pygame.draw.circle(screen, BLACK, (randint(MIN_X, MAX_X), randint(MIN_Y, MAX_Y)), 2))
    return listofPoints

SIZE = 600
MID_X = SIZE/2
MIN_X = 2
MAX_X = 598
MIN_Y = 2
MAX_Y = 598
RED = (255, 0, 0) 
BLACK = (0, 0, 0)       
pygame.init()
screen = pygame.display.set_mode((SIZE, SIZE), pygame.SCALED)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255,255))
screen.blit(background, (0,0))
pygame.display.flip()
clock = pygame.time.Clock()
going = True

while going:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False

    screen.blit(background, (0,0))
    drawVertex(MID_X, MIN_Y)
    drawVertex(MIN_X, MAX_Y)
    drawVertex(MAX_X, MAX_Y)
    plotPoints()
    pygame.display.flip()
    