import pygame 
from gameControler import GameControler
import time
from ray import Ray
from finishObject import FinishObject
import color
from mirror import Mirror
from wall import Wall


 


def start(screen, mirrors=[]):

    pygame.font.init()
    font = pygame.font.Font(None, 45)

    W, H = screen.get_size()

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
    hold = False
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
                    for i in gameControler.objects[startObjectLen:]:
                        x1, y1 = i.x1, i.y1
                        x2, y2 = i.x2, i.y2
                        x, y = event.pos
                        if (x1 - x)**2 + (y1 - y)**2 <= 20:
                            hold = True
                            holdedMirror = i
                            pointNum = 1
                        elif  (x2 - x)**2 + (y2 - y)**2 <=20:
                            hold = True
                            holdedMirror = i
                            pointNum = 2
                    if not hold:
                        points.append(event.pos)  
                        if len(points) == 2:
                            gameControler.objects.append(Mirror(points[0][0], points[0][1], points[1][0], points[1][1]))
                            points = [] 
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and hold:
                    hold = False
        
        if hold:
            x, y = pygame.mouse.get_pos()
            if pointNum == 1:
                holdedMirror.x1 = x
                holdedMirror.y1 = y
            elif pointNum == 2:
                holdedMirror.x2 = x
                holdedMirror.y2 = y


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
                    return start(screen, m)

        gameControler.calculate()
        if gameControler.win:
            count = len(gameControler.objects) - startObjectLen
            if count == 2:
                return 3
            elif count == 4:
                return 2
            elif count > 4:
                return 1
        
        gameControler.draw()

        text = font.render("r - заново", True, (255, 255, 255))  # Белый цвет текста

        # Получаем прямоугольник текста для центрирования
        text_rect = text.get_rect(center=(640, 400))  # Центрируем текст в окне

        # Отображаем текст на экране
        screen.blit(text, text_rect)

        pygame.display.update()
