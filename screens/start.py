import pygame
from components.textbox import TextBox
from components.editable_group import EditableGroup
from .base import BaseScreen
from .game import GameScreen

class StartScreen(BaseScreen):
    def __init__(self, window):
        super().__init__(window)
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 48)
        self.group = pygame.sprite.Group()

        # Rummikub text with my name and student number
        text_surface = font.render("Rummikub, Harry Zhou A01235123", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(window.get_width() // 2, window.get_width()*0.2))
        text_sprite = pygame.sprite.Sprite()
        text_sprite.image = text_surface
        text_sprite.rect = text_rect
        self.group.add(text_sprite)

        # Text box for player to enter their name
        self.text_box_group = EditableGroup()
        text_box = TextBox(
            dimensions=(300, 40),
            text="Name",
            id="player_name",
            bgcolor=(255, 120, 120),
            color=(0, 0, 0),
            font_size=24,
        )
        # Border for text box
        pygame.draw.rect(text_box.image, (255, 0, 255), text_box.image.get_rect(), 2)
        text_box.rect.topleft = (window.get_width() // 2 - text_box.rect.width // 2, 250)
        self.text_box_group.add(text_box)

        # Play button
        play_button_rect = pygame.Rect((window.get_width() - 100) // 2, 350, 100, 40)
        play_button_sprite = pygame.sprite.Sprite()
        play_button_sprite.image = pygame.Surface((100, 40)) 
        play_button_sprite.image.fill((0, 0, 255))
        # Play text
        play_button_text_surface = font.render("PLAY", True, (255, 0, 0))
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
                # handle text box click (select the box)
                self.text_box_group.manage_click(event)
            # on play button (Second sprite that was added to the group and player has entered a name)
            if self.group.sprites()[1].rect.collidepoint(event.pos) and self.text_box_group.sprites()[0].text != "Name":
                # Go to game screen, with player's entered name
                self.persistent["name"] = self.text_box_group.sprites()[0].text
                print(self.persistent["name"])
                self.next_screen = GameScreen(self.window, self.persistent)

        if event.type == pygame.KEYDOWN:
            # Handle text box key presses (In editable group)
            self.text_box_group.manage_key(event)

    
    def draw(self):
        self.window.fill((255, 255, 255))
        self.group.draw(self.window)
        self.text_box_group.draw(self.window)
