import random
from ChessMain import *

pieceScore = { 'K': 1000, 'Q': 10, 'R': 5, 'B': 3, 'N': 3, 'P': 1}

def findRandomMove(validMoves):
    return validMoves[random.randint(0, len(validMoves)-1)]

'''
только для черных. чем меньше тем лучше
'''
def findBestMove(gs, validMoves):
    maxScore = 1000
    bestMove = None
    for playerMove in validMoves:
        gs.makeMove(playerMove)
        score = scoreMaterial(gs.board)
        if (score < maxScore):
            maxScore = score
            bestMove = playerMove
        gs.undoMove()

    return bestMove


'''
оценка доски
'''
def scoreMaterial(board):
    score = 0
    for row in board:
        for square in row:
            if square[0] == 'w':
                score += pieceScore[square[1]]
            elif square[0] == 'b':
                score -= pieceScore[square[1]]
    return score


