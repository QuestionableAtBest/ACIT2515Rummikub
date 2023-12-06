from random import shuffle
from .tile import Tile
from constants import TILE_COLORS, TILE_NUMBERS

class TileBag:
    def __init__(self):
        self.tiles = []
        test_tile = Tile("1","r")
        self.tiles.append(test_tile)
        self.fill_tiles()
        shuffle(self.tiles)

    # Fill tile bag with all tiles for game
    def fill_tiles(self):
        for color in TILE_COLORS:
            for number in TILE_NUMBERS:
                self.tiles.append(Tile(number, color))

    # Draw a tile from the bag
    def draw_tile(self):
        if self.tiles:
            return self.tiles.pop()
        else:
            print("The bag is empty.")
            return None

    def is_empty(self):
        return self.tiles.length == 0
