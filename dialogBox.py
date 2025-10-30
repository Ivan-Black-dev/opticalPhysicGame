import pygame

class DialogBox:
    def __init__(self, rect, font, text=''):
        self.rect = pygame.Rect(rect)
        self.font = font
        self.text = text
        self.active = False
        self.input_text = ''
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive

    def handle_event(self, event):
        if not self.active:
            return None
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                entered_text = self.input_text
                self.input_text = ''
                self.active = False
                return entered_text
            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            else:
                self.input_text += event.unicode
        return None

    def draw(self, surface):
        # фон диалога
        pygame.draw.rect(surface, (240, 240, 240), self.rect)
        pygame.draw.rect(surface, self.color, self.rect, 2)

        # текст приглашения и вводимый текст
        prompt_surf = self.font.render(self.text, True, (0, 0, 0))
        surface.blit(prompt_surf, (self.rect.x + 5, self.rect.y + 5))

        input_surf = self.font.render(self.input_text, True, (0, 0, 0))
        surface.blit(input_surf, (self.rect.x + 5, self.rect.y + 25))

    def activate(self, prompt):
        self.text = prompt
        self.active = True
        self.input_text = ''
        self.color = self.color_active

    def deactivate(self):
        self.active = False
        self.color = self.color_inactive