import pygame

def start(screen):
    clock = pygame.time.Clock()

    images_paths = [
        "assets/o_t_1.png",
        "assets/o_t_2.png",
        "assets/o_t_3.png"
    ]

    images = [pygame.transform.smoothscale(pygame.image.load(p).convert_alpha(), screen.get_size()) for p in images_paths]

    current = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                current += 1
                if current >= len(images):
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                current += 1
                if current >= len(images):
                    running = False
        
        if current < len(images):
            screen.blit(images[current], (0, 0))
            pygame.display.flip()

        clock.tick(60)
