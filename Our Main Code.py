import random, copy, sys, pygame, itertools
from pygame.locals import *

BOARDWIDTH=int(input("Enter how wide you want the board to be: "))
BOARDHEIGHT=int(input("Enter how high you want the board to be: "))
assert BOARDWIDTH >=4 and BOARDHEIGHT >=4

DIFFICULTY=int(input("Enter AI difficulty: "))

SPACESIZE = 50

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480

XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * SPACESIZE) / 2)
YMARGIN = int((WINDOWHEIGHT - BOARDHEIGHT * SPACESIZE) / 2)

BGCOL=(132,110,200)
TEXTCOL=(98,221,154)


def main():
    global FPSCLOCK, DISPLAYSURF, boardimg, board, tile, SPACERECT, SPACESIZE

    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    DISPLAYSURF=pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Four-In-A-Row Tutorial")
    #boardimg=pygame.image.load("woodb.jpg")
    #boardimg=pygame.transform.smoothscale(boardimg, (SPACESIZE, SPACESIZE))
    pygame.display.update()
    FPSCLOCK.tick()
    runGame()
  
    

        
def runGame():
    while True:
        humanTile, computerTile=enterHumanTile()
        turn=firstMove()
        print("The "+turn+" player will go first. ")
        mainBoard=getNewBoard()
        drawBoard(mainBoard)
        pygame.display.update()

        while True:
            if turn=="human":
                drawBoard(mainBoard)
                move=getHumanMove(mainBoard, humanTile)
                if isWinner(mainBoard, humanTile):
                    winner="human"
                    break
                print(isWinner(mainBoard, humanTile))
                turn="computer"

            else:
                drawBoard(mainBoard)
                move=getComputerMove(mainBoard, computerTile)
                drawMove(board,computerTile,*move)
                if isWinner(mainBoard, computerTile):
                    winner="computer"
                    break
                print(isWinner(mainBoard, computerTile))
                turn="human"
            
        drawBoard(mainBoard)
        pygame.display.update()
        FPSCLOCK.tick()
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEBUTTONUP:
                return
        
def enterHumanTile():
    tile=" "
    while not (tile=="x" or tile =="o"):
        print("Do you want to be X or O?")
        tile=input().upper()

        if tile=="x":
            return["x","o"]
        else:
            return["o","x"]

def getHumanMove(board, tile):
    print("human move")
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEBUTTONDOWN:
                clickBoard(board,tile)
                drawBoard(board)
                pygame.display.update()
            else:
                drawBoard(board)
                pygame.display.update()
                FPSCLOCK.tick()
            
                      
        
def getComputerMove(board, computerTile):
    potentialMoves=getPotentialMoves(board, computerTile, DIFFICULTY)
    bestMoveScore=-1
    for i in potentialMoves:
            print(i)
            if potentialMoves[i]>bestMoveScore and isValidMove(board,[i]):
                bestMoveScore=potentialMoves[i]
    bestMoves=[]
    for i in range(len(potentialMoves)):
           if potentialMoves[i]==bestMoveScore and isValidMove(board,[i]):
                bestMoves.append(i)
    return random.choice(bestMoves)
    

def getPotentialMoves(board, computerTile, DIFFICULTY):
    print("board pot move")
    if DIFFICULTY==0 or isBoardFull(board):
        return [0]*(BOARDHEIGHT*BOARDWIDTH)

    if computerTile=="x":
        humanTile="o"
    else:
        humanTile="x"
    potentialMoves=[]
    potentialMoves=[0]*(BOARDHEIGHT*BOARDWIDTH)
    for playerrow in range(BOARDWIDTH):
        for playercolumn in range(BOARDHEIGHT):
            playerMove=(playerrow,playercolumn)
            print(playerMove)
            dupeBoard=copy.deepcopy(board)
            if not isValidMove(dupeBoard, playerrow,playercolumn):
                continue
            drawMove(dupeBoard, computerTile, playerrow,playercolumn)
            if isWinner(dupeBoard, computerTile):
                potentialMoves[playerMove]=1
                print(potentialMoves[playerMove])
                break
            else:
                if isBoardFull(dupeBoard):
                    potentialMoves[playerMove]=0
                else:
                    for enemyrow in range(BOARDWIDTH):
                        for enemycolumn in range(BOARDHEIGHT):
                            enemyMove=(enemyrow,enemycolumn)
                            dupeBoard2=copy.deepcopy(dupeBoard)
                            if not isValidMove(dupeBoard2, enemyrow,enemycolumn):
                               continue
                            drawMove(dupeBoard2, humanTile, enemyrow,enemycolumn)
                            if isWinner(dupeBoard2, humanTile):
                                potentialMoves[playerMove]=-1
                                break
                            else:
                                print(potentialMoves[playerMove])
                                results=getPotentialMoves(dupeBoard2, computerTile, DIFFICULTY-1)
                                potentialMoves[playerMove]+=(sum(results)/BOARDWIDTH)/BOARDHEIGHT
                                print(potentialMoves[playerMove])
    return potentialMoves
                        
            
    
