import random
from ChessMain import *

pieceScore = { 'K': 1000, 'Q': 10, 'R': 5, 'B': 3, 'N': 3, 'P': 11}

def findRandomMove(validMoves):
    return validMoves[random.randint(0, len(validMoves)-1)]

'''
можно использовать фикстуру gs
'''
def findBestMove(gs, validMoves):
    turn = 1 if gs.whiteToMove else -1
    maxScore = -1000
    bestMove = None
    bestMoveArr = []
    for playerMove in validMoves:
        gs.makeMove(playerMove)
        score = turn * scoreMaterial(gs.board)
        if (score > maxScore):
            scoreArr = []
            maxScore = score
            bestMove = playerMove
            bestMoveArr.append(bestMove)
        #elif score == maxScore:
        #    maxScore = score
        #    bestMove = playerMove
        #    bestMoveArr.append(bestMove)
        gs.undoMove()
    #return bestMoveArr[random.randint(0, len(bestMoveArr)-1)]
    return bestMove


'''
оценка доски?
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


