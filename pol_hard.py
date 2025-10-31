import pygame
from gameControler import GameControler
from wall import Wall
from finishObject import FinishObject
from polarizer import Polarizer
from ray import Ray
import color
import sys
from dialogBox import DialogBox
import polarization_choice
from button import Button


 

def start(screen, pol=[]):
    
    W, H = screen.get_size()
    gameControler = GameControler(screen)

    dialog_font = pygame.font.Font(None, 20)
    dialog = DialogBox((50, 50, 300, 70), dialog_font)
    
    font = pygame.font.Font(None, 39)
    exit_button_font = pygame.font.Font(None, 40)
    exit_button = Button((W-300+10, H-200, 200, 40), 'ВЫХОД', exit_button_font, (200, 200, 200), (255, 255, 255))


    # ============================ СТАРТОВАЯ РАСТОНОВКА ============================
    wall = Wall(W-300, H-300, 300, 10)
    gameControler.objects.append(wall)

    wall = Wall(W-300, H-300, 10, 300)
    gameControler.objects.append(wall)

    wall = Wall(0, 0, 10, H)
    gameControler.objects.append(wall)

    wall = Wall(0, 0, W, 10)
    gameControler.objects.append(wall)

    wall = Wall(W-10, 0, 10, H)
    gameControler.objects.append(wall)

    wall = Wall(0, H-10, W, 10)
    gameControler.objects.append(wall)

    ray = Ray((15, H/2,), (1, 0), width=2)
    gameControler.objects.append(ray)

    finish = FinishObject(W-60, H/2-50, 50, 100, 0.5, 30, (255, 255, 255))
    gameControler.objects.append(finish)

    startObjectLen = len(gameControler.objects)

    for i in pol:
        gameControler.objects.append(i)


    stop = False
    while not stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            
            if exit_button.handle_event(event):
                polarization_choice.start(screen)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    stop = True
                if event.key == pygame.K_DELETE and startObjectLen < len(gameControler.objects):
                    gameControler.objects = gameControler.objects[:-1]
            
            if dialog.active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        dialog.deactivate()
                result = dialog.handle_event(event)
                if result is not None:
                    angle = result
                    # Создаете поляризатор после ввода
                    pol = Polarizer(cor[0], cor[1], int(angle), width=40)
                    gameControler.objects.append(pol)
                    dialog.deactivate()

            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    cor = pygame.mouse.get_pos()
                    if event.button == 1:
                        dialog.activate("Введите угол:")

        gameControler.draw()
        if dialog.active:
            dialog.draw(screen)

        text = font.render(f"Сейчас: I = {round(ray.intensiv_and_angle[-1][0], 2)}", True, (255, 255, 255))
        text_rect = text.get_rect(topleft=(20, H // 2 + 30))
        screen.blit(text, text_rect)

        text = font.render(f"Нужно: I = 0.16", True, (255, 255, 255))
        text_rect = text.get_rect(topleft=(W-200, H // 2 + 100))
        screen.blit(text, text_rect)

        text = font.render("s - старт", True, (255, 255, 255))  # Белый цвет текста
        text_rect = text.get_rect(topleft=(W-300+10, H-300+10))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        text = font.render("r - заново", True, (255, 255, 255))  # Белый цвет текста
        text_rect = text.get_rect(topleft=(W-300+10, H-300+30))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        text = font.render("del - удалить", True, (255, 255, 255))  # Белый цвет текста
        text_rect = text.get_rect(topleft=(W-300+10, H-300+55))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        text = font.render("поляризатор", True, (255, 255, 255))  # Белый цвет текста
        text_rect = text.get_rect(topleft=(W-300+10, H-300+75))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        exit_button.draw(screen)

        pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if exit_button.handle_event(event):
                polarization_choice.start(screen)
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    m = []
                    for i in gameControler.objects:
                        if isinstance(i, Polarizer):
                            m.append(i)
                    return start(screen, m)
        
        gameControler.calculate()
        if gameControler.win:
            I, _ = ray.intensiv_and_angle[-1]
            if I == 0.5:
                return 2
            elif 0.16 - 0.06 <= I <= 0.16 + 0.06:
                return 3
            else:
                return 1

        gameControler.draw()    

        text = font.render(f"Сейчас: I = {round(ray.intensiv_and_angle[-1][0], 2)}", True, (255, 255, 255))
        text_rect = text.get_rect(topleft=(20, H // 2 + 30))
        screen.blit(text, text_rect)

        text = font.render(f"Нужно: I = 0.16", True, (255, 255, 255))
        text_rect = text.get_rect(topleft=(W-200, H // 2 + 100))
        screen.blit(text, text_rect)

        text = font.render("s - старт", True, (255, 255, 255))  # Белый цвет текста
        text_rect = text.get_rect(topleft=(W-300+10, H-300+10))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        text = font.render("r - заново", True, (255, 255, 255))  # Белый цвет текста
        text_rect = text.get_rect(topleft=(W-300+10, H-300+30))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        text = font.render("del - удалить", True, (255, 255, 255))  # Белый цвет текста
        text_rect = text.get_rect(topleft=(W-300+10, H-300+55))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        text = font.render("поляризатор", True, (255, 255, 255))  # Белый цвет текста
        text_rect = text.get_rect(topleft=(W-300+10, H-300+75))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        exit_button.draw(screen)

        pygame.display.update()