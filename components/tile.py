from pathlib import Path
from constants import TILE_COLORS, TILE_NUMBERS
class Tile:
    def __init__(self, color, number):
        if color not in TILE_COLORS or number not in TILE_NUMBERS:
            raise ValueError("Invalid color")
        else:
            self.color = color
            self.number = number
            self.path_to_image = self.get_image_path()
    
    def __str__(self):
        return f"{self.color}{self.number}"
    
    def sameNumber(self,other):
        return self.number == other.number

    def sameColor(self,other):
        return self.color == other.color
    
    def get_image_path(self):
        return Path(f"../images/{self.color}{self.number}.png")
    
    
    