import color
from ray import Ray
from finishObject import FinishObject
from polarizer import Polarizer
from mirror import Mirror
from wall import Wall
import pygame
import sys
import time


class GameControler:
    
    def __init__(this, screen):
        this.screen = screen
        this.BACKROUND_COLOR = color.BLACK
        this.objects = []
        this.win = False

    def draw(this):
        this.screen.fill(this.BACKROUND_COLOR)
        for i in this.objects:
            if isinstance(i, Ray):
                for point in i.points:
                    try:
                        pygame.draw.circle(this.screen, i.color, point, i.width)
                    except:
                        print(point)
            elif isinstance(i, Polarizer):
                pygame.draw.circle(this.screen, i.color, (i.x, i.y), i.width)
                font = pygame.font.Font(None, 20) 
                polText = font.render(f'{i.angle}', True, color.RED)
                this.screen.blit(polText, (i.x+(i.width/2)-20, i.y+(i.width/2)-20))
            elif isinstance(i, Mirror):
                pygame.draw.circle(this.screen, i.color, (i.x1, i.y1), 10)
                pygame.draw.circle(this.screen, i.color, (i.x2, i.y2), 10)
                pygame.draw.line(this.screen, i.color, (i.x1, i.y1), (i.x2, i.y2), 3)
            elif isinstance(i, Wall):
                pygame.draw.rect(this.screen, i.color, (i.x, i.y, i.w, i.h))
            elif isinstance(i, FinishObject):
                pygame.draw.rect(this.screen, i.color, (i.x, i.y, i.width, i.height))

    def calculate(this):
        for i in this.objects:
            if isinstance(i, Ray):
                if not i.finish:
                    for j in this.objects:
                        if not isinstance(j, Ray):
                            rez = i.collision(j, this.screen)
                            if rez == 1:
                                this.win = True
                    i.tick()