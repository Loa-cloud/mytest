import unittest

from ChessMain import *
#from ChessEngine import *

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.testGame = GameState()
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
        self.moves = []
        #self.testMove = Move()

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_Move_makeMove(self):
        #self.moves.append(Move((0, 0), (2, 2), self.board))
        move = Move((0, 0), (2, 2), self.board)
        expectedBoard = [
            ['--', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', 'bR', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
        self.testGame.makeMove(move)
        self.assertEqual(expectedBoard, self.testGame.board)

    def test_Move_undoMove(self):
        #self.moves.append(Move((0, 0), (2, 2), self.board))
        #move = Move((6, 0), (5, 0), self.board)
        self.testGame.movelog.append(Move((6, 0), (5, 0), self.board))
        self.testGame.movelog.append(Move((1, 0), (2, 0), self.board))

        expectedMoveLog = []
        expectedMoveLog.append(Move((6, 0), (5, 0), self.board))

        self.testGame.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['--', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['bP', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', '--', '--', '--', '--', '--', '--', '--'],
            ['--', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]

        expectedBoard = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', '--', '--', '--', '--', '--', '--', '--'],
            ['--', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
        self.testGame.undoMove()
        self.assertEqual(expectedBoard, self.testGame.board)
        self.assertEqual(expectedMoveLog, self.testGame.movelog)

    def test_Move_getPawnMoves(self):
        expectedMoves = []
        expectedMoves.append(Move((6, 0), (5, 0), self.board))
        expectedMoves.append(Move((6, 0), (4, 0), self.board))
        expectedMoves.append(Move((6, 0), (5, 1), self.board))

        self.testGame.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', 'bP', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]

        actualMoves = []
        self.testGame.getPawnMoves(6, 0, actualMoves)
        self.assertEqual(expectedMoves, actualMoves)


    def test_Move_getKingMoves(self):
        expectedMoves = []
        expectedMoves.append(Move((1, 1), (0, 0), self.board))
        expectedMoves.append(Move((1, 1), (0, 1), self.board))
        expectedMoves.append(Move((1, 1), (0, 2), self.board))
        expectedMoves.append(Move((1, 1), (1, 0), self.board))
        expectedMoves.append(Move((1, 1), (1, 2), self.board))
        expectedMoves.append(Move((1, 1), (2, 0), self.board))
        expectedMoves.append(Move((1, 1), (2, 1), self.board))
        expectedMoves.append(Move((1, 1), (2, 2), self.board))
        self.testGame.board = [
            ['--', '--', '--', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['--', 'bK', '--', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
        actualMoves = []
        self.testGame.getKingMoves(1, 1, actualMoves)
        self.assertEqual(expectedMoves, actualMoves)

    def test_Move_getBishopMoves(self):
        expectedMoves = []
        expectedMoves.append(Move((1, 1), (2, 2), self.board))
        expectedMoves.append(Move((1, 1), (0, 0), self.board))
        expectedMoves.append(Move((1, 1), (2, 0), self.board))
        expectedMoves.append(Move((1, 1), (0, 2), self.board))

        self.testGame.board = [
            ['--', '--', '--', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['--', 'bB', '--', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', 'bP', '--', '--', '--', '--'],
            ['--', '--', '--', '--', 'bP', '--', '--', '--'],
            ['--', '--', '--', '--', '--', 'bP', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
        actualMoves = []
        self.testGame.whiteToMove = False
        self.testGame.getBishopMoves(1, 1, actualMoves)
        self.assertEqual(expectedMoves, actualMoves)


    def test_Move_getQueenMoves(self):
        expectedMoves = []
        expectedMoves.append(Move((1, 1), (2, 2), self.board))
        expectedMoves.append(Move((1, 1), (0, 0), self.board))
        expectedMoves.append(Move((1, 1), (2, 0), self.board))
        expectedMoves.append(Move((1, 1), (0, 2), self.board))

        expectedMoves.append(Move((1, 1), (1, 2), self.board))
        expectedMoves.append(Move((1, 1), (1, 0), self.board))
        expectedMoves.append(Move((1, 1), (2, 1), self.board))
        expectedMoves.append(Move((1, 1), (0, 1), self.board))

        self.testGame.board = [
            ['--', '--', '--', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['--', 'bR', '--', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', 'bP', '--', 'bP', '--', '--', '--', '--'],
            ['--', '--', '--', '--', 'bP', '--', '--', '--'],
            ['--', '--', '--', '--', '--', 'bP', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
        actualMoves = []
        self.testGame.whiteToMove = False
        self.testGame.getQueenMoves(1, 1, actualMoves)
        self.assertEqual(expectedMoves, actualMoves)

    def test_Move_getRockMoves(self):
        expectedMoves = []
        expectedMoves.append(Move((1, 1), (1, 2), self.board))
        expectedMoves.append(Move((1, 1), (1, 0), self.board))
        expectedMoves.append(Move((1, 1), (2, 1), self.board))
        expectedMoves.append(Move((1, 1), (0, 1), self.board))

        self.testGame.board = [
            ['--', '--', '--', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['--', 'bR', '--', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', 'bP', '--', 'bP', '--', '--', '--', '--'],
            ['--', '--', '--', '--', 'bP', '--', '--', '--'],
            ['--', '--', '--', '--', '--', 'bP', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
        actualMoves = []
        self.testGame.whiteToMove = False
        self.testGame.getRockMoves(1, 1, actualMoves)
        self.assertEqual(expectedMoves, actualMoves)

    def test_Move_getKnightMoves(self):
        expectedMoves = []

        expectedMoves.append(Move((2, 2), (0, 1), self.board))
        expectedMoves.append(Move((2, 2), (0, 3), self.board))
        expectedMoves.append(Move((2, 2), (4, 1), self.board))
        expectedMoves.append(Move((2, 2), (4, 3), self.board))
        expectedMoves.append(Move((2, 2), (1, 0), self.board))
        expectedMoves.append(Move((2, 2), (1, 4), self.board))
        expectedMoves.append(Move((2, 2), (3, 0), self.board))
        expectedMoves.append(Move((2, 2), (3, 4), self.board))

        self.testGame.board = [
            ['--', 'wP', '--', 'wP', '--', '--', 'bN', 'bR'],
            ['wP', '--', '--', '--', 'wP', '--', 'bP', 'bP'],
            ['--', '--', 'bN', '--', '--', '--', '--', '--'],
            ['wP', '--', '--', '--', 'wP', '--', '--', '--'],
            ['--', 'wP', '--', 'wP', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', 'bP', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
        actualMoves = []
        self.testGame.whiteToMove = False
        self.testGame.getKnightMoves(2, 2, actualMoves)
        self.assertEqual(expectedMoves, actualMoves)

