from .rack import Rack

class Player:
    def __init__(self, name):
        self.name = name
        self.rack = Rack()
        #Probably add database scores to this later

    def add_tile_to_rack(self, tile):
        self.rack.add_tile(tile)

    def get_score(self):
        score = 0
        for tile in self.rack.tiles:
            score += tile.number
    
    def get_tiles(self):
        return self.rack.tiles