import pygame
from gameControler import GameControler
from wall import Wall
from finishObjectPol import FinishObjectPol
from polarizer import Polarizer
from ray import Ray
import tkinter
from tkinter import simpledialog
import color

pygame.init() 

W = 720
H = 600

screen = pygame.display.set_mode((W, H)) 

def start(pol=[]):
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

    finish = FinishObjectPol(W-60, H/2-50, 50, 100, 1/2, 30, color=color.BLUE)
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
                    return start(m)
        
        gameControler.calculate()
        if gameControler.win:
            return 1
        
        gameControler.draw()
        pygame.display.update()


print(start())