from constants import WIDTH, HEIGHT
import pygame
from screens import GameScreen


def main():
    pygame.init()
    pygame.key.set_repeat(400, 400)
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    screen = GameScreen(window)
    screen.run()


if __name__ == "__main__":
    main()
