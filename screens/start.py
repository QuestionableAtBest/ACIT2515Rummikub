import pygame
from components.textbox import TextBox
from components.editable_group import EditableGroup
from .base import BaseScreen

class StartScreen(BaseScreen):
    def __init__(self, window):
        super().__init__(window)
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 48)

        # Create a sprite group
        self.group = pygame.sprite.Group()

        # Rummikub text
        text_surface = font.render("Rummikub", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(window.get_width() // 2, 200))
        text_sprite = pygame.sprite.Sprite()
        text_sprite.image = text_surface
        text_sprite.rect = text_rect
        self.group.add(text_sprite)

        # Text box for name
        self.text_box_group = EditableGroup()
        text_box = TextBox(
            dimensions=(300, 40),
            text="Name",
            id="player_name",
            bgcolor=(255, 120, 120),
            color=(0, 0, 0),
            font_size=24,
        )
        # Border
        pygame.draw.rect(text_box.image, (255, 0, 255), text_box.image.get_rect(), 2)
        text_box.rect.topleft = (window.get_width() // 2 - text_box.rect.width // 2, 250)
        self.text_box_group.add(text_box)

        # Play button
        play_button_rect = pygame.Rect((window.get_width() - 100) // 2, 350, 100, 40)

        play_button_sprite = pygame.sprite.Sprite()
        play_button_sprite.image = pygame.Surface((100, 40)) 
        play_button_sprite.image.fill((0, 0, 255))

        # Play text
        play_button_text_surface = font.render("PLAY", True, (255, 0, 0))  # Red text
        play_button_text_rect = play_button_text_surface.get_rect(center=(50, 20))
        play_button_sprite.image.blit(play_button_text_surface, play_button_text_rect)

        play_button_sprite.rect = play_button_rect
        self.group.add(play_button_sprite)

    def manage_event(self, event):
        super().manage_event(event)
        # If left click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # on text box (In editable group)
            if self.text_box_group.sprites()[0].rect.collidepoint(event.pos):
                self.text_box_group.manage_click(event)
            # on play button (Second sprite that was added to the group)
            if self.group.sprites()[1].rect.collidepoint(event.pos):
                # FIX HERE: Somehow make it so player name gets passed into GameScreen
                print(self.text_box_group.sprites()[0].text)
                self.running = False
        if event.type == pygame.KEYDOWN:
            self.text_box_group.manage_key(event)

    
    def draw(self):
        self.window.fill((255, 255, 255))
        self.group.draw(self.window)
        self.text_box_group.draw(self.window)
