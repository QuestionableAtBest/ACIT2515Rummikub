import pygame
from components import Player, TileBag, Rack, Table
from .base import BaseScreen
from constants import RACK_WIDTH, RACK_HEIGHT,TILE_SPACING, TILE_WIDTH, TILE_HEIGHT, RACK_START_X, RACK_START_Y

class GameScreen(BaseScreen):
    def __init__(self, window, persistent=None):
        super().__init__(window)
        # persistent from start screen to get name
        self.persistent = persistent

        #assign player and cpu racks
        self.player = Player(persistent["name"])
        self.cpu = Player("CPU")

        #initialize bag and tabletop
        self.tile_bag = TileBag()
        self.tabletop = Table()
        # Draw 13 tiles for each player to start
        for i in range(14):
            self.player.add_tile_to_rack(self.tile_bag.get_tile())
            self.cpu.add_tile_to_rack(self.tile_bag.get_tile())


    def update(self):
        self.player.rack.update()


    def manage_event(self, event):
        super().manage_event(event)
        # If left click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Handle tile selection
            for tile in self.player.get_tiles():
                if tile.rect.collidepoint(event.pos):
                    tile.toggle_selection()
            
    def draw(self):
        self.window.fill((104, 95, 140)) 
        rack_surface = pygame.Surface((RACK_WIDTH, RACK_HEIGHT))
        rack_surface.fill((0, 0, 0))
        self.window.blit(rack_surface, (RACK_START_X, RACK_START_Y))
        # Draw player's rack
        y = RACK_START_Y
        x = RACK_START_X
        for i, tile in enumerate(self.player.get_tiles()):
            self.window.blit(tile.image, (x, y))
            x = RACK_START_X + i * ((TILE_WIDTH + TILE_SPACING)/2)
            if x > RACK_WIDTH + TILE_WIDTH:
                x = RACK_START_X + (i-13) * ((TILE_WIDTH + TILE_SPACING)/2)
                y = RACK_START_Y + TILE_HEIGHT
