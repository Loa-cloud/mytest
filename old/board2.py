from tkinter import *
import pygame

from chess import ChessBoard


class Game:
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((900, 650))
        pygame.display.set_caption('Chess')

        #self.settings = {'board_image': 'images/orange_board.png'}
        #self.board_image = pygame.image.load(self.settings['board_image'])

        self.clock = pygame.time.Clock()
        self.chess_board = ChessBoard()

        self.curr_selected_piece = None
        self.curr_poss_moves = []
        #self.all_poss_moves = self.get_all_poss_moves()

        self.white_pieces_taken_images = []
        self.black_pieces_taken_images = []

        self.play_game()

        def play_game(self):
            """Loop that executes the game"""
            while True:

                # Draw whole window (and draw board)
                self.draw_window()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()

                    if event.type == pygame.MOUSEBUTTONUP:
                        # Get user click
                        self.get_user_click()

        def draw_window(self):
            """Draws everything in the window"""
            self.game_display.fill(white)
            # Draw side menu
            #self.draw_side_menu()
            # Draw bottom menu
            # Draw board
            self.draw_board()
            pygame.display.update()

        def get_user_click(self):
            pass

        def draw_board(self):
            pass

class Game2:
    def __init__(self):
        pass

class Square:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.abs_x = x * width
        self.abs_y = y * height
        self.abs_pos = (self.abs_x, self.abs_y)
        self.pos = (x, y)
        self.color = 'light' if (x + y) % 2 == 0 else 'dark'
        self.draw_color = (220, 208, 194) if self.color == 'light' else (53, 53, 53)
        self.highlight_color = (100, 249, 83) if self.color == 'light' else (0, 228, 10)
        self.occupying_piece = None
        self.coord = self.get_coord()
        self.highlight = False
        self.rect = pygame.Rect(
            self.abs_x,
            self.abs_y,
            self.width,
            self.height
        )

    # get the formal notation of the tile
    def get_coord(self):
        columns = 'abcdefgh'
        return columns[self.x] + str(self.y + 1)

    def draw(self, display):
        # configures if tile should be light or dark or highlighted tile
        if self.highlight:
            pygame.draw.rect(display, self.highlight_color, self.rect)
        else:
            pygame.draw.rect(display, self.draw_color, self.rect)
        # adds the chess piece icons
        if self.occupying_piece != None:
            centering_rect = self.occupying_piece.img.get_rect()
            centering_rect.center = self.rect.center
            display.blit(self.occupying_piece.img, centering_rect.topleft)

white = (255, 255, 255)
blue = (34, 0, 255)
red = (209, 9, 9)
black = (0, 0, 0)
Square()
