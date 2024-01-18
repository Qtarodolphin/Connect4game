import random, copy, sys

BOARDWIDTH=8
BOARDHEIGHT=7

def main():
    """
    b=getBoard()
    b[6][5]="X"
    b[5][4]="X"
    b[4][3]="X"
    b[3][2]="X"
    drawBoard(b)
    print(winnder(b, "X")

    sys.exit()
    """

    print("Four-In-A-Row")
    print()

    while True:
        humanTile, computerTile = enterHumanTile()
        turn = whoGoesFirst()
        print('The %s player will go first.' % (turn))
        mainBoard = getNewBoard()

        while True:
            if turn == 'human':
                drawBoard(mainBoard)
                move = getHumanMove(mainBoard)
                makeMove(mainBoard, humanTile, move)
                if isWinner(mainBoard, humanTile):
                    winner = 'human'
                    break
                turn = 'computer'
            else:
                drawBoard(mainBoard)
                print('The computer is thinking...')
                move = getComputerMove(mainBoard, computerTile)
                makeMove(mainBoard, computerTile, move)
                if isWinner(mainBoard, computerTile):
                    winner = 'computer'
                    break
                turn = 'human'

            if isBoardFull(mainBoard):
                winner = 'tie'
                break

        drawBoard(mainBoard)
        print('Winner is: %s' % winner)
        if not playAgain():
            break


def getBoard():
    board=[]
    for x in range(BOARDWIDTH):
        board.append([" "]*BOARDHEIGHT)
    return board

def drawBoard(board):
    print()
    print(" ", end=" ")
    for x in range(1, BOARDWIDTH+1):
        print(" %s " %x, end=" ")
    print()

    print("+---+" + ("---+" * (BOARDWIDTH-1)))

    for y in range (BOARDHEIGHT):
        print("| |"+(" |"*(BOARDWIDTH-1)))

        print("|", end=" ")
        for x in range(BOARDWIDTH):
            print(" %s |" % board[x][y], end=" ")
        print()

        print("| |"+(" |" * (BOARDWIDTH-1)))
        print("+---+"+("---+"*(BOARDWIDTH-1)))
        
                    
