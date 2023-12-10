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
    playerTwo = True

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

                        if move in validMoves: # поменять потом. белые могут ходить как им угодно, даже тупо
                            #drawText(screen, 'tesxt')
                            #print('----valid----')
                            #print(move.getChessNotation())
                            gs.makeMove(move)
                            #print(move.getChessNotation())
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
            #s = p.Surface((SQ_SIDE, SQ_SIDE))
            #s.fill(p.Color('red'))

            #print(type(AiMove))
            #screen.blit(s, (c * SQ_SIDE, r * SQ_SIDE))
        # генерируем новые возможные ходы
        # позволяем пк ходить
        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False

        gameOver = gs.GameOver()
        if gameOver:

            if gs.whiteToMove:
                #print('b')
                drawText(screen, 'Черные поставили мат!')
            else:
                #print('w')
                drawText(screen, 'Белые поставили мат!')

        #if gs.chekMate:
        #    gameOver = True
        #    if gs.whiteToMove:
        #        drawText(screen, 'Черные поставили мат!')
        #    else:
        #        drawText(screen, 'Белые поставили мат!')
        #elif gs.staleMate:
        #    gameOver = True
        #    drawText(screen, 'Ничья!')



        drawGameState(screen, gs, validMoves, sqSelected)
        clock.tick(MAS_FPS)
        p.display.flip()

def drawText1(screen, text):
    print('game over1')
    font = p.font.SysFont('Arial', 32, True, False)
    textObject = font.render(text, 0, p.Color('Red'))
    textLocation = p.Rect(0, 0, WIDTH, HEIGHT)
    screen.blit(textObject, textLocation)

def drawText2(screen, text):
    # Create a font file by passing font file
    # and size of the font
    font1 = p.font.SysFont('freesanbold.ttf', 50)
    font2 = p.font.SysFont('chalkduster.ttf', 40)

    # Render the texts that you want to display
    text1 = font1.render('GeeksForGeeks', True, (0, 255, 0))
    text2 = font2.render('GeeksForGeeks', True, (0, 255, 0))



    # create a rectangular object for the
    # text surface object
    textRect1 = text1.get_rect()
    textRect2 = text2.get_rect()

    # setting center for the first text
    textRect1.center = (250, 250)

    # setting center for the second text
    textRect2.center = (250, 300)

    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)

    #messagebox. askquestion('Confirm','Are you sure?')
    #text = 'hello world!'
    # Рендерим
    #a = Font.render(text, 1, (100, 100, 100))
    # Рисуем отрендеренный текст в созданном окне
    #screen.blit(a, (160, 110))


    print('game over')
    font = p.font.SysFont('Times', 32, True, False)
    textObject = font.render('text', 0, p.Color('Gray'))
    #textLocation = p.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH/2 - textObject.get_width()/2, HEIGHT/2 - textObject.get_height()/2)
    textLocation = p.Rect(0, 0, WIDTH, HEIGHT)
    screen.blit(textObject, textLocation)
    #textObject = font.render(text, 0, p.Color('Black'))
    #screen.blit(textObject, textLocation.move(2, 2))


def drawText2(screen, gs ,text):
    pass


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
