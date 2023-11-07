import random
import pygame

from .base import BaseScreen


class GameScreen(BaseScreen):
    def __init__(self, window, persistent=None):
        super().__init__(window, persistent)

    def update(self):
        pass

    def manage_event(self, event):
        super().manage_event(event)
        pass

    def draw(self):
        pass