import unittest

from ChessMain import GameState
from Ai import *



class MyTestCase(unittest.TestCase):


    def setUp(self):
        self.testGame = GameState()


    def test_scoreMaterial_1(self):
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


    def test_getPawnMoves_1(self):
        actualMoves = []

        self.testGame.getPawnMoves(6, 0, actualMoves)
        self.assertEqual(2, len(actualMoves))


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


    def test_isNull(self):
        self.assertTrue(self.testGame.isNull(3, 3))


    def test_getKnightMoves_1(self):


        # expectedMoves = [1,2]
        actualMoves = []
        self.testGame.getKnightMoves(7, 2, actualMoves)

        self.assertEqual(2, len(actualMoves))


    def test_getKnightMoves_2(self):


        # expectedMoves = [1,2]
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


        # expectedMoves = [1,2]
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


        # expectedMoves = [1,2]
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


        # expectedMoves = [1,2]
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


        # expectedMoves = [1,2]
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


        # expectedMoves = [1,2]
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


        # expectedMoves = [1,2]
        actualMoves = []
        self.testGame.board = [
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', '--', 'wP'],
            ['wP', 'wP', 'wB', 'wP', 'wP', '--', 'wP', 'wP'],
            ['wP', 'wP', 'wP', 'wP', '--', 'wP', 'wP', 'wP'],
            ['wP', 'wP', 'wP', '--', 'wP', 'wP', 'wP', 'wP'],
            ['wP', 'wP', '--', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wP', '--', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wB', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
        ]
        self.testGame.getBishopMoves(2, 2, actualMoves)

        self.assertEqual(0, len(actualMoves))


    def test_getKingMoves_1(self):


        # expectedMoves = [1,2]
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


    def test_inCheck_3(self):
        pass
        #self.whiteKingLocation = (0, 0)


        #self.testGame.board = [
        #    ['wK', '--', '--', '--', '--', '--', '--', '--'],
        #   ['--', '--', '--', '--', '--', '--', '--', '--'],
        #    ['--', '--', '--', '--', '--', '--', '--', '--'],
        #    ['--', '--', '--', '--', '--', '--', '--', '--'],
        #    ['--', '--', '--', '--', '--', '--', '--', '--'],
        #   ['--', '--', 'bR', '--', '--', '--', '--', '--'],
        #    ['--', '--', '--', '--', '--', '--', '--', '--'],
        #   ['bQ', '--', '--', '--', '--', '--', '--', '--'],
        #]
        #actual = self.testGame.inCheck()
        #self.assertFalse(actual)


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

if __name__ == '__main__':
    unittest.main()
