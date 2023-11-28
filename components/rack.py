class Rack:
    def __init__(self, player_name):
        self.player_name = player_name
        self.tiles = []

    def add_tile(self, tile):
        self.tiles.append(tile)

    def remove_tile(self, tile):
        if tile in self.tiles:
            self.tiles.remove(tile)
        else:
            print(f"{tile} not found in {self.player_name}'s rack.")

    def display_rack(self):
        print(f"{self.player_name}'s Rack:")
        for tile in self.tiles:
            print(tile, end=" ")

    def __len__(self):
        return len(self.tiles)
    
    def sort_by_numbers(self):
        self.tiles.sort(key=lambda tile: tile.number)

    def sort_by_colors(self):
        self.tiles.sort(key=lambda tile: tile.color)