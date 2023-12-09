from constants import WIDTH, HEIGHT
import pygame
from screens.start import StartScreen
def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    #Start screen, user enters their name and presses play button
    screen = StartScreen(window)
    screen.run()

if __name__ == "__main__":
    main()
