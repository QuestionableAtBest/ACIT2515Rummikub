import pygame
from .base import BaseScreen
from .start import StartScreen
from constants import WIDTH, HEIGHT
# Game over screen
class GameOverScreen(BaseScreen):
    def __init__(self, window, persistent=None):
        super().__init__(window, persistent)
        self.persistent = persistent
        # Get win and score from persistent, win is a boolean (true if win, false if lose)
        self.win = persistent["win"]
        self.score = persistent["score"]

        self.font = pygame.font.SysFont("Arial", 36)
        self.buttons = pygame.sprite.Group()

        # Create retry button
        retry_button_rect = pygame.Rect(WIDTH/4, HEIGHT/2, WIDTH*0.2, HEIGHT*0.1)
        retry_button_sprite = pygame.sprite.Sprite()
        retry_button_sprite.image = pygame.Surface((150, 50))
        retry_button_sprite.image.fill((0, 255, 0))
        retry_button_text = self.font.render("Retry", True, (0, 0, 0))
        retry_button_sprite.image.blit(retry_button_text, (40, 10))
        #Add retry to sprite group
        retry_button_sprite.rect = retry_button_rect
        self.buttons.add(retry_button_sprite)

        # Create quit button
        quit_button_rect = pygame.Rect(WIDTH/2, HEIGHT/2, WIDTH*0.2, HEIGHT*0.1)
        quit_button_sprite = pygame.sprite.Sprite()
        quit_button_sprite.image = pygame.Surface((150, 50))
        quit_button_sprite.image.fill((255, 0, 0))
        quit_button_text = self.font.render("Quit", True, (0, 0, 0))
        quit_button_sprite.image.blit(quit_button_text, (45, 10))
        #Add quit to sprite group
        quit_button_sprite.rect = quit_button_rect
        self.buttons.add(quit_button_sprite)

    def manage_event(self, event):
        super().manage_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button in self.buttons:
                if button.rect.collidepoint(event.pos):
                    #Retry pressed
                    if button == self.buttons.sprites()[0]:
                        self.next_screen = StartScreen(self.window)
                    #Quit pressed
                    elif button == self.buttons.sprites()[1]:
                        pygame.quit()
                        quit()

    def draw(self):
        self.window.fill((255, 255, 255))
        # Display message and score
        if self.win:
            message = "CONGRATULATIONS! YOU WON!"
        else:
            message = "OH NO YOU LOST"
        score_message = f"SCORE: {self.score}"
        message_text = self.font.render(message, True, (0, 0, 0))
        score_text = self.font.render(score_message, True, (0, 0, 0))
        self.window.blit(message_text, (WIDTH/4, HEIGHT*0.3))
        self.window.blit(score_text, (WIDTH/4, HEIGHT*0.35))

        # Draw buttons
        self.buttons.draw(self.window)