from pathlib import Path
from constants import TILE_COLORS, TILE_NUMBERS
import pygame

class Tile:
    def __init__(self, number, color):
        if color not in TILE_COLORS or number not in TILE_NUMBERS:
            raise ValueError("Invalid color")
        else:
            self.number = int(number)
            self.color = color 
    
    def __str__(self):
        return f"{self.color}{self.number}"
    
    def sameNumber(self,other):
        return self.number == other.number

    def sameColor(self,other):
        return self.color == other.color
    
    def load_sprite(self):
        current_directory = str(Path.cwd().parent).replace("\\","/")
        path = current_directory + f"/images/{self.number}{self.color}.png"
        image = pygame.image.load(path)
        return pygame.sprite.Sprite(image)