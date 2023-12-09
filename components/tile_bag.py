from random import shuffle
from .tile import Tile
from constants import TILE_COLORS, TILE_NUMBERS

# Tilebag holds all the tiles in the game for players to draw from (I have taken the liberty to remove the joker tile because thats too much work)
class TileBag:
    def __init__(self):
        tiles = []
        for color in TILE_COLORS:
            for number in TILE_NUMBERS:
                tile = Tile(number, color)
                tiles.append(tile)
        shuffle(tiles)
        self.tiles = tiles

    def get_tile(self):
        if self.tiles:
            return self.tiles.pop()
        else:
            return None
        
    def __len__(self):
        return len(self.tiles)