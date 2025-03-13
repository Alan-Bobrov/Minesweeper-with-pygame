import pygame as pg

def game():
    pg.init()

    screen = pg.display.set_mode((500, 400))
    screen.fill((255, 255, 255))

    is_game = True

    while is_game:

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