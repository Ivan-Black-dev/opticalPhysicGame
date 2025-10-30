import pygame
from generator import Generator
from random_level import start
import pygame

pygame.init()

# Получаем информацию о текущем дисплее
display_info = pygame.display.Info()
width, height = display_info.current_w, display_info.current_h

BACKGROUND_COLOR = (30, 30, 30)
POINT_COLOR = (255, 100, 100)
LINE_COLOR = (200, 200, 200)

# Создаем окно в полноэкранном режиме с текущим разрешением экрана
screen = pygame.display.set_mode((width, height))

print(start(screen))

# gen = Generator(width, height, level=5)
# walls= gen.generate_walls()




# # Главный цикл программы
# running = True
# while running:
#     screen.fill(BACKGROUND_COLOR)
#     for wall in walls:
#         pygame.draw.rect(screen, [255, 255, 255], wall, width=0)

    

#     # Обработка событий
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     pygame.display.flip()

# pygame.quit()
# sys.exit()

