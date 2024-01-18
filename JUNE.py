import random, copy, sys, pygame
from pygame.locals import *

BOARDWIDTH=7
BOARDHEIGHT=6

SPACESIZE=50

FPS=30
WINDOWWIDTH=640
WINDOWHEIGHT=480

XMARGIN=int(WINDOWWIDTH-BOARDWIDTH*SPACESIZE/2)
YMARGIN=int(WINDOWHEIGHT-BOARDHEIGHT*SPACESIZE/2)

BLUE=(158,210,143)
WHITE=(88,199,195)

pygame.init()
FPSCLOCK=pygame.time.Clock()
DISPLAYSURF=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption("A Game We Call...")

SIDE1=pygame.Rect(int(SPACESIZE/2), WINDOWHEIGHT-int(3*SPACESIZE/2),SPACESIZE,SPACESIZE)
SIDE2=pygame.Rect(int(SPACESIZE/2), WINDOWHEIGHT-int(3*SPACESIZE/2),SPACESIZE,SPACESIZE)

                          
DISPLAYSURF.fill(BLUE)
spaceRect=pygame.Rect(0,0,SPACESIZE,SPACESIZE)
for x in range(BOARDWIDTH):
    for y in range(BOARDHEIGHT):
        spaceRect.topleft = (XMARGIN + (x * SPACESIZE), YMARGIN + (y * SPACESIZE))

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    
