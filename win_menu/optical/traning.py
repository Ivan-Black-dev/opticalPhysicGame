import pygame

def show_menu(screen, win):
    bg_img = pygame.image.load("assets/win.png")
    background_scaled = pygame.transform.scale(bg_img, screen.get_size())
    stop = False
    screen.blit(background_scaled, (0,0))
    pygame.display.update()
    while not stop:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                stop = True