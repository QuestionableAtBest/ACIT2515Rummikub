from .rack import Rack

class Player:
    def __init__(self, name):
        self.name = name
        self.rack = Rack()
        #This is used to determine if the player has made a move yet, in Rummikub, you don't have to draw a tile after you made a valid move
        self.made_move = False
        
        #Probably add database scores to this later

    def add_tile_to_rack(self, tile):
        self.rack.add_tile(tile)

    def get_score(self):
        score = 0
        for tile in self.rack.tiles:
            score += tile.number
    
    def get_tiles(self):
        return self.rack.tiles