

class One_move:
    def __init__(self, value, i, j):
        self.value = value
        self.i = i
        self.j = j

class Figure:
    def __init__(self, color, position):
        self.name = "Figure"
        self.value = 0
        self.position = position
        self.color = color
        #self.color = color.lower()
        #self.opponent_color = 'b' if self.color == 'w' else 'w'
        #if color not in ['b', 'w']:
        #    raise TypeError('%s color should be \'w\' or \'b\'' % self.name)

    def Get_moves(self):
        pass

    def Get_diogonal_moves(self):
        pass

    def Get_line_moves(self):
        pass

class King(Figure):
    def __init__(self, color, position):
        self.name = "Figure"
        self.value = 100
        self.position = position
        self.color = color
        self.image = 'images/b_king.jpg'


    def Get_moves(self):
        pass

class Queen(Figure):

    def Get_moves(self):
        pass


class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]

        self.board[4][7] = King('b', (4, 7))
        self.board[3][7] = Queen('b', (3, 7))
        self.board[4][0] = King('w', (4, 0))
        self.board[3][0] = Queen('w', (3, 0))

        self.curr_player = 'w'

        self.played_moves = []

    def Change_player(self):
        pass

    def Change_moving(self):
        pass

    def Reset(self):
        pass

    def Is_inside_board(self):
        pass

    # возможно это все здесь не нужно, а понадобится в фигуре?
    def Is_Enemy(self):
        pass

    def Is_Null(self):
        pass

    def Is_Player(self):
        pass

    # скорее всего это можно будет убрать. у фигуры теперь есть имя
    def Get_type_of_figure(self):
        pass

    def Get_king_move(self):
        pass

    def Get_queen_move(self):
        pass

    def Get_rock_move(self):
        pass

    def Get_bishop_move(self):
        pass

    def Get_pawn_move(self):
        pass

    def Is_Mate(self):
        pass

    def Get_Moves_current_player(self):
        pass

    def Get_Best_Moves(self):
        pass
