def firstMove():
    if random.randint(0,1)==0:
        return "computer"
    else:
        return "human"
    
def boardPos(mouseX, mouseY):
    row=mouseY//(SPACESIZE+YMARGIN)
    col=mouseX//(SPACESIZE+XMARGIN)
    #if (mouseY < 100):
        #row=0
    #elif (mouseY > 100):
        #row=mouseY/10
        #row=row//1
        #row=row-1

    #if (mouseX < 100):
        #col=0
    #elif (mouseX > 100):
       #col=mouseX/10
        #col=col//1
        #col=col-1

    print(row,col)
    return (row, col)

def drawMove (board, tile, row, col):
    #row,col=move
    centerX=((col)*100)+50
    centerY=((row)*100)+50

    if (tile=="o"):
        pygame.draw.circle(DISPLAYSURF, (0,0,0), (centerX, centerY), 44, 2)
    else:
        pygame.draw.line(DISPLAYSURF, (0,0,0), (centerX-22, centerY-22),(centerX+22, centerY+22),2)
        pygame.draw.line(DISPLAYSURF, (0,0,0), (centerX+22, centerY-22),(centerX-22, centerY+22),2)

    if isValidMove(board,row,col):    
        board[row][col]=tile
        print(isValidMove(board,row,col))
    print(tile)
    
def getNewBoard():
    board=[]
    for x in range(BOARDWIDTH):
        board.append([" "]*BOARDHEIGHT)
    return board

def drawBoard(board):
    spaceRect=pygame.Rect(0,0, SPACESIZE, SPACESIZE)
    DISPLAYSURF.fill(BGCOL)
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            spaceRect.topleft=(XMARGIN+(x*SPACESIZE), YMARGIN+(y*SPACESIZE))
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            spaceRect.topleft=(XMARGIN+(x*SPACESIZE), YMARGIN+(y*SPACESIZE))
            #DISPLAYSURF.blit(boardimg, spaceRect)
            color=(255,255,255)
            pygame.draw.rect(DISPLAYSURF, color, spaceRect)
            #DISPLAYSURF.blit(DISPLAYSURF,spaceRect)
            #DISPLAYSURF.fill(color)
    #background=pygame.Surface(DISPLAYSURF.get_size())
    #background=background.convert()
    #return background

def isValidMove(board, row, col):
    if row < BOARDWIDTH or col >= BOARDWIDTH and row <BOARDHEIGHT or col >=BOARDHEIGHT:
        return False

    if row or col!= ' ':
        return False

    return True

def clickBoard(board,tile):
    (mouseX, mouseY)=pygame.mouse.get_pos()
    print("should click here")
    (row,col)=boardPos(mouseX, mouseY)
    (row,col)=(int(row),int(col))
    print(row,col)
    if tile in board[row][col]:
       return
    drawMove(board, tile, row, col)

def isBoardFull(board):
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if board[x][y]==" ":
                return False
    return True
    

def isWinner(board, tile):
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT - 3):
            if board[x][y]==tile and board[x][y+1]==tile and board[x][y+2] and board[x][y+3]==tile:
                return True
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT - 3):
            if board[x][y]==tile and board[x+1][y]==tile and board[x+2][y] and board[x+3][y]==tile:
                return True
    for x in range(BOARDWIDTH-3):
        for y in range(BOARDHEIGHT - 3):
            if board[x][y]==tile and board[x+1][y+1]==tile and board[x+2][y+2] and board[x+3][y+3]==tile:
                return True
    for x in range(BOARDWIDTH):
        for y in range(3, BOARDHEIGHT):
            if board[x][y]==tile and board[x+1][y-1]==tile and board[x+2][y-2] and board[x+3][y-3]==tile:
                return True
    return False
        

main()


    



    
