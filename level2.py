import pygame
from gameControler import GameControler
from wall import Wall
from finishObject import FinishObject
from polarizer import Polarizer
from ray import Ray
import tkinter
from tkinter import simpledialog
import color



 

def start(screen, pol=[]):
    W, H = screen.get_size()
    gameControler = GameControler(screen)

    # ============================ СТАРТОВАЯ РАСТОНОВКА ============================
    wall = Wall(0, 0, 10, H)
    gameControler.objects.append(wall)

    wall = Wall(0, 0, W, 10)
    gameControler.objects.append(wall)

    wall = Wall(W-10, 0, 10, H)
    gameControler.objects.append(wall)

    wall = Wall(0, H-10, W, 10)
    gameControler.objects.append(wall)

    ray = Ray((20, 300,), (1, 0), width=2)
    gameControler.objects.append(ray)

    finish = FinishObject(W-60, H/2-50, 50, 100, 1/2, 30, color=color.BLUE)
    gameControler.objects.append(finish)

    startObjectLen = len(gameControler.objects)

    for i in pol:
        gameControler.objects.append(i)


    stop = False
    while not stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    stop = True
                if event.key == pygame.K_DELETE and startObjectLen < len(gameControler.objects):
                    gameControler.objects = gameControler.objects[:-1]
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                cor = pygame.mouse.get_pos()
                if event.button == 1 and (10 < cor[0] < W-10) and (10 < cor[0] < H-10): # Создание поляризатора   

                    root = tkinter.Tk()
                    root.withdraw()  # Скрыть главное окно
                    angle = simpledialog.askstring("Настройки", "Введите угол:")
                    root.destroy()  # Закрыть окно после ввода
                    pol = Polarizer(cor[0], cor[1], int(angle), width=20)
                    gameControler.objects.append(pol)


        gameControler.draw()
        pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
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
        pygame.display.update()
