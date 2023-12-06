class Rack:
    def __init__(self):
        self.tiles = []

    def add_tile(self, tile):
        self.tiles.append(tile)

    def remove_tile(self, tile):
        if tile in self.tiles:
            self.tiles.remove(tile)

    def __len__(self):
        return len(self.tiles)
    
    def sort_by_numbers(self):
        self.tiles.sort(key=lambda tile: tile.number)

    def sort_by_colors(self):
        self.tiles.sort(key=lambda tile: tile.color)