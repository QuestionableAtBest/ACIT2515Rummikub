import random
import pygame
from components.tile import Tile
from components.rack import Rack
from .base import BaseScreen
import constants

class GameScreen(BaseScreen):
    def __init__(self, window, persistent=None):
        super().__init__(window, persistent)
        self.player_rack = Rack("Player")
        self.load_rack_sprites()

    def update(self):
        pass

    def manage_event(self, event):
        super().manage_event(event)
        pass


    def load_rack_sprites(self):
        # Load rack sprites (two black rectangles)
        self.rack_sprite = pygame.Surface((constants.RACK_WIDTH, constants.RACK_HEIGHT))
        self.rack_sprite.fill((0, 0, 0))

    def draw(self):
        self.draw_rack()
        self.draw_tiles_on_rack()

    def draw_rack(self):
        # Draw the player's rack using the rack sprites
        for i in range(constants.RACK_SIZE):
            x = constants.RACK_START_X + i * (constants.RACK_WIDTH + constants.RACK_SPACING)
            y = constants.RACK_START_Y
            self.window.blit(self.rack_sprite, (x, y))

    def draw_tiles_on_rack(self):
        # Draw the tiles on the player's rack
        for i, tile in enumerate(self.player_rack.tiles):
            x = constants.RACK_START_X + i * (constants.RACK_WIDTH  + constants.RACK_SPACING)
            y = constants.RACK_START_Y
            self.window.blit(tile.sprite.image, (x, y))
