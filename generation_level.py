import pygame 
from gameControler import GameControler
from ray import Ray
from finishObject import FinishObject
import color
from mirror import Mirror
import sys
from generator import Generator
from button import Button
import optic_choice
from wall import Wall


 


def start(screen, mirrors=[], walls=[],start_ray=[],firstLaunch=True):

    W, H = screen.get_size()

    pygame.font.init()
    font = pygame.font.Font(None, 39)
    exit_button_font = pygame.font.Font(None, 40)
    exit_button = Button((W-300+10, H-120, 200, 40), 'ВЫХОД', exit_button_font, (200, 200, 200), (255, 255, 255))

    generator = Generator(W, H)
    gameControler = GameControler(screen)

    wall = Wall(W-300, H-300, 300, 10)
    gameControler.objects.append(wall)

    wall = Wall(W-300, H-300, 10, 300)
    gameControler.objects.append(wall)


    if firstLaunch:
        walls, points = generator.generate_walls()
        for wall in walls:
            gameControler.objects.append(wall)


        if points[0] == 1:
            start_ray = [(0, 0), (1, 1)]
            ray = Ray((0, 0), (1, 1), width=2)
        elif points[0] == 2:
            start_ray = [(0, H), (1, -1)]
            ray = Ray((0, H), (1, -1), width=2)
        elif points[0] == 3:
            start_ray = [(0, H/2) , (1, 0)]
            ray = Ray((0, H/2) , (1, 0), width=2)
        gameControler.objects.append(ray)

        if points[-1] == 1:
            finish = FinishObject(W-75, 0, 75, 10, I=1, angle=-1)
        if points[-1] == 2:
            finish = FinishObject(W-10, H/2-75/2, 10, 75, I=1, angle=-1)
        gameControler.objects.append(finish)
        startObjectLen = len(gameControler.objects)

    else:
        for i in walls:
            if isinstance(i, Ray):
                ray = Ray(start_ray[0], start_ray[1], width=2)
                gameControler.objects.append(ray)
            else:
                gameControler.objects.append(i)    
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
        text_rect = text.get_rect(topleft=(W-300+10, H-300+10))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        text = font.render("r - заново", True, (255, 255, 255))  # Белый цвет текста
        text_rect = text.get_rect(topleft=(W-300+10, H-300+30))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        text = font.render("Мышью раставлять", True, (255, 255, 255))  # Белый цвет текста
        text_rect = text.get_rect(topleft=(W-300+10, H-300+55))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        text = font.render("зеркала", True, (255, 255, 255))  # Белый цвет текста
        text_rect = text.get_rect(topleft=(W-300+10, H-300+75))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        text = font.render("Зеркала можно", True, (255, 255, 255))  # Белый цвет текста
        text_rect = text.get_rect(topleft=(W-300+10, H-300+100))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        text = font.render("двигать за края", True, (255, 255, 255))  # Белый цвет текста
        text_rect = text.get_rect(topleft=(W-300+10, H-300+125))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        text = font.render("del - удалить зеркало", True, (255, 255, 255))  # Белый цвет текста
        text_rect = text.get_rect(topleft=(W-300+10, H-300+150))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        exit_button.draw(screen)
        
        pygame.display.update()



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if exit_button.handle_event(event):
                optic_choice.start(screen)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    m = []
                    objects = []
                    for i in gameControler.objects:
                        if isinstance(i, Mirror):
                            m.append(i)
                        else:
                            objects.append(i)
                    return start(screen, mirrors=m, walls=objects, firstLaunch=False, start_ray=start_ray)

        gameControler.calculate()
        if gameControler.win:
            return
        
        gameControler.draw()

        text = font.render("s - старт", True, (255, 255, 255))  # Белый цвет текста
        text_rect = text.get_rect(topleft=(W-300+10, H-300+10))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        text = font.render("r - заново", True, (255, 255, 255))  # Белый цвет текста
        text_rect = text.get_rect(topleft=(W-300+10, H-300+30))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        text = font.render("Мышью раставлять", True, (255, 255, 255))  # Белый цвет текста
        text_rect = text.get_rect(topleft=(W-300+10, H-300+55))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        text = font.render("зеркала", True, (255, 255, 255))  # Белый цвет текста
        text_rect = text.get_rect(topleft=(W-300+10, H-300+75))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        text = font.render("Зеркала можно", True, (255, 255, 255))  # Белый цвет текста
        text_rect = text.get_rect(topleft=(W-300+10, H-300+100))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        text = font.render("двигать за края", True, (255, 255, 255))  # Белый цвет текста
        text_rect = text.get_rect(topleft=(W-300+10, H-300+125))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        text = font.render("del - удалить зеркало", True, (255, 255, 255))  # Белый цвет текста
        text_rect = text.get_rect(topleft=(W-300+10, H-300+150))  # Центрируем текст в окне
        screen.blit(text, text_rect) # Отображаем текст на экране
        exit_button.draw(screen)

        pygame.display.update()
