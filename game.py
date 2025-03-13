import pygame as pg
from images.images import *

def game():
    pg.init()

    settings_screen = pg.display.set_mode((500, 400))
    settings_screen.fill((255, 255, 255))
    pg.display.set_caption("Minesweeper with pygame")
    
    is_game = True

    while is_game:
        settings_screen.blit(settings_menu, (0, 0))
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_game = False
                break
                    
            elif (event.type == pg.MOUSEBUTTONDOWN) and (pg.mouse.get_pressed(num_buttons=3)[0]):
                x, y = pg.mouse.get_pos()
                print(x, y)

        pg.display.flip()

game()

print("end")