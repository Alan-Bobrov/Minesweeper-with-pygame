from pygame.image import load

def Load(image):
    return load(f"images/{image}.png")

settings_menu = Load("settings menu")