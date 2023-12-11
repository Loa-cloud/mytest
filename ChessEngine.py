'''
Текущее состояние шахматной партии
Допустимые ходы в текущем состояниии
Сохранение ходов - то что мне не нужно
https://youtu.be/F-ZPioOvOaM?list=PLBwF487qi8MGU81nDGaeNE1EnNEPYWKY_
'''

import pygame as p
from ChessMain import *
from Ai import *
import sys
from tkinter import *
from tkinter import messagebox


WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIDE = HEIGHT // DIMENSION
MAS_FPS = 15
IMAGES = {}

'''
загрузка изображений 1 раз
- можно сделать юнит тест по поводу загрузки словаря
'''
def loadImages():
    IMAGES['wP'] = p.transform.scale(p.image.load('images/wp.png'), (SQ_SIDE, SQ_SIDE))
    IMAGES['bP'] = p.transform.scale(p.image.load('images/bp.png'), (SQ_SIDE, SQ_SIDE))
    IMAGES['wR'] = p.transform.scale(p.image.load('images/wR.png'), (SQ_SIDE, SQ_SIDE))
    IMAGES['bR'] = p.transform.scale(p.image.load('images/bR.png'), (SQ_SIDE, SQ_SIDE))
    IMAGES['wN'] = p.transform.scale(p.image.load('images/wN.png'), (SQ_SIDE, SQ_SIDE))
    IMAGES['bN'] = p.transform.scale(p.image.load('images/bN.png'), (SQ_SIDE, SQ_SIDE))
    IMAGES['wB'] = p.transform.scale(p.image.load('images/wB.png'), (SQ_SIDE, SQ_SIDE))
    IMAGES['bB'] = p.transform.scale(p.image.load('images/bB.png'), (SQ_SIDE, SQ_SIDE))
    IMAGES['wQ'] = p.transform.scale(p.image.load('images/wQ.png'), (SQ_SIDE, SQ_SIDE))
    IMAGES['bQ'] = p.transform.scale(p.image.load('images/bQ.png'), (SQ_SIDE, SQ_SIDE))
    IMAGES['wK'] = p.transform.scale(p.image.load('images/wK.png'), (SQ_SIDE, SQ_SIDE))
    IMAGES['bK'] = p.transform.scale(p.image.load('images/bK.png'), (SQ_SIDE, SQ_SIDE))


'''
основаня функция
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill((p.Color('white')))
    gs = GameState()
    validMoves = gs.getValidMoves() #чтобы пользователь мог делать только проверенные ходы
    moveMade = False #флаг для того сделан ход или нет, чтобы можно было сгенерировать новый validMoves

    loadImages()
    running = True
    sqSelected = ()
    playerClicks = []
    gameOver = False

    playerOne = True
    playerTwo = False

    while running:
        humanTurn = (gs.whiteToMove and playerOne) or (not gs.whiteToMove and playerTwo)
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:

                if not gameOver and humanTurn:
                    location = p.mouse.get_pos() #(x,y) координаты мыши
                    col = location[0]//SQ_SIDE
                    row = location[1]//SQ_SIDE
                    if sqSelected == (row, col): # сброс выбора
                        sqSelected = ()
                        playerClicks = []
                    else:
                        sqSelected = (row, col)
                        playerClicks.append(sqSelected)
                    if len(playerClicks) == 2:
                        move = Move(playerClicks[0], playerClicks[1], gs.board)

                        if move in validMoves:
                            gs.makeMove(move)
                            moveMade = True
                            sqSelected = ()
                            playerClicks = []
                        if not moveMade:
                            playerClicks = [sqSelected]


        if not gameOver and not humanTurn:
            aiMove = findBestMove(gs, validMoves)
            if aiMove == None:
                aiMove = findRandomMove(validMoves)
            gs.makeMove(aiMove)
            moveMade = True
            sqSelected = ()
            playerClicks = []

        # генерируем новые возможные ходы
        # позволяем пк ходить
        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False

        drawGameState(screen, gs, validMoves, sqSelected)
        clock.tick(MAS_FPS)
        p.display.flip()



'''
подсветка
'''
def highlightSquares(screen,gs,validMoves,sqSelected):
    if sqSelected != ():
        r, c = sqSelected
        if gs.board[r][c][0] == ('w' if gs.whiteToMove else 'b') :
            s = p.Surface((SQ_SIDE,SQ_SIDE))
            s.set_alpha(100) # показатель прозрачности; 255 - не прозрачный
            s.fill(p.Color('red'))
            screen.blit(s, (c*SQ_SIDE, r*SQ_SIDE))

            s.fill(p.Color('yellow'))
            for move in validMoves:
                if move.startRow == r and move.startCol == c:
                    screen.blit(s, (move.endCol * SQ_SIDE, move.endRow * SQ_SIDE))


'''
вся графика в игре
'''
def drawGameState(screen,gs, validMoves, sqSelected):
    drawBoard(screen) # квадратики
    highlightSquares(screen, gs, validMoves, sqSelected)
    drawPieces(screen, gs.board) # фигуры

'''
квадратики
'''
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            color = colors[((i+j) % 2)]
            p.draw.rect(screen, color, p.Rect(j*SQ_SIDE, i*SQ_SIDE, SQ_SIDE, SQ_SIDE))

'''
фигуры на доске
'''
def drawPieces(screen, board):
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            piece = board[i][j]
            if (piece != '--'):
                screen.blit(IMAGES[piece], p.Rect(j*SQ_SIDE, i*SQ_SIDE, SQ_SIDE, SQ_SIDE))



main()
