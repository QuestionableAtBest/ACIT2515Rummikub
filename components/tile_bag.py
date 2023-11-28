from random import shuffle
from tile import Tile
from constants import TILE_COLORS, TILE_NUMBERS
class TileBag:
    def __init__(self):
        self.tiles = []
        self.initialize_tiles()
        self.tiles = shuffle(self.tiles)

    def initialize_tiles(self):
        for color in TILE_COLORS:
            for number in TILE_NUMBERS:
                self.tiles.append(Tile(color, number))

    def draw_tile(self):
        if self.tiles:
            return self.tiles.pop()
        else:
            print("The bag is empty.")
            return None

    def is_empty(self):
        return self.tiles.length == 0
