import pygame
import sys
import main
import training_level  # модуль для тренировки
import generation_level  # модуль для генерации

from win_menu.optical import generation, traning


def start(screen):
    pygame.init()
    clock = pygame.time.Clock()

    WIDTH, HEIGHT = screen.get_size()

    # Загрузка фона и кнопок
    background = pygame.image.load("assets/geom_back.png").convert()
    training_img = pygame.image.load("assets/tren.png").convert_alpha()
    generation_img = pygame.image.load("assets/generation.png").convert_alpha()
    main_img = pygame.image.load("assets/out.png").convert_alpha()

    # Размер кнопок 20% ширины и 15% высоты
    btn_width = int(WIDTH * 0.3)
    btn_height = int(HEIGHT * 0.15)
    training_img = pygame.transform.smoothscale(training_img, (btn_width, btn_height))
    generation_img = pygame.transform.smoothscale(generation_img, (btn_width, btn_height))
    main_img = pygame.transform.smoothscale(main_img, (btn_width, btn_height))

    # Позиции кнопок (по центру, вертикально)
    center_x = WIDTH // 2
    training_rect = training_img.get_rect(center=(center_x, HEIGHT // 2 - btn_height * 1.5))
    generation_rect = generation_img.get_rect(center=(center_x, HEIGHT // 2))
    main_rect = main_img.get_rect(center=(center_x, HEIGHT // 2 + btn_height * 1.5))

    running = True
    training_pressed = False
    generation_pressed = False
    main_pressed = False

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

        # Обработка нажатий и эффект смещения кнопки при нажатии
        if training_rect.collidepoint(mouse_pos):
            if mouse_clicked:
                training_pressed = True
            elif training_pressed:
                training_pressed = False
                win = training_level.start(screen)  # Запуск модуля тренировки
                traning.show_menu(screen, win)
        else:
            training_pressed = False

        if generation_rect.collidepoint(mouse_pos):
            if mouse_clicked:
                generation_pressed = True
            elif generation_pressed:
                generation_pressed = False
                win = generation_level.start(screen)  # Запуск модуля генерации
                generation.show_menu(screen, win)
        else:
            generation_pressed = False

        if main_rect.collidepoint(mouse_pos):
            if mouse_clicked:
                main_pressed = True
            elif main_pressed:
                main_pressed = False
                main.start()  # Вызов функции main из модуля main
        else:
            main_pressed = False

        def draw_button(image, rect, pressed):
            if pressed:
                pressed_rect = rect.move(5, 5)
                screen.blit(image, pressed_rect)
            else:
                screen.blit(image, rect)

        draw_button(training_img, training_rect, training_pressed)
        draw_button(generation_img, generation_rect, generation_pressed)
        draw_button(main_img, main_rect, main_pressed)

        pygame.display.flip()
        clock.tick(60)
