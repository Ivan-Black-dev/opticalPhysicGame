import pygame
import sys

import pol_easy     # файл с легким уровнем
import pol_medium   # файл со средним уровнем
import pol_hard     # файл со сложным уровнем
import main

from win_menu.pol import easy, hard, medium

def start(screen):
    clock = pygame.time.Clock()
    WIDTH, HEIGHT = screen.get_size()

    # Загрузка фона и кнопок
    background = pygame.image.load("assets/background.png").convert()
    easy_img = pygame.image.load("assets/pixel_button.png").convert_alpha()
    medium_img = pygame.image.load("assets/pixel_button.png").convert_alpha()
    hard_img = pygame.image.load("assets/pixel_button.png").convert_alpha()
    back_img = pygame.image.load("assets/pixel_button.png").convert_alpha()

    btn_w = int(WIDTH * 0.2)
    btn_h = int(HEIGHT * 0.12)
    easy_img = pygame.transform.smoothscale(easy_img, (btn_w, btn_h))
    medium_img = pygame.transform.smoothscale(medium_img, (btn_w, btn_h))
    hard_img = pygame.transform.smoothscale(hard_img, (btn_w, btn_h))
    back_img = pygame.transform.smoothscale(back_img, (btn_w, btn_h))

    center_x = WIDTH // 2
    easy_rect = easy_img.get_rect(center=(center_x, HEIGHT // 2 - btn_h * 1.5))
    medium_rect = medium_img.get_rect(center=(center_x, HEIGHT // 2))
    hard_rect = hard_img.get_rect(center=(center_x, HEIGHT // 2 + btn_h * 1.5))
    back_rect = back_img.get_rect(center=(center_x, HEIGHT // 2 + btn_h * 3))

    easy_pressed = False
    medium_pressed = False
    hard_pressed = False
    back_pressed = False

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True

        screen.blit(pygame.transform.smoothscale(background, (WIDTH, HEIGHT)), (0, 0))

        # Обработка кнопок
        if easy_rect.collidepoint(mouse_pos):
            if mouse_clicked:
                easy_pressed = True
            elif easy_pressed:
                easy_pressed = False
                win = pol_easy.start(screen)
                easy.show_menu(screen, win)

        else:
            easy_pressed = False

        if medium_rect.collidepoint(mouse_pos):
            if mouse_clicked:
                medium_pressed = True
            elif medium_pressed:
                medium_pressed = False
                win = pol_medium.start(screen)
                medium.show_menu(screen, win)
        else:
            medium_pressed = False

        if hard_rect.collidepoint(mouse_pos):
            if mouse_clicked:
                hard_pressed = True
            elif hard_pressed:
                hard_pressed = False
                win = pol_hard.start(screen)
                hard.show_menu(screen, win)
        else:
            hard_pressed = False

        if back_rect.collidepoint(mouse_pos):
            if mouse_clicked:
                back_pressed = True
            elif back_pressed:
                back_pressed = False
                main.start()  # Приступаем к главному меню main.py (замени на нужную функцию)
        else:
            back_pressed = False

        def draw_button(img, rect, pressed):
            if pressed:
                pressed_rect = rect.move(5, 5)
                screen.blit(img, pressed_rect)
            else:
                screen.blit(img, rect)

        draw_button(easy_img, easy_rect, easy_pressed)
        draw_button(medium_img, medium_rect, medium_pressed)
        draw_button(hard_img, hard_rect, hard_pressed)
        draw_button(back_img, back_rect, back_pressed)

        pygame.display.flip()
        clock.tick(60)
