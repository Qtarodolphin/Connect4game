import random
import copy
import sys
import pygame
from pygame.locals import * 


BOARDWIDTH = 7
BOARDHEIGHT = 6

WINDOWWIDTH=640
WINDOWHEIGHT=480

SPACESIZE=50
FPS=30

BLUE=(224,78,66)
GREEN=(182,33,76)

XMARGIN=int((WINDOWWIDTH-BOARDWIDTH*SPACESIZE)/2)
YMARGIN=int((WINDOWHEIGHT-BOARDHEIGHT*SPACESIZE)/2)

BGCOLOR=BLUE
TEXTCOLOR=GREEN
empty=None

def main():
    global FPSCLOCK,DISPLAYSURF, boardimg

    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    pygame.display.set_caption("Four in a Row")
    DISPLAYSURF=pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    DISPLAYSURF.fill(BGCOLOR)
    mainboard=getBoard()
    boardimg=pygame.image.load("woodb.jpg")
    boardimg=pygame.transform.smoothscale(boardimg, (SPACESIZE, SPACESIZE))
    

    while True:
        drawBoard(mainboard)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
def drawBoard(board):
    spaceRect=pygame.Rect(0,0,SPACESIZE,SPACESIZE)
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            spaceRect.topleft=(XMARGIN+(x*SPACESIZE), YMARGIN+(y*SPACESIZE))
            color=TEXTCOLOR
            if board[x][y]=="red":
                DISPLAYSURF.blit(spaceRect)
            elif board[x][y]=="black":
                DISPLAYSURF.blit(spaceRect)
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            spaceRect.topleft=(XMARGIN+(x*SPACESIZE), YMARGIN+(y*SPACESIZE))
            DISPLAYSURF.blit(boardimg, spaceRect)

def getBoard():
    board=[]
    for x in range(BOARDWIDTH):
        board.append([empty]*BOARDHEIGHT)
    return board


    

main()

