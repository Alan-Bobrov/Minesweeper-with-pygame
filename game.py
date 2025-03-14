import pygame as pg
from images.images import *

def SettingsMenu():
    pg.init()

    settings_screen = pg.display.set_mode((500, 400))
    settings_screen.fill((255, 255, 255))
    pg.display.set_caption("Minesweeper with pygame")

    difficulty = ""

    while True:
        settings_screen.blit(settings_menu, (0, 0))
        if difficulty:
            if difficulty == "Beginner":
                settings_screen.blit(selecting_arrow, (8, 192))
            elif difficulty == "Intermediate":
                settings_screen.blit(selecting_arrow, (8, 252))
            elif difficulty == "Expert":
                settings_screen.blit(selecting_arrow, (8, 312))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0

            elif (event.type == pg.MOUSEBUTTONDOWN):
                x, y = pg.mouse.get_pos()
                print(x, y)

                if (0 < x < 415) and (185 < y < 250):
                    if difficulty == "Beginner":
                        print(1)
                        return 1
                    difficulty = "Beginner"
                elif (0 < x < 415) and (251 < y < 300):
                    if difficulty == "Intermediate":
                        print(2)
                        return 2
                    difficulty = "Intermediate"
                elif (0 < x < 415) and (300 < y):
                    if difficulty == "Expert":
                        print(3)
                        return 3
                    difficulty = "Expert"

        pg.display.flip()

def game():
    settings = SettingsMenu()
    print(settings)
    if settings == 0:
        return 0
    else:
        print(1)
        


game()
print("end")