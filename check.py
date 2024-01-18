print("Fuck you")
while True:
    mainBoard=getNewBoard()
    resetBoard(mainBoard)
    if whoGoesFirst()=="player":
        turn="X"
    else:
        turn="O"
    print("The "+turn", murderer of all we hold dear, will cede his turn first.")
    while True:
        drawBoard(mainBoard)
        scores=getScoreOfBoard(mainBoard)
    print
    
