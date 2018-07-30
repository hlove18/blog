#Added:
    #five-piece tetrominoes instead of four-piece
    #a mirrorPiece function, using "m"-key
    #a drawHighScore function that resets when the program quits
    #dual rotation:  "a" for counter clockwise, "s" for clockwise
    #a pause feature
    #a hard drop:  spacebar
    #piece preview
    #an instructions screen before the start of first game

from Tkinter import *
import random

def drawGame(canvas):
    drawBoard(canvas)
    if (canvas.data["isGameOver"] == False):
        drawFallingPiece(canvas)

def drawBoard(canvas):
    for row in xrange(canvas.data["rows"]):
        for col in xrange(canvas.data["cols"]):
            drawCell(canvas, row, col, canvas.data["board"][row][col])

def drawCell(canvas, row, col, color):
    topLeftX = 30 + col * 20
    topLeftY = 30 + row * 20
    bottomRightX = topLeftX + 20
    bottomRightY = topLeftY + 20
    canvas.create_rectangle((topLeftX, topLeftY), (bottomRightX,
                                                   bottomRightY),
                            fill = "white")
    colorTopX = topLeftX + 2
    colorTopY = topLeftY + 2
    colorBottomX = bottomRightX - 2
    colorBottomY = bottomRightY - 2
    canvas.create_rectangle((colorTopX, colorTopY), (colorBottomX,
                                                     colorBottomY),
                            fill = color)
        
def timerFired(canvas):
    canvas.data["firstGame"] = False
    if canvas.data["isGameOver"]:
        gameOverScreen(canvas)
        canvas.after(1000, timerFired, canvas)
    elif canvas.data["paused"]:
        pauseScreen(canvas)
        canvas.after(1000, timerFired, canvas)
    elif moveFallingPiece(canvas, 1, 0):
        delay = 1000
        canvas.after(delay, timerFired, canvas)
        redrawAll(canvas)
    else:
        placeFallingPiece(canvas)
        removeFullRows(canvas)
        canvas.data["fallingPiece"] = canvas.data["nextFallingPiece"]
        canvas.data["fallingPieceColor"] = canvas.data["nextFallingPieceColor"]
        newFallingPiece(canvas)
        if (moveFallingPiece(canvas, 0, 0) == False):
            canvas.data["isGameOver"] = True
            timerFired(canvas)
        else:
            redrawAll(canvas)
            canvas.after(1000, timerFired, canvas)

def gameOverScreen(canvas):
    canvas.data["isGameOver"] = True
    textX = canvas.data["canvasWidth"]/2
    textY = canvas.data["canvasHeight"]/6
    canvas.create_text((textX, textY), text = "Game Over!", font =
                       ("Arial", 28, "bold"), fill = "white")
    canvas.create_text((textX, textY + 30),
                       text = "Press 'r' to restart", font =
                       ("Arial", 18, "bold"), fill = "white")

def drawHighScores(canvas):
    textX = canvas.data["canvasWidth"]/2
    textY = canvas.data["canvasHeight"]/2.5 - 25
    highScores = canvas.data["highScores"]
    currentScore = canvas.data["score"]
    if (canvas.data["highScoresPrinted"] == False):
        if (currentScore > highScores[-1]):
            highScores[-1] = currentScore
            for x in xrange(1, 5):
                if (highScores[-x] > highScores[-(x + 1)]):
                    swapIndices(highScores, -x, -(x + 1))
    canvas.create_text((textX, textY), text = "High Scores:", font =
                       ("Arial", 34, "bold"), fill = "white")
    for x in xrange(5):
        score = highScores[x]
        canvas.create_text((textX, textY + 50 + 40 * x), text = score,
                           font = ("Arial", 34, "bold"), fill = "white")
    canvas.data["highScoresPrinted"] = True

def swapIndices(highScores, index1, index2):
    holdValue = highScores[index1]
    highScores[index1] = highScores[index2]
    highScores[index2] = holdValue

