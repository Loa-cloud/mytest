import unittest

from ChessMain import GameState
from Ai import *



class MyTestCase(unittest.TestCase):


    def setUp(self):
        self.testGame = GameState()


    def test_scoreMaterial_0(self):
        #actualMoves = []
        board = [
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', 'wQ', '--', 'wN', '--', '--', '--', '--'],
            ['--', '--', 'bQ', '--', '--', '--', '--', '--'],
            ['--', 'wR', 'wP', 'wB', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
        ]
        start = scoreMaterial(board)

        board = [
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', 'wN', '--', '--', '--', '--'],
            ['--', '--', 'bQ', '--', '--', '--', '--', '--'],
            ['--', 'wR', 'wP', 'wB', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
        ]
        q = scoreMaterial(board)

        board = [
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', 'wQ', '--', 'wN', '--', '--', '--', '--'],
            ['--', '--', 'bQ', '--', '--', '--', '--', '--'],
            ['--', '--', 'wP', 'wB', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
        ]
        r = scoreMaterial(board)

        board = [
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', 'wQ', '--', '--', '--', '--', '--', '--'],
            ['--', '--', 'bQ', '--', '--', '--', '--', '--'],
            ['--', 'wR', 'wP', 'wB', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
        ]
        n = scoreMaterial(board)

        board = [
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', 'wQ', '--', 'wN', '--', '--', '--', '--'],
            ['--', '--', 'bQ', '--', '--', '--', '--', '--'],
            ['--', 'wR', '--', 'wB', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
        ]
        p = scoreMaterial(board)

        # чем меньше счет тем лучше для черных
        self.assertGreater(start, q)
        self.assertLess(q, r)
        self.assertLess(r, n)
        self.assertLess(n, p)


    def test_scoreMaterial_1(self):
        board_1 = [
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', 'wR', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
        ]
        r = scoreMaterial(board_1)

        board_2 = [
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', 'wQ', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
        ]
        q = scoreMaterial(board_2)

        self.assertLess(r, q)


    def test_scoreMaterial_2(self):
        board_1 = [
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', 'bR', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
        ]
        r = scoreMaterial(board_1)

        board_2 = [
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', 'bP', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
        ]
        q = scoreMaterial(board_2)

        self.assertLess(r, q)




    def test_insideBoard_1(self):
        self.assertFalse(self.testGame.insideBoard(8, 0))

    def test_insideBoard_2(self):
        self.assertTrue(self.testGame.insideBoard(5, 5))

    def test_isEnemy_empty(self):
        self.assertFalse(self.testGame.isEnemy(5, 0))


    def test_isEnemy_enemy_white(self):
        self.testGame.whiteToMove = True
        self.assertTrue(self.testGame.isEnemy(0, 0))


    def test_isEnemy_enemy_black(self):
        self.testGame.whiteToMove = False
        self.assertTrue(self.testGame.isEnemy(7, 7))


    def test_isAlly_enemy_white(self):
        self.testGame.whiteToMove = True
        self.assertTrue(self.testGame.isАlly(7, 7))


    def test_isAlly_enemy_black(self):
        self.testGame.whiteToMove = False
        self.assertTrue(self.testGame.isАlly(0, 0))


    def test_isNull_1(self):
        self.assertTrue(self.testGame.isNull(3, 3))

    def test_isNull_2(self):
        self.assertFalse(self.testGame.isNull(0, 0))


    def test_getPawnMoves_1(self):
        actualMoves = []

        self.testGame.getPawnMoves(6, 0, actualMoves)
        self.assertEqual(2, len(actualMoves))

    def test_getPawnMoves_2(self):
        actualMoves = []
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

        self.testGame.getPawnMoves(6, 0, actualMoves)
        self.assertEqual(3, len(actualMoves))


    def test_getPawnMoves_3(self):
        actualMoves = []
        self.testGame.board = [
        ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
        ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['wP', 'bP', '--', '--', '--', '--', '--', '--'],
        ['--', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
        ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]

        self.testGame.getPawnMoves(5, 0, actualMoves)
        self.assertEqual(1, len(actualMoves))


    def test_getKnightMoves_1(self):
        actualMoves = []
        self.testGame.getKnightMoves(7, 1, actualMoves)

        self.assertEqual(2, len(actualMoves))


    def test_getKnightMoves_2(self):
        actualMoves = []
        self.testGame.board = [
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', 'bP', '--', 'bP', '--', '--', '--'],
            ['--', 'bP', '--', '--', '--', 'bP', '--', '--'],
            ['--', '--', '--', 'wN', '--', '--', '--', '--'],
            ['--', 'bP', '--', '--', '--', 'bP', '--', '--'],
            ['--', '--', 'bP', '--', 'bP', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
        ]
        self.testGame.getKnightMoves(3, 3, actualMoves)

        self.assertEqual(8, len(actualMoves))


    def test_getKnightMoves_3(self):
        actualMoves = []
        self.testGame.board = [
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wP', '--', 'wP', '--', 'wP', 'wP', 'wP', 'wP'],
            ['--', 'wP', 'wP', 'wP', '--', 'wP', 'wP', 'wP'],
            ['wP', 'wP', 'wN', 'wP', 'wP', 'wP', 'wP', 'wP'],
        ]
        self.testGame.getKnightMoves(7, 2, actualMoves)

        self.assertEqual(4, len(actualMoves))


    def test_getBishopMoves_1(self):
        actualMoves = []
        self.testGame.board = [
            ['--', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wP', '--', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wP', 'wP', '--', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wP', 'wP', 'wP', '--', 'wP', 'wP', 'wP', 'wP'],
            ['wP', 'wP', 'wP', 'wP', '--', 'wP', 'wP', 'wP'],
            ['wP', 'wP', 'wP', 'wP', 'wP', '--', 'wP', 'wP'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', '--', 'wP'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wB'],
        ]
        self.testGame.getBishopMoves(7, 7, actualMoves)

        self.assertEqual(7, len(actualMoves))


    def test_getBishopMoves_2(self):
        actualMoves = []
        self.testGame.board = [
            ['wB', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wP', '--', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wP', 'wP', '--', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wP', 'wP', 'wP', '--', 'wP', 'wP', 'wP', 'wP'],
            ['wP', 'wP', 'wP', 'wP', '--', 'wP', 'wP', 'wP'],
            ['wP', 'wP', 'wP', 'wP', 'wP', '--', 'wP', 'wP'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', '--', 'wP'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', '--'],
        ]
        self.testGame.getBishopMoves(0, 0, actualMoves)

        self.assertEqual(7, len(actualMoves))


    def test_getBishopMoves_3(self):
        actualMoves = []
        self.testGame.board = [
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wB'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', '--', 'wP'],
            ['wP', 'wP', 'wP', 'wP', 'wP', '--', 'wP', 'wP'],
            ['wP', 'wP', 'wP', 'wP', '--', 'wP', 'wP', 'wP'],
            ['wP', 'wP', 'wP', '--', 'wP', 'wP', 'wP', 'wP'],
            ['wP', 'wP', '--', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wP', '--', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['--', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
        ]
        self.testGame.getBishopMoves(0, 7, actualMoves)

        self.assertEqual(7, len(actualMoves))


    def test_getBishopMoves_4(self):
        actualMoves = []
        self.testGame.board = [
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', '--', 'wP'],
            ['wP', 'wP', 'wP', 'wP', 'wP', '--', 'wP', 'wP'],
            ['wP', 'wP', 'wP', 'wP', '--', 'wP', 'wP', 'wP'],
            ['wP', 'wP', 'wP', '--', 'wP', 'wP', 'wP', 'wP'],
            ['wP', 'wP', '--', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wP', '--', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wB', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
        ]
        self.testGame.getBishopMoves(7, 0, actualMoves)

        self.assertEqual(7, len(actualMoves))


    def test_getBishopMoves_5(self):
        actualMoves = []
        self.testGame.board = [
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', '--', 'wP'],
            ['wP', 'wP', 'wB', 'wP', 'wP', '--', 'wP', 'wP'],
            ['wP', 'wP', 'wP', 'wP', '--', 'wP', 'wP', 'wP'],
            ['wP', 'wP', 'wP', '--', 'wP', 'wP', 'wP', 'wP'],
            ['wP', 'wP', '--', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wP', '--', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
        ]
        self.testGame.getBishopMoves(2, 2, actualMoves)

        self.assertEqual(0, len(actualMoves))


    def test_getKingMoves_1(self):
        actualMoves = []
        self.testGame.board = [
            ['--', '--', '--', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['--', 'wK', '--', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['--', '--', '--', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
        ]
        self.testGame.getKingMoves(1, 1, actualMoves)

        self.assertEqual(8, len(actualMoves))


    def test_getRockMoves_1(self):
        actualMoves = []
        self.testGame.board = [
            ['wR', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
        ]
        self.testGame.getRockMoves(0, 0, actualMoves)

        self.assertEqual(14, len(actualMoves))


    def test_getQueenMoves_1(self):
        actualMoves = []
        self.testGame.board = [
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', 'wQ', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
        ]
        self.testGame.getQueenMoves(2, 2, actualMoves)

        self.assertEqual(25, len(actualMoves))


    def test_inCheck_1(self):
        self.whiteKingLocation = (0, 0)

        self.testGame.board = [
            ['wK', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
        ]
        actual = self.testGame.inCheck()
        self.assertFalse(actual)


    def test_inCheck_2(self):
        self.whiteKingLocation = (0, 0)


        self.testGame.board = [
            ['wK', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['bQ', '--', '--', '--', '--', '--', '--', '--'],
        ]
        actual = self.testGame.inCheck()
        self.assertTrue(actual)

    def test_suareUnderAttack_1(self):
        self.testGame.board = [
            ['wK', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['bQ', '--', '--', '--', '--', '--', '--', '--'],
        ]


        actual = self.testGame.suareUnderAttack(0, 0)
        self.assertTrue(actual)


    def test_suareUnderAttack_2(self):
        self.testGame.board = [
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', 'wK', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['bQ', '--', '--', '--', '--', '--', '--', '--'],
        ]


        actual = self.testGame.suareUnderAttack(1, 1)
        self.assertFalse(actual)



    def test_GameOver_1(self):
        self.testGame.board = self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]

        self.assertFalse(self.testGame.GameOver())

    def test_GameOver_2(self):
        self.testGame.board = self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', '--', 'wB', 'wN', 'wR'],
        ]

        self.assertTrue(self.testGame.GameOver())

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

    def test_Ai_preferKing(self):
        self.testGame.whiteToMove = False
        self.testGame.board = [
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', 'wQ', '--', 'wN', '--', '--', '--', '--'],
            ['--', '--', 'bQ', '--', '--', '--', '--', '--'],
            ['--', 'wR', '--', 'wB', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', 'wK', '--', '--', '--', '--', '--'],
        ]
        testValidMoves = []
        testValidMoves.append(Move((2, 2), (1, 3), self.testGame.board))
        testValidMoves.append(Move((2, 2), (3, 1), self.testGame.board))
        testValidMoves.append(Move((2, 2), (3, 2), self.testGame.board))
        testValidMoves.append(Move((2, 2), (7, 2), self.testGame.board))
        testValidMoves.append(Move((2, 2), (3, 3), self.testGame.board))
        testValidMoves.append(Move((2, 2), (1, 1), self.testGame.board))

        expectedMove = Move((2, 2), (7, 2), self.testGame.board)
        bestMove = findBestMove(self.testGame, testValidMoves)
        self.assertEqual(expectedMove, bestMove)

    def test_Ai_preferQueen(self):
        self.testGame.whiteToMove = False
        self.testGame.board = [
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', 'wQ', '--', 'wN', '--', '--', '--', '--'],
            ['--', '--', 'bQ', '--', '--', '--', '--', '--'],
            ['--', 'wR', 'wP', 'wB', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
        ]
        testValidMoves = []
        testValidMoves.append(Move((2, 2), (1, 3), self.testGame.board))
        testValidMoves.append(Move((2, 2), (3, 1), self.testGame.board))
        testValidMoves.append(Move((2, 2), (3, 2), self.testGame.board))
        testValidMoves.append(Move((2, 2), (3, 3), self.testGame.board))
        testValidMoves.append(Move((2, 2), (1, 1), self.testGame.board))

        expectedMove = Move((2, 2), (1, 1), self.testGame.board)
        bestMove = findBestMove(self.testGame, testValidMoves)
        self.assertEqual(expectedMove, bestMove)

    def test_Ai_preferRock(self):
        self.testGame.whiteToMove = False
        self.testGame.board = [
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', 'wN', '--', '--', '--', '--'],
            ['--', '--', 'bQ', '--', '--', '--', '--', '--'],
            ['--', 'wR', 'wP', 'wB', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
        ]
        testValidMoves = []
        testValidMoves.append(Move((2, 2), (1, 3), self.testGame.board))
        testValidMoves.append(Move((2, 2), (3, 1), self.testGame.board))
        testValidMoves.append(Move((2, 2), (3, 2), self.testGame.board))
        testValidMoves.append(Move((2, 2), (3, 3), self.testGame.board))

        expectedMove = Move((2, 2), (3, 1), self.testGame.board)
        bestMove = findBestMove(self.testGame, testValidMoves)
        self.assertEqual(expectedMove, bestMove)

    def test_Ai_preferBihop(self):
        self.testGame.whiteToMove = False
        self.testGame.board = [
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', 'bQ', '--', '--', '--', '--', '--'],
            ['--', '--', 'wP', 'wB', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
        ]
        testValidMoves = []
        testValidMoves.append(Move((2, 2), (3, 2), self.testGame.board))
        testValidMoves.append(Move((2, 2), (3, 3), self.testGame.board))

        expectedMove = Move((2, 2), (3, 3), self.testGame.board)
        bestMove = findBestMove(self.testGame, testValidMoves)
        self.assertEqual(expectedMove, bestMove)

    def test_Ai_preferKnight(self):
        self.testGame.whiteToMove = False
        self.testGame.board = [
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', 'bQ', '--', '--', '--', '--', '--'],
            ['--', '--', 'wP', 'wN', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
        ]
        testValidMoves = []
        testValidMoves.append(Move((2, 2), (3, 2), self.testGame.board))
        testValidMoves.append(Move((2, 2), (3, 3), self.testGame.board))

        expectedMove = Move((2, 2), (3, 3), self.testGame.board)
        bestMove = findBestMove(self.testGame, testValidMoves)
        self.assertEqual(expectedMove, bestMove)

    def test_Ai_preferPawn(self):
        self.testGame.whiteToMove = False
        self.testGame.board = [
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', 'bQ', '--', '--', '--', '--', '--'],
            ['--', '--', 'wP', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
        ]
        testValidMoves = []
        testValidMoves.append(Move((2, 2), (0, 2), self.testGame.board))
        testValidMoves.append(Move((2, 2), (3, 2), self.testGame.board))
        testValidMoves.append(Move((2, 2), (1, 1), self.testGame.board))
        expectedMove = Move((2, 2), (3, 2), self.testGame.board)
        bestMove = findBestMove(self.testGame, testValidMoves)
        self.assertEqual(expectedMove, bestMove)

    def test_Move_makeMove(self):
        # self.moves.append(Move((0, 0), (2, 2), self.board))
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
            ['--', 'bQ', '--', 'bP', 'bP', 'bP', 'bP', 'bP'],
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

if __name__ == '__main__':
    unittest.main()
