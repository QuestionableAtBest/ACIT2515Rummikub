import pygame
from components import *
from .base import BaseScreen
from constants import RACK_WIDTH, RACK_HEIGHT, RACK_START_X, RACK_START_Y, TILE_SPACING

class GameScreen(BaseScreen):
    def __init__(self, window, persistent=None):
        super().__init__(window, persistent)
        self.player = Player("TEMP NAME")
        self.cpu = Player("CPU")
        self.bag = TileBag()

        # Draw 14 tiles to start
        for i in range(14):
            self.player.add_tile_to_rack(self.bag.draw_tile())
            self.cpu.add_tile_to_rack(self.bag.draw_tile())


    def update(self):
        pass

    def manage_event(self, event):
        super().manage_event(event)
        pass

    def draw(self):
        self.draw_rack()
        self.draw_tiles_on_rack()

    def draw_rack(self):
        self.rack_sprite = pygame.Surface((RACK_WIDTH, RACK_HEIGHT))
        self.rack_sprite.fill((0, 0, 0))
        self.window.blit(self.rack_sprite, (RACK_START_X, RACK_START_Y))

    def draw_tiles_on_rack(self):
        for i, tile in enumerate(self.player.get_tiles()):
            x = RACK_START_X + i * (RACK_WIDTH + TILE_SPACING)
            y = RACK_START_Y
            self.window.blit(tile.load_sprite(), (x, y))
