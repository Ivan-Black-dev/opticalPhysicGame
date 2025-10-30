import pygame 
from gameControler import GameControler
from ray import Ray
from finishObject import FinishObject
import color
from mirror import Mirror
import sys
from button import Button
import optic_choice

 


def start(screen, mirrors=[]):

    
    W, H = screen.get_size()

    pygame.font.init()
    font = pygame.font.Font(None, 45)
    exit_button_font = pygame.font.Font(None, 20)
    exit_button = Button((W-150, H-150, 100, 20), 'ВЫХОД', exit_button_font, (200, 200, 200), (255, 255, 255))


    gameControler = GameControler(screen)

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
    holdedMirror = None
    while not stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if exit_button.handle_event(event):
                optic_choice.start(screen)

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
                        if (x1 - x)**2 + (y1 - y)**2 <= 30:
                            hold = True
                            holdedMirror = i
                            pointNum = 1
                        elif  (x2 - x)**2 + (y2 - y)**2 <= 30:
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
                    x1, y1 = holdedMirror.x1, holdedMirror.y1
                    x2, y2 = holdedMirror.x2, holdedMirror.y2
                    colorMirorr = holdedMirror.color
                    gameControler.objects.append(Mirror(x1, y1, x2, y2, colorMirorr))
                    gameControler.objects.remove(holdedMirror)
                    del holdedMirror
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
        text_rect = text.get_rect(center=(W-75, H-100))  # Центрируем текст в окне
        
        exit_button.draw(screen)

        # Отображаем текст на экране
        screen.blit(text, text_rect)
        
        pygame.display.update()



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    m = []
                    for i in gameControler.objects:
                        if isinstance(i, Mirror):
                            m.append(i)
                    return start(screen, m)

        gameControler.calculate()
        if gameControler.win:
            return
        
        gameControler.draw()

        text = font.render("r - заново", True, (255, 255, 255))  # Белый цвет текста

        # Получаем прямоугольник текста для центрирования
        text_rect = text.get_rect(center=(W-75, H-100))  # Центрируем текст в окне

        # Отображаем текст на экране
        screen.blit(text, text_rect)

        pygame.display.update()

