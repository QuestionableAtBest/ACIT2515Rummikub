from pygame.sprite import Sprite
import pygame
#Online answer for sorting sprites
from operator import attrgetter

class Rack(Sprite):
    def __init__(self):
        super().__init__()
        # A rack is a group of tile sprites
        self.tiles = pygame.sprite.Group()

    def add_tile(self, tile):
        self.tiles.add(tile)

    def remove_tile(self, tile):
        self.tiles.remove(tile)

    def update(self):
        #Always sort rack by color
        self.sort_by_color()
        self.tiles.update()

    def draw(self, surface):
        # Draw the tiles on the rack
        self.tiles.draw(surface)

    def __len__(self):
        return len(self.tiles)
    
    def sort_by_number(self):
        self.tiles = pygame.sprite.Group(sorted(self.tiles, key=attrgetter('number')))

    def sort_by_color(self):
        self.tiles = pygame.sprite.Group(sorted(self.tiles, key=attrgetter('color')))

    #Pulled from the editable group class. Still is not working
    def manage_click(self, event):
        for s in self.tiles:
            if s.rect.collidepoint(event.pos):
                s.toggle_selected()

    def valid_set(self):
        #Basic check, all valid racks must have at least 4 tiles
        if len(self) < 4:
            return False
        check = self.tiles.sprites()[0]
        cur_colors = []
        #Sets are only valid if all the numbers on the rack are the same
        for tile in self.tiles[1:]:
            if not tile.sameNumber(check):
                return False
            cur_colors.append(tile.color)
        #Sets are only valid if all the colors on the rack are different    
        return len(set(cur_colors)) != len(cur_colors)

    def valid_run(self):
        #Basic check, all valid racks must have at least 4 tiles
        if len(self) < 4:
            return False
        #Sort the tiles by number
        self.sort_by_number()
        prev = self.tiles.sprites()[0]
        #Runs are only valid if all the colors on the rack are the same and the numbers are consecutive
        for tile in self.tiles[1:]:
            if not tile.sameColor(prev) or tile.number != prev.number + 1:
                return False
            prev = tile