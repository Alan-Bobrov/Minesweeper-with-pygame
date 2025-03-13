from pygame.image import load

def Load(image):
    return load(f"{image}.png")

settings_menu = Load("settings menu")