def placeFallingPiece(canvas):
    fallingPieceRow = canvas.data["fallingPieceRow"]
    fallingPieceCol = canvas.data["fallingPieceCol"]
    piece = canvas.data["fallingPiece"]
    color = canvas.data["fallingPieceColor"]
    board = canvas.data["board"]
    for y in xrange(len(piece)):
        for x in xrange(len(piece[0])):
            if piece[y][x]:
                board[y + fallingPieceRow][x + fallingPieceCol] = color
    canvas.after(1000, redrawAll, canvas)

def newFallingPiece(canvas):
    fallingPiece = canvas.data["nextFallingPiece"]
    fallingPieceColor = canvas.data["nextFallingPieceColor"]
    newNextFallingPiece(canvas)
    canvas.data["fallingPiece"] = fallingPiece
    canvas.data["fallingPieceColor"] = fallingPieceColor
    fallingPieceRow = 0
    fallingPieceCol = canvas.data["cols"]/2 - len(fallingPiece[0])/2
    canvas.data["fallingPieceRow"] = fallingPieceRow
    canvas.data["fallingPieceCol"] = fallingPieceCol
    if (moveFallingPiece(canvas, 0, 0)):
        redrawAll(canvas)
    else:
        canvas.data["isGameOver"] = True
        gameOverScreen(canvas)

def drawFallingPiece(canvas):
    drawNextFallingPiece(canvas)
    piece = canvas.data["fallingPiece"]
    color = canvas.data["fallingPieceColor"]
    TLrow = canvas.data["fallingPieceRow"]
    TLcol = canvas.data["fallingPieceCol"]
    for y in xrange(len(piece)):
        for x in xrange(len(piece[y])):
            if piece[y][x]:
                TLX = 30 + (TLcol + x) * 20
                TLY = 30 + (TLrow + y) * 20
                BRX = TLX + 20
                BRY = TLY + 20
                canvas.create_rectangle((TLX, TLY), (BRX, BRY), fill =
                                        "white")
                TLXColor = TLX + 2
                TLYColor = TLY + 2
                BRXColor = BRX - 2
                BRYColor = BRY - 2
                canvas.create_rectangle((TLXColor, TLYColor),
                                        (BRXColor,BRYColor), fill =
                                        color)

def newNextFallingPiece(canvas):
    x = random.randint(0, 11)
    nextFallingPiece = canvas.data["tetrisPieces"][x]
    nextFallingPieceColor = canvas.data["tetrisPieceColors"][x]
    canvas.data["nextFallingPiece"] = nextFallingPiece
    canvas.data["nextFallingPieceColor"] = nextFallingPieceColor

def drawNextFallingPiece(canvas):
    piece = canvas.data["nextFallingPiece"]
    color = canvas.data["nextFallingPieceColor"]
    TLPointX = 10
    TLPointY = 10
    for y in xrange(len(piece)):
        for x in xrange(len(piece[y])):
            if piece[y][x]:
                TLX = 10 + x * 5
                TLY = 10 + y * 5
                BRX = TLX + 5
                BRY = TLY + 5
                canvas.create_rectangle((TLX, TLY), (BRX, BRY), fill = color)

def dropFallingPiece(canvas):
    while fallingPieceIsLegal(canvas):
        canvas.data["fallingPieceRow"] += 1
    canvas.data["fallingPieceRow"] -= 1
    redrawAll(canvas)

def moveFallingPiece(canvas, drow, dcol):
    canvas.data["fallingPieceRow"] += drow
    canvas.data["fallingPieceCol"] += dcol
    if fallingPieceIsLegal(canvas):
        piece = canvas.data["fallingPiece"]
        color = canvas.data["fallingPieceColor"]
        for y in xrange(len(piece)):
            for x in xrange(len(piece[y])):
                if piece[y][x]:
                    tlx = canvas.data["fallingPieceRow"]
                    tly = canvas.data["fallingPieceCol"]
                    brx = canvas.data["fallingPieceRow"] + 20
                    bry = canvas.data["fallingPieceCol"] + 20
                    canvas.create_rectangle((tlx, tly), (brx, bry),
                                            fill = "white")
                    canvas.create_rectangle((tlx + 2, tly + 2),
                                            (brx - 2, bry - 2), fill =
                                            color)
        return True
    else:
        canvas.data["fallingPieceRow"] -= drow
        canvas.data["fallingPieceCol"] -= dcol
        redrawAll(canvas)
        return False

