from screens import *
from components.rack import Rack
import pygame
from constants import WIDTH, HEIGHT

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))


#All these screens seem to work fine seperately, but unfortunately I can't get them to work together, self.next_screen does not like me
screen = StartScreen(window)
screen.run()

# screen = GameScreen(window,{"name": "Player 1"})
# screen.run()

# screen = GameOverScreen(window, {"name": "Player 1","win": False,"score": 0})
# screen.run()
