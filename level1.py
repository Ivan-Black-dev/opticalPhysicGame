import pygame 
from gameControler import GameControler
import time
from ray import Ray
from finishObject import FinishObject
import color
from mirror import Mirror
from wall import Wall

# initializing the constructor 
pygame.init() 

W = 720
H = 600

screen = pygame.display.set_mode((W, H)) 
pygame.font.init()
font = pygame.font.Font(None, 45)

def start(mirrors=[]):
    gameControler = GameControler(screen)
    # ============================== СТЕНЫ ==============================
    wall = Wall(0, 0, 10, H)
    gameControler.objects.append(wall)

    wall = Wall(0, 0, W, 10)
    gameControler.objects.append(wall)

    wall = Wall(W-10, 0, 10, H)
    gameControler.objects.append(wall)

    wall = Wall(0, H-10, W, 10)
    gameControler.objects.append(wall)

    wall = Wall(350, 0, 10, 350)
    gameControler.objects.append(wall)

    wall = Wall(550, H-300, 10, 300)
    gameControler.objects.append(wall)

    wall = Wall(550, H-300, 300, 10)
    gameControler.objects.append(wall)

    ray = Ray((20, 300,), (1, 0), width=2)
    gameControler.objects.append(ray)

    finish = FinishObject(W-100, 10, 75, 10, I=1, angle=-1)
    gameControler.objects.append(finish)

    startObjectLen = len(gameControler.objects)


    for i in mirrors:
        gameControler.objects.append(i)

    stop = False
    points = []
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
                if event.button == 1:  
                    points.append(event.pos)  
                    if len(points) == 2:
                        gameControler.objects.append(Mirror(points[0][0], points[0][1], points[1][0], points[1][1]))
                        points = [] 


        gameControler.draw()

        if len(points) == 1:
            pygame.draw.line(screen, color.GRAY, points[0], pygame.mouse.get_pos())

        text = font.render("s - старт", True, (255, 255, 255))  # Белый цвет текста

        # Получаем прямоугольник текста для центрирования
        text_rect = text.get_rect(center=(640, 400))  # Центрируем текст в окне

        # Отображаем текст на экране
        screen.blit(text, text_rect)
        
        pygame.display.update()



    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    m = []
                    for i in gameControler.objects:
                        if isinstance(i, Mirror):
                            m.append(i)
                    return start(m)

        
        gameControler.calculate()
        if gameControler.win:
            return 1
        
        gameControler.draw()

        text = font.render("r - заново", True, (255, 255, 255))  # Белый цвет текста

        # Получаем прямоугольник текста для центрирования
        text_rect = text.get_rect(center=(640, 400))  # Центрируем текст в окне

        # Отображаем текст на экране
        screen.blit(text, text_rect)

        pygame.display.update()