def fallingPieceIsLegal(canvas):
    board = canvas.data["board"]
    piece = canvas.data["fallingPiece"]
    row = canvas.data["fallingPieceRow"]
    col = canvas.data["fallingPieceCol"]
    emptyColor = canvas.data["emptyColor"]
    for y in xrange(len(piece)):
        for x in xrange(len(piece[y])):
            if piece[y][x]:
                if ((row + y) >= canvas.data["rows"]):
                    return False
                elif ((col + x) >= canvas.data["cols"]):  return False
                elif ((row + y) < 0):
                    return False
                if ((col + x) < 0):  return False
                elif (board[row + y][col + x] != emptyColor):
                    return False
    return True

def mirrorFallingPiece(canvas):
    oldPiece = canvas.data["fallingPiece"]
    rows = len(oldPiece)
    cols = len(oldPiece[0])
    newPiece = []
    for x in xrange(rows):
        newPiece.append([False] * cols)
    for y in xrange(len(oldPiece)):
        for x in xrange(len(oldPiece[y])):
            if (oldPiece[y][x]):
                newPiece[y][-(x + 1)] = True
    canvas.data["fallingPiece"] = newPiece
    if fallingPieceIsLegal(canvas):
        redrawAll(canvas)
    else:
        canvas.data["fallingPiece"] = oldPiece

def rotateFallingPieceCC(canvas):
    oldPiece = canvas.data["fallingPiece"]
    oldRows = len(oldPiece)
    oldCols = len(oldPiece[0])
    oldCenterRow = fallingPieceCenter(canvas)[0]
    oldCenterCol = fallingPieceCenter(canvas)[1]
    newRows = oldCols
    newCols = oldRows
    newPiece = []
    for x in xrange(newRows):
        newPiece.append([False] * newCols)
    for y in xrange(len(oldPiece)):
        for x in xrange(len(oldPiece[y])):
            if (oldPiece[y][x]):
                newPiece[-(x + 1)][y] = True
    canvas.data["fallingPiece"] = newPiece
    newCenterRow = fallingPieceCenter(canvas)[0]
    newCenterCol = fallingPieceCenter(canvas)[1]
    canvas.data["fallingPieceRow"] += (oldCenterRow - newCenterRow)
    canvas.data["fallingPieceCol"] += (oldCenterCol - newCenterCol)
    if fallingPieceIsLegal(canvas):
        redrawAll(canvas)
    else:
        canvas.data["fallingPiece"] = oldPiece
        canvas.data["fallingPieceRow"] -= (oldCenterRow - newCenterRow)
        canvas.data["fallingPieceCol"] -= (oldCenterCol - newCenterCol)

def rotateFallingPieceC(canvas):
    oldPiece = canvas.data["fallingPiece"]
    oldRows = len(oldPiece)
    oldCols = len(oldPiece[0])
    oldCenterRow = fallingPieceCenter(canvas)[0]
    oldCenterCol = fallingPieceCenter(canvas)[1]
    newRows = oldCols
    newCols = oldRows
    newPiece = []
    for x in xrange(newRows):
        newPiece.append([False] * newCols)
    for y in xrange(len(oldPiece)):
        for x in xrange(len(oldPiece[y])):
            if (oldPiece[y][x]):
                newPiece[x][-(y + 1)] = True
    canvas.data["fallingPiece"] = newPiece
    newCenterRow = fallingPieceCenter(canvas)[0]
    newCenterCol = fallingPieceCenter(canvas)[1]
    canvas.data["fallingPieceRow"] += (oldCenterRow - newCenterRow)
    canvas.data["fallingPieceCol"] += (oldCenterCol - newCenterCol)
    if fallingPieceIsLegal(canvas):
        redrawAll(canvas)
    else:
        canvas.data["fallingPiece"] = oldPiece
        canvas.data["fallingPieceRow"] -= (oldCenterRow - newCenterRow)
        canvas.data["fallingPieceCol"] -= (oldCenterCol - newCenterCol)

