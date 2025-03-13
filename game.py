import pygame as pg
from images.images import *

def game():
    pg.init()

    settings_screen = pg.display.set_mode((500, 400))
    settings_screen.fill((255, 255, 255))
    pg.display.set_caption("Minesweeper with pygame")

    is_game = True
    difficulty = ""

    while is_game:
        settings_screen.blit(settings_menu, (0, 0))
        if difficulty:
            if difficulty == "Beginner":
                settings_screen.blit(selecting_arrow, (8, 192))
            elif difficulty == "Intermediate":
                settings_screen.blit(selecting_arrow, (8, 260))
            elif difficulty == "Expert":
                settings_screen.blit(selecting_arrow, (8, 320))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_game = False
                break

            elif (event.type == pg.MOUSEBUTTONDOWN) and (pg.mouse.get_pressed(num_buttons=3)[0]):
                x, y = pg.mouse.get_pos()
                print(x, y)

                if (0 < x < 330) and (185 < y < 250):
                    print(1)
                    difficulty = "Beginner"
                elif () and ():
                    pass
                elif () and ():
                    pass

        pg.display.flip()

game()

print("end")