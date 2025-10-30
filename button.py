import pygame

class Button:
    def __init__(self, rect, text, font, inactive_color, active_color):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.active = False

    def draw(self, surface):
        color = self.active_color if self.active else self.inactive_color
        pygame.draw.rect(surface, color, self.rect)
        text_surf = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False