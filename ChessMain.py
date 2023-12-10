'''
Класс текущего состояния игры
'''

'''
makeMove зависит от другого класса
лучшее место для создания фикстуры
'''
class GameState():
    def __init__(self):

        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
        self.whiteToMove = True
        self.movelog = []
        self.whiteKingLocation = (7, 4)
        self.blackKingLocation = (0, 4)
        self.chekMate = False
        self.staleMate = False





    def makeMove(self, move):
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.board[move.startRow][move.startCol] = '--'
        self.movelog.append(move)
        self.whiteToMove = not self.whiteToMove

        # обновление позиции короля
        if move.pieceMoved == 'wK':
            self.whiteKingLocation = (move.endRow, move.endCol)
        if move.pieceMoved == 'bK':
            self.blackKingLocation = (move.endRow, move.endCol)


    def undoMove(self):
        if len(self.movelog) != 0:
            move = self.movelog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove

            # обновление позиции короля
            if move.pieceMoved == 'wK':
                self.whiteKingLocation = (move.startRow, move.startCol)
            if move.pieceMoved == 'bK':
                self.blackKingLocation = (move.startRow, move.startCol)




    '''
    находится ли игрок под шахом?
    '''
    def inCheck(self):
        if self.whiteToMove:
            return self.suareUnderAttack(self.whiteKingLocation[0], self.whiteKingLocation[1])
        else:
            return self.suareUnderAttack(self.blackKingLocation[0], self.blackKingLocation[1])



    def GameOver(self):
        count = 0
        for c in range(8):
            for r in range(8):
                if self.board[c][r][1] == 'K':
                    count += 1
        if count == 2:
            return False
        return True

    '''
    нерабочая фигня
    '''
    def getSmartMoves(self):
        #1) сгенерировать все свои ходы
        moves = self.getAllPossibleMoves()
        #2) пойти по списку и походить
        for i in range(len(moves)-1, -1, -1):
            self.makeMove(moves[i])
            #3) сгенерировать все ходы врага
            #4) посмотреть не находится ли король под атакой
            self.whiteToMove = not self.whiteToMove
            if self.inCheck():
                moves.remove(moves[i]) #5) если король под атакой, то этот ход делать нельзя
            self.whiteToMove = not self.whiteToMove
            self.undoMove()
        return moves



    '''
    атакует ли враг текущую клетку?
    '''
    def suareUnderAttack(self, r, c):
        self.whiteToMove = not self.whiteToMove # становимся аппонентом
        oppMoves = self.getAllPossibleMoves()
        for move in oppMoves:
            if move.endRow == r and move.endCol == c:
                self.whiteToMove = not self.whiteToMove
                return True
        return False


    '''
    Все ходы с проверкой шаха, чтобы не подставлять короля
    останется дли ии черных
    '''
    def getValidMoves(self):
        return self.getAllPossibleMoves()
        #return self.getSmartMoves()

    '''
    Все ходы без проверки шаха?
    для игрока
    '''
    def getAllPossibleMoves(self):
        #moves = [Move((6,4), (4,4), self.board), Move((6,4), (0,0), self.board)]
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0] # белые или черные
                if (turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1] # тип фигуры
                    if piece == 'P':
                        self.getPawnMoves(r, c, moves)
                    if piece == 'R':
                        self.getRockMoves(r, c, moves)
                    if piece == 'N':
                        self.getKnightMoves(r, c, moves)
                    if piece == 'B':
                        self.getBishopMoves(r, c, moves)
                    if piece == 'Q':
                        self.getQueenMoves(r, c, moves)
                    if piece == 'K':
                        self.getKingMoves(r, c, moves)
        return moves

    def insideBoard(self, c, r):
        if (c >= 0) and (c <= 7) and (r >= 0) and (r <= 7):
            return True
        return False

    def isEnemy(self, r, c):
        if ((self.board[r][c][0] == 'b' and self.whiteToMove) or
            (self.board[r][c][0] == 'w' and not self.whiteToMove)):
            return True
        return False

    def isАlly(self, r, c):
        if ((self.board[r][c][0] == 'b' and not self.whiteToMove) or
            (self.board[r][c][0] == 'w' and self.whiteToMove)):
            return True
        return False

    def isNull(self, r, c):
        if self.board[r][c] == '--':
            return True
        return False


    def getPawnMoves(self, row, col, moves):
        turn = 1
        if self.whiteToMove:
            turn = -1
        # одиночный и двойной ход
        if  self.insideBoard(row + turn, col) and (self.board[row + turn][col] == '--'):
            moves.append(Move((row, col), (row + turn, col), self.board))
            if (self.insideBoard(row + turn * 2, col) and
                (self.board[row + turn * 2][col] == '--') and
                ((turn == -1 and row == 6) or (turn == 1 and row == 1))):
                moves.append(Move((row, col), (row + turn * 2, col), self.board))

        # поедание
        if (self.insideBoard(row + turn, col - 1) and
            self.isEnemy(row + turn, col - 1)):
            moves.append(Move((row, col), (row + turn, col - 1), self.board))

        if (self.insideBoard(row + turn, col + 1) and
            self.isEnemy(row + turn, col + 1)):
            moves.append(Move((row, col), (row + turn, col + 1), self.board))


    def getKnightMoves(self, row, col, moves):
        knightMoves = [
                        (-2, -1), (-2, +1), (+2, -1), (+2, +1),
                        (-1, -2), (-1, +2), (+1, -2), (+1, +2),
                       ]

        for m in knightMoves:
            r = m[0] + row
            c = m[1] + col
            if (self.insideBoard(r, c) and (self.isNull(r, c) or self.isEnemy(r, c))):
                moves.append(Move((row, col), (r, c), self.board))


    def getBishopMoves1(self, row, col, moves):
        enemyCanBeEaten = True
        for t in range(row, 8):
            r = row + t
            c = col + t
            if (self.insideBoard(r, c) and enemyCanBeEaten):
                if (self.isNull(r, c) or self.isEnemy(r, c)):
                    moves.append(Move((row, col), (r, c), self.board))
                    if self.isEnemy(r, c):
                        enemyCanBeEaten = False
                if self.isАlly(r, c):
                    enemyCanBeEaten = False

        enemyCanBeEaten = True
        for t in range(0, 8):
            r = row - t
            c = col - t
            if (self.insideBoard(r, c) and enemyCanBeEaten):
                if (self.isNull(r, c) or self.isEnemy(r, c)):
                    moves.append(Move((row, col), (r, c), self.board))
                    if self.isEnemy(r, c):
                        enemyCanBeEaten = False
                if self.isАlly(r, c):
                    enemyCanBeEaten = False

        enemyCanBeEaten = True
        for t in range(0, 8):
            r = row + t
            c = col - t
            #if (self.insideBoard(r, c):

            if (self.insideBoard(r, c) and enemyCanBeEaten):
                if (self.isNull(r, c) or self.isEnemy(r, c)):
                    moves.append(Move((row, col), (r, c), self.board))
                    if self.isEnemy(r, c):
                        enemyCanBeEaten = False
                if self.isАlly(r,c):
                    enemyCanBeEaten = False

        enemyCanBeEaten = True
        for t in range(0, 8):
            r = row - t
            c = col + t
            if (self.insideBoard(r, c) and enemyCanBeEaten):
                if (self.isNull(r, c) or self.isEnemy(r, c)):
                    moves.append(Move((row, col), (r, c), self.board))
                    if self.isEnemy(r, c):
                        enemyCanBeEaten = False
                if self.isАlly(r, c):
                    enemyCanBeEaten = False

    def getBishopMoves2(self, row, col, moves):
        bishopMoves = [
            (-1, -1, -10, -10),
            (-1, 1, -10, 10),
            (1, -1, 10, -10),
            (1, 1, 10, 10),
        ]
        for m in bishopMoves:
            for r in range(row + m[0], m[2], m[0]):
                for c in range(col + m[1], m[3], m[1]):
                    enemyCanBeEaten = True
                    if self.insideBoard(r, c) and enemyCanBeEaten:
                        if self.isАlly(r, c):
                            enemyCanBeEaten = False
                        elif self.isEnemy(r, c):
                            enemyCanBeEaten = False
                            moves.append(Move((row, col), (r, c), self.board))
                        else:
                            moves.append(Move((row, col), (r, c), self.board))
                    #else:
                        #break
        #pass


    def getBishopMoves3(self, row, col, moves):
        bishopMoves = [
            (-1, -1, -100, -100),
            (-1, 1, -100, 100),
            (1, -1, 100, -100),
            (1, 1, 100, 100),
        ]


        for r in range(row - 1, -10, -1):
            for c in range(col - 1, -10, -1):
                enemyCanBeEaten = True
                if self.insideBoard(r, c) and enemyCanBeEaten:
                    if self.isАlly(r, c):
                        enemyCanBeEaten = False
                    elif self.isEnemy(r, c):
                        enemyCanBeEaten = False
                        moves.append(Move((row, col), (r, c), self.board))
                    else:
                        moves.append(Move((row, col), (r, c), self.board))
                else:
                    break


    def getBishopMoves(self, row, col, moves):
        arr = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        for t in arr:
            enemyCanBeEaten = True
            for i in range(1, 8):
                r = row + i * t[0]
                c = col + i * t[1]
                if self.insideBoard(r, c) and enemyCanBeEaten:
                    if self.isАlly(r, c):
                        enemyCanBeEaten = False
                    elif self.isEnemy(r, c):
                        enemyCanBeEaten = False
                        moves.append(Move((row, col), (r, c), self.board))
                    else:
                        moves.append(Move((row, col), (r, c), self.board))
                else:
                    break


    def getRockMoves(self, row, col, moves):
        arr = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for t in arr:
            enemyCanBeEaten = True
            for i in range(1, 8):
                r = row + i * t[0]
                c = col + i * t[1]
                if self.insideBoard(r, c) and enemyCanBeEaten:
                    if self.isАlly(r, c):
                        enemyCanBeEaten = False
                    elif self.isEnemy(r, c):
                        enemyCanBeEaten = False
                        moves.append(Move((row, col), (r, c), self.board))
                    else:
                        moves.append(Move((row, col), (r, c), self.board))
                else:
                    break

    def getQueenMoves(self, row, col, moves):
        self.getBishopMoves(row, col, moves)
        self.getRockMoves(row, col, moves)

    def getKingMoves(self, row, col, moves):
        for r in range (row-1, row + 2):
            for c in range(col - 1, col + 2):
                if (self.insideBoard(r, c) and self.isNull(r, c)):
                    moves.append(Move((row, col), (r, c), self.board))


class Move():
    ranksToRows = {'1': 7, '2': 6, '3': 5, '4': 4,
                   '5': 3, '6': 2, '7': 1, '8': 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
                   'e': 4, 'f': 5, 'g': 6, 'h': 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}


    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveId = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol

    '''
    переопределение класса equals
    '''
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveId == other.moveId
        return False

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
