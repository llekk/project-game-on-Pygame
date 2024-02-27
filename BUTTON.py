import pygame


class Button:
    def __init__(self, x, y, width, height, text, imape_path, hover_im, sound=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.image = pygame.image.load(imape_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image
        if hover_im:
            self.hover_image = pygame.image.load(hover_im)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        if sound:
            self.soundd = pygame.mixer.Sound(sound)
        self.is_hovered = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)
        font = pygame.font.Font(None, 36)
        text_srfc = font.render(self.text, True, (255, 255, 255))
        text_rect = text_srfc.get_rect(center=self.rect.center)
        screen.blit(text_srfc, text_rect)

    def check_hover(self, mous_pos):
        self.is_hovered = self.rect.collidepoint(mous_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.soundd:
                self.soundd.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
