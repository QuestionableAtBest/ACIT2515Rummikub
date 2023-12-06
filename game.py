from constants import WIDTH, HEIGHT
import pygame
from screens.game import GameScreen
from screens.start import StartScreen

def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    #Start screen, user enters their name and presses play button
    screen = StartScreen(window)
    screen.run()
    
    #Clear screen then play game
    window.fill((255,255,255))
    screen = GameScreen(window)
    screen.run() 
    
    #Game finished, clear screen then show end screen
    window.fill((255,255,255))

import os
if __name__ == "__main__":
    
    main()
