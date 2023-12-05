from pathlib import Path
import constants
import pygame

class Tile:
    def __init__(self, color, number):
        if color not in constants.TILE_COLORS or number not in constants.TILE_NUMBERS:
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
    
    def load_sprite(self):
        image = pygame.image.load(str(self.image_path))
        return pygame.sprite.Sprite(image)