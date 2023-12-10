from tkinter import *
import pygame
class FormWindow:

    board = [[None for _ in range(8)] for _ in range(8)]
    is_moving = False

    def Init(self):
        root = Tk()
        root.title("METANIT.COM")
        root.geometry("250x200")
        root.mainloop()

    def Init_board(self):
        w = 20
        scale = 20
        for x in range(8):
            for y in range(8):
                if y % 2 == 0:
                    if not x % 2 == 0:
                        pygame.draw.rect(w, (255, 255, 255), (x * scale, y * scale, scale, scale))
                else:
                    if x % 2 == 0:
                        pygame.draw.rect(w, (255, 255, 255), (x * scale, y * scale, scale, scale))

    def Reset_board(self):
        pass

    def Message_game_over(self):
        pass

    def On_button_click(self):
        pass

    def Activate_yellow_path(self):
        pass

    def Deactivate_yellow_pass(self):
        pass

    def Deactivate_all_button(self):
        pass

    def Аctivate_all_button(self):
        pass

    def Switch_player_lable(self):
        pass

    def Ai(self):
        pass






















