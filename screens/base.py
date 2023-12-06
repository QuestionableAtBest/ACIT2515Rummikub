import pygame


class BaseScreen:
    def __init__(self, window, persistent=None):
        if persistent is None:
            self.persistent = {}
        else:
            self.persistent = persistent

        self.window = window
        self.running = False

    def run(self):
        clock = pygame.time.Clock()
        self.running = True
        while self.running:
            clock.tick(60)
            self.update()
            self.draw()
            pygame.display.update()
            for event in pygame.event.get():
                self.manage_event(event)

    def draw(self):
        pass

    def update(self):
        pass

    def manage_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            self.next_screen = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.running = False
            self.next_screen = False 
