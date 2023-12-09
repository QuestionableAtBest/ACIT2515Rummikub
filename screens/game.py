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
            print("Clicked at:", event.pos)
            self.player.rack.manage_click(event)
        # If keyboard pressed
        if event.type == pygame.KEYDOWN:
            # and is p (player has passed their turn)
            if event.key == pygame.K_p:
                # Player has made a valid move
                if self.player.made_move:
                    self.player.made_move = False
                else:
                    # Player passed without making a valid move, draw a tile
                    self.player.add_tile_to_rack(self.tile_bag.get_tile())
                    #Check if drawing the tile resulted in 26 tiles in the rack or 0 tiles in the bag, if so then game over (MY RULE NOT OFFICIAL RUMMIKUB)
                    from .game_over import GameOverScreen
                    if len(self.player.rack) >= 26 or len(self.tile_bag) == 0:
                        self.persistent["win"] = False
                        self.persistent["score"] = 0
                        self.next_screen = GameOverScreen(self.window, self.persistent)
                # After player passes, CPU's Turn (Right now it is the dumbest I can think of, random tile from its rack, 
                # random rack on the table. Check valid move, if not then just draw a tile)
                # Also need to find a way to alternate, so that player cant press anything during CPU turn.
                # self.cpu_turn()

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