def fallingPieceCenter(canvas):
    piece = canvas.data["fallingPiece"]
    TLRow = canvas.data["fallingPieceRow"]
    TLCol = canvas.data["fallingPieceCol"]
    centerRow = TLRow + len(piece)/2
    centerCol = TLCol + len(piece[0])/2
    return (centerRow, centerCol)

def drawScore(canvas):
    score = canvas.data["score"]
    textX = canvas.data["canvasWidth"]/2
    textY = 30/2
    canvas.create_rectangle((textX - 30 * 2, textY - 15), (textX + 30 *
                                                           2, textY + 15),
                            fill = "white")
    canvas.create_text((textX, textY), text = ("Score:", score), font =
                       ("Arial", 16, "bold"))

def removeFullRows(canvas):
    emptyColor = canvas.data["emptyColor"]
    boardRows = canvas.data["rows"]
    boardCols = canvas.data["cols"]
    board = canvas.data["board"]
    oldRow = boardRows - 1
    newRow = boardRows - 1
    while (oldRow > -1):
        for x in xrange(boardCols):
            board[newRow][x] = board[oldRow][x]
        if (emptyColor in board[oldRow]):
            newRow -= 1
        oldRow -= 1
    canvas.data["score"] += (oldRow - newRow)**2
    for x in xrange(newRow - oldRow):
        for y in xrange(boardCols):
            board[x][y] = "black"

def instructions(canvas):
    width = canvas.data["canvasWidth"]
    height = canvas.data["canvasHeight"]
    textX = width/2
    textY = height/6
    canvas.create_text((textX, textY), text = "Pentris Instructions:",
                       font = ("Arial", 24, "bold"), fill = "white")
    canvas.create_text((textX, textY + 35), text =
                       "Use arrow keys to move right, left, and down",
                       font = ("Arial", 12, "bold"), fill = "white")
    canvas.create_text((textX, textY + 65), text =
                       "'a' key rotates the falling piece counter clockwise",
                       font = ("Arial", 12, "bold"), fill = "white")
    canvas.create_text((textX, textY + 95), text =
                       "'s' key rotates the falling piece clockwise",
                       font = ("Arial", 12, "bold"), fill = "white")
    canvas.create_text((textX, textY + 125), text =
                       "'m' key makes a mirror of the falling piece",
                       font = ("Arial", 12, "bold"), fill = "white")
    canvas.create_text((textX, textY + 155), text =
                       "The spacebar hard drops the falling piece",
                       font = ("Arial", 12, "bold"), fill = "white")
    canvas.create_text((textX, textY + 185), text =
                       "Look in upper left corner for next piece",
                       font = ("Arial", 12, "bold"), fill = "white")
    canvas.create_text((textX, textY + 215), text =
                       "'p' key pauses the current game", font =
                       ("Arial", 12, "bold"), fill = "white")
    canvas.create_text((textX, textY + 245), text =
                       "'r' key starts a new game", font =
                       ("Arial", 12, "bold"), fill = "white")
    canvas.create_text((textX, height * 5/6), text =
                       "Push 'r' for New Game!", font =
                       ("Arial", 18, "bold"), fill = "white")

def pauseScreen(canvas):
    textX = canvas.data["canvasWidth"]/2
    textY = canvas.data["canvasHeight"]/2
    canvas.create_text((textX, textY), text = "Paused", font =
                       ("Arial", 32, "bold"), fill = "white")
    canvas.create_text((textX, textY + 50), text =
                       "Press 'p' to resume", font =
                       ("Arial", 16, "bold"), fill = "white")
    canvas.create_text((textX, textY + 70), text =
                       "or press 'r' to restart", font =
                       ("Arial", 16, "bold"), fill = "white")

