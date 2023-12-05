from rack import Rack
from tile import Tile

class Player:
    def __init__(self, name):
        self.name = name
        self.rack = Rack(name)

    def add_tile_to_rack(self, tile):
        self.rack.add_tile(tile)

    def play_tile(self, tile):
        if tile in self.rack.tiles:
            self.rack.remove_tile(tile)
            print(f"{self.name} played {tile}.")
            return tile
        else:
            print(f"{self.name} doesn't have {tile} in their rack.")
            return None

    def display_rack(self):
        print(f"{self.name}'s Rack:")
        for tile in self.rack.tiles:
            print(tile, end=" ")
        print()
