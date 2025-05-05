import pygame
import sys

# === Настройка ===
SCREEN_WIDTH, SCREEN_HEIGHT = 720, 600
FPS = 60


# === Цвета ===
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Повелитель оптики')

clock = pygame.time.Clock()

# === Загрузка ресурсов ===

background_img = pygame.image.load("assets/icon.ico").convert()
pygame.display.set_icon(background_img)

background_img = pygame.image.load("assets/background.png").convert()
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

finish_img = pygame.image.load("assets/finish.png").convert()
finish_img = pygame.transform.scale(finish_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

button_img = pygame.image.load("assets/pixel_button.png").convert_alpha()
button_img = pygame.transform.scale(button_img, (300, 60))

font = pygame.font.Font("assets/PressStart2P-vaV7.ttf", 18)

num1_img = pygame.image.load("assets/num1.png").convert()
num1_img = pygame.transform.scale(num1_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

num2_img = pygame.image.load("assets/num2.png").convert()
num2_img = pygame.transform.scale(num2_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

upr_img = pygame.image.load("assets/upr.png").convert()
upr_img = pygame.transform.scale(upr_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

upr2_img = pygame.image.load("assets/upr_2.png").convert()
upr2_img = pygame.transform.scale(upr2_img, (SCREEN_WIDTH, SCREEN_HEIGHT))


oneStar = pygame.image.load('assets/zv_1.png').convert()
oneStar = pygame.transform.scale(oneStar, (SCREEN_WIDTH, SCREEN_HEIGHT))

twoStar = pygame.image.load('assets/zv_2.png').convert()
twoStar = pygame.transform.scale(twoStar, (SCREEN_WIDTH, SCREEN_HEIGHT))

threeStar = pygame.image.load('assets/zv_3.png').convert()
threeStar = pygame.transform.scale(threeStar, (SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_text(text, font, color, surface, x, y, center=True):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)
    return text_rect




def main_menu(start_game_callback, level2_callback):
    clicked_button = None  # None, 'level1', or 'level2'

    while True:
        screen.blit(background_img, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        # --- Кнопка Уровень 1 ---
        button1_rect = button_img.get_rect(center=(SCREEN_WIDTH // 2, 250))
        hovered1 = button1_rect.collidepoint(mouse_pos)
        y_offset1 = 3 if clicked_button == 'level1' else 0
        screen.blit(button_img, button1_rect.move(0, y_offset1))
        draw_text(" 1 уровень", font, RED if hovered1 else WHITE, screen, SCREEN_WIDTH // 2, 250 + y_offset1)

        # --- Кнопка Уровень 2 ---
        button2_rect = button_img.get_rect(center=(SCREEN_WIDTH // 2, 350))
        hovered2 = button2_rect.collidepoint(mouse_pos)
        y_offset2 = 3 if clicked_button == 'level2' else 0
        screen.blit(button_img, button2_rect.move(0, y_offset2))
        draw_text(" 2 уровень", font, RED if hovered2 else WHITE, screen, SCREEN_WIDTH // 2, 350 + y_offset2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if hovered1:
                    clicked_button = 'level1'
                elif hovered2:
                    clicked_button = 'level2'

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if clicked_button == 'level1' and hovered1:
                    start_game_callback(screen)
                elif clicked_button == 'level2' and hovered2:
                    level2_callback(screen)
                clicked_button = None

        pygame.display.flip()
        clock.tick(FPS)

def finish_menu():
    while True:
        screen.blit(finish_img, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def result(res, next_slide):
    clicked_button = None  # None, 'level1', or 'level2'

    while True:

        if res == 1:
            screen.blit(oneStar, (0, 0))
        elif res == 2:
            screen.blit(twoStar, (0, 0))
        elif res == 3:
            screen.blit(threeStar, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        # --- Кнопка рестарт ---
        button1_rect = button_img.get_rect(center=(SCREEN_WIDTH // 2, 350))
        hovered1 = button1_rect.collidepoint(mouse_pos)
        y_offset1 = 3 if clicked_button == 'level1' else 0
        screen.blit(button_img, button1_rect.move(0, y_offset1))
        draw_text(" Заново", font, RED if hovered1 else WHITE, screen, SCREEN_WIDTH // 2, 350 + y_offset1)

        # --- Кнопка дальше ---
        button2_rect = button_img.get_rect(center=(SCREEN_WIDTH // 2, 450))
        hovered2 = button2_rect.collidepoint(mouse_pos)
        y_offset2 = 3 if clicked_button == 'level2' else 0
        screen.blit(button_img, button2_rect.move(0, y_offset2))
        draw_text(" Дальше", font, RED if hovered2 else WHITE, screen, SCREEN_WIDTH // 2, 450 + y_offset2)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if hovered1:
                    clicked_button = 'level1'
                elif hovered2:
                    clicked_button = 'level2'

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if clicked_button == 'level1' and hovered1 and next_slide == 2:
                    start_level_one(screen)
                elif clicked_button == 'level2' and hovered2 and next_slide == 2:
                    start_level_two(screen)

                if clicked_button == 'level1' and hovered1 and next_slide == 3:
                    start_level_two(screen)
                elif clicked_button == 'level2' and hovered2 and next_slide == 3:
                    finish_menu()
                clicked_button = None

        pygame.display.flip()
        clock.tick(FPS)


# === Пример функции запуска 1 уровня ===
def start_level_one(screen):
    next_slide = 2 #след уровень 2й
    cnt = 0
    while True:
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and cnt == 0:
                screen.blit(upr_img, (0, 0))
                pygame.display.update()
                cnt += 1
            
            elif event.type == pygame.MOUSEBUTTONDOWN and cnt == 1:
                screen.blit(num1_img, (0, 0))
                pygame.display.update()
                cnt += 1

            elif event.type == pygame.MOUSEBUTTONDOWN and cnt == 2:
                import level1
                rez = level1.start(screen)
                result(rez, next_slide)
        
    

                


# === 2 уровень ===
def start_level_two(screen):
    next_slide = 3 #след уровень 3й
    cnt = 0
    
    while True:
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and cnt == 0:
                screen.blit(upr2_img, (0, 0))
                pygame.display.update()
                cnt += 1
            
            elif event.type == pygame.MOUSEBUTTONDOWN and cnt == 1:
                screen.blit(num2_img, (0, 0))
                pygame.display.update()
                cnt += 1

            elif event.type == pygame.MOUSEBUTTONDOWN and cnt == 2:
                import level2
                rez = level2.start(screen)
                result(rez, next_slide)

    


# === Запуск меню ===
if __name__ == "__main__":
    main_menu(start_level_one, start_level_two)