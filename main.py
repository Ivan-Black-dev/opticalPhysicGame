import pygame
import sys

import level1_teory  # файл с теорией перед уровнем 1
import level2_teory  # файл с теорией перед уровнем 2
import optic_choice  # модуль выбора для optic_choise
import polarization_choice  # модуль выбора для polarization_choice


def start():
    pygame.init()

    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w, info.current_h

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Главное меню")

    clock = pygame.time.Clock()

    # Загрузка изображений
    background = pygame.image.load("assets/background.png").convert()
    title_img = pygame.image.load("assets/pixel_button.png").convert_alpha()
    level1_img = pygame.image.load("assets/pixel_button.png").convert_alpha()
    level2_img = pygame.image.load("assets/pixel_button.png").convert_alpha()
    exit_img = pygame.image.load("assets/pixel_button.png").convert_alpha()  # кнопка выхода

    # Размеры кнопок и заголовка
    button_width, button_height = int(WIDTH * 0.1), int(HEIGHT * 0.1)
    title_height = int(HEIGHT * 0.2)
    title_width = int(title_img.get_width() * (title_height / title_img.get_height()))  # сохр. пропорции

    title_img = pygame.transform.smoothscale(title_img, (title_width, title_height))
    level1_img = pygame.transform.smoothscale(level1_img, (button_width, button_height))
    level2_img = pygame.transform.smoothscale(level2_img, (button_width, button_height))
    exit_img = pygame.transform.smoothscale(exit_img, (button_width, button_height))

    center_x = WIDTH // 2

    title_rect = title_img.get_rect(center=(center_x, HEIGHT // 2 - button_height * 2))
    level1_rect = level1_img.get_rect(center=(center_x, HEIGHT // 2 - button_height // 4))
    level2_rect = level2_img.get_rect(center=(center_x, HEIGHT // 2 + button_height))
    exit_rect = exit_img.get_rect(center=(center_x, HEIGHT // 2 + button_height * 2.5))

    def draw_button(image, rect, pressed):
        """Рисуем кнопку с эффектом нажатия"""
        if pressed:
            offset_rect = rect.move(5, 5)
            screen.blit(image, offset_rect)
        else:
            screen.blit(image, rect)

    running = True
    level1_pressed = False
    level2_pressed = False
    exit_pressed = False

    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True

        screen.blit(pygame.transform.smoothscale(background, (WIDTH, HEIGHT)), (0, 0))
        screen.blit(title_img, title_rect)

        # Обработка нажатий кнопок с запуском теории, а затем уровня без дополнительного клика
        if level1_rect.collidepoint(mouse_pos):
            if mouse_clicked:
                level1_pressed = True
            else:
                if level1_pressed:
                    level1_pressed = False
                    # Запускаем теорию
                    level1_teory.start(screen)
                    # Затем запускаем выбор оптики
                    optic_choice.start(screen)
        else:
            level1_pressed = False

        if level2_rect.collidepoint(mouse_pos):
            if mouse_clicked:
                level2_pressed = True
            else:
                if level2_pressed:
                    level2_pressed = False
                    level2_teory.start(screen)
                    polarization_choice.start(screen)
        else:
            level2_pressed = False

        if exit_rect.collidepoint(mouse_pos):
            if mouse_clicked:
                exit_pressed = True
            else:
                if exit_pressed:
                    exit_pressed = False
                    running = False
        else:
            exit_pressed = False

        draw_button(level1_img, level1_rect, level1_pressed)
        draw_button(level2_img, level2_rect, level2_pressed)
        draw_button(exit_img, exit_rect, exit_pressed)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    start()
