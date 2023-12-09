from pathlib import Path
import pygame
from constants import TILE_COLORS,TILE_NUMBERS,TILE_WIDTH,TILE_HEIGHT
from pygame.sprite import Sprite

#Tile class, each tile has a number and a color from 1-13 and red,blue,yellow,black respectively
class Tile(Sprite):
    def __init__(self, number, color):
        super().__init__()
        if color not in TILE_COLORS or number not in TILE_NUMBERS:
            raise ValueError("Invalid color")
        else:
            self.number = int(number)
            self.color = color
            self.image = pygame.image.load(f"images/{self.number}{self.color}.png")
            self.image = pygame.transform.scale(self.image,(TILE_WIDTH,TILE_HEIGHT))
            self.rect = self.image.get_rect()
            self.selected = False

    def __str__(self):
        return f"{self.color}{self.number}"

    def sameNumber(self, other):
        return self.number == other.number

    def sameColor(self, other):
        return self.color == other.color

    def toggle_selected(self):
        self.selected = not self.selected