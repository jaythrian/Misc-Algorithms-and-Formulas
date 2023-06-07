"""Creates the Sierpinsky Triangle"""
import pygame
from random import randint, choice

SIZE = 600 # window size is 600x600
MID_X = SIZE/2
MIN_X = 2
MAX_X = 598
MIN_Y = 2
MAX_Y = 598
RED = (255, 0, 0) 
BLACK = (0, 0, 0)    

def drawVertex(x, y):
    """Function for drawing a vertex"""
    return pygame.draw.circle(screen, RED, (x,y), 3)

# pygame boilerplate code   
pygame.init()
screen = pygame.display.set_mode((SIZE, SIZE), pygame.SCALED)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255,255))
screen.blit(background, (0,0))
pygame.display.flip()
clock = pygame.time.Clock()
going = True
########################
# vertex points
v1 = drawVertex(MID_X, MIN_Y)
v2 = drawVertex(MIN_X, MAX_Y)
v3 = drawVertex(MAX_X, MAX_Y)
listofVertex = []
listofPoints = []
listofVertex.append(v1)
listofVertex.append(v2)
listofVertex.append(v3)
vertexChoice = choice(listofVertex) # chooses random rect object out of listofVertex
point = pygame.draw.circle(screen, BLACK, ((MID_X + MIN_X)/2, (MIN_Y + MAX_Y)/2), 2) # the initial midpoint for which the chaos game is played
listofPoints.append(point)

# for loop adds new rect object with its coords to listofPoints
for i in range(50000):
    vertexChoice = choice(listofVertex) # overides the vertexChoice variable in memory
    # vertexChoice[0] choses a random x coord; point[0] is the last point's x coord; [1] is y coord; /2 is for the midpoint formula 
    point = pygame.draw.circle(screen, BLACK, ((vertexChoice[0] + point[0])/2, (vertexChoice[1] + point[1])/2), 2) 
    listofPoints.append(point)


while going:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False

    screen.blit(background, (0,0))
    pygame.draw.rect(screen, RED, v1) # draws vertex to screen
    pygame.draw.rect(screen, RED, v2)
    pygame.draw.rect(screen, RED, v3)
    
    for i in listofPoints:
        pygame.draw.rect(screen, BLACK, i) # draws every rect in listofPoints
    pygame.display.flip()
    