def keyPressed(event):
    canvas = event.widget.canvas
    if canvas.data["isGameOver"]:
        if (event.keysym == "r"):
            init(canvas)
    elif canvas.data["paused"]:
        if (event.keysym == "p"):
            canvas.data["paused"] = False
        elif (event.keysym == "r"):
            canvas.data["paused"] = False
            init(canvas)
    else:
        if (event.keysym == 'Down'):
            moveFallingPiece(canvas, 1, 0)
            redrawAll(canvas)
        elif (event.keysym == "Left"):
            moveFallingPiece(canvas, 0, -1)
            redrawAll(canvas)
        elif (event.keysym == "Right"):
            moveFallingPiece(canvas, 0, 1)
            redrawAll(canvas)
        elif (event.keysym == "a"):
            rotateFallingPieceCC(canvas)
        elif (event.keysym == "s"):
            rotateFallingPieceC(canvas)
        elif (event.keysym == "m"):
            mirrorFallingPiece(canvas)
        elif (event.keysym == "space"):
            dropFallingPiece(canvas)
        elif (event.keysym == "r"):
            init(canvas)
        elif (event.keysym == "p"):
            if canvas.data["paused"]:
                canvas.data["paused"] = False
            else:
                canvas.data["paused"] = True

def redrawAll(canvas):
    canvas.delete(ALL)
    drawGame(canvas)
    drawScore(canvas)
    if canvas.data["isGameOver"]:
        gameOverScreen(canvas)
        drawHighScores(canvas)

def init(canvas):
    canvas.data["highScoresPrinted"] = False
    canvas.data["isGameOver"] = False
    emptyColor = ("black")
    board = []
    rows = canvas.data["rows"]
    cols = canvas.data["cols"]
    canvas.data["score"] = 0
    for x in xrange(rows):
        board.append([emptyColor] * cols)
    canvas.data["board"] = board
    canvas.data["emptyColor"] = emptyColor
    pieceA = [[True, True, True, True, True]]
    pieceB = [[True, False, False, False],
              [True, True, True, True]]
    pieceC = [[True, True, False, False],
              [False, True, True, True]]
    pieceD = [[True, True, False],
              [True, True, True]]
    pieceE = [[True, False, True],
              [True, True, True]]
    pieceF = [[True, True, True, True],
              [False, False, True, False]]
    pieceG = [[False, True, False],
              [False, True, False],
              [True, True, True]]
    pieceH = [[True, False, False],
              [True, False, False],
              [True, True, True]]
    pieceI = [[True, True, False],
              [False, True, True],
              [False, False, True]]
    pieceJ = [[True, False, False],
               [True, True, True],
               [False, False, True]]
    pieceK = [[True, False, False],
               [True, True, True],
               [False, True, False]]
    pieceL = [[False, True, False],
               [True, True, True],
               [False, True, False]]
    tetrisPieces = [pieceA, pieceB, pieceC, pieceD, pieceE, pieceF,
                    pieceG, pieceH, pieceI, pieceJ, pieceK, pieceL]
    tetrisPieceColors = ["YellowGreen", "red", "yellow", "magenta",
                         "pink", "cyan", "green", "orange",
                         "VioletRed", "SeaGreen", "PowderBlue",
                         "PeachPuff"]
    canvas.data["tetrisPieces"] = tetrisPieces
    canvas.data["tetrisPieceColors"] = tetrisPieceColors
    newNextFallingPiece(canvas)
    newFallingPiece(canvas)
    redrawAll(canvas)
    if canvas.data["firstGame"]:
        canvas.after(1000, timerFired, canvas)

def run(rows, cols):
    root = Tk()
    canvas = Canvas(root, width = cols * 20 + 2 * 30,
                    height = rows * 20 + 2 * 30, bg = "black")
    canvas.pack()
    root.resizable(width = 0, height = 0)
    root.canvas = canvas.canvas = canvas
    canvas.data = {}
    canvas.data["rows"] = rows
    canvas.data["cols"] = cols
    canvas.data["canvasWidth"] = cols * 20 + 2 * 30
    canvas.data["canvasHeight"] = rows * 20 + 2 * 30
    canvas.data["canvasColor"] = "black"
    highScores = [0, 0, 0, 0, 0]
    canvas.data["highScores"] = highScores
    canvas.data["isGameOver"] = True
    canvas.data["firstGame"] = True
    canvas.data["paused"] = False
    instructions(canvas)
    root.bind_all("<KeyPress>", keyPressed)
    root.mainloop()

run(18, 12)
