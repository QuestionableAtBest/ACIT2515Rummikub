import pygame

#Textbox example from class imported over
class TextBox(pygame.sprite.Sprite):
    def __init__(
        self,
        dimensions,
        text,
        id=None,
        color=(0, 0, 0),
        bgcolor=(255, 255, 255),
        font_size=24,
    ):
        if id is None:
            raise RuntimeError("Must provide ID for TextBox!")

        super().__init__()
        self.dimensions = dimensions
        self.color = color
        self.bgcolor = bgcolor
        self.font_size = font_size
        self.id = id

        self._selected = False

        self._text = text
        self.update()
        self.rect = self.image.get_rect()

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, value):
        new_value = bool(value)
        if self._selected != new_value:
            self._selected = bool(value)
            self.update()

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = str(value)
        self.update()

    def update(self):
        surface = pygame.Surface(self.dimensions)
        surface.fill(self.bgcolor)

        if self.selected:
            surface.fill((255, 0, 0))
            # 5px border when text is selected
            pygame.draw.rect(
                surface,
                self.bgcolor,
                (5, 5, self.dimensions[0] - 10, self.dimensions[1] - 10),
            )

        font = pygame.font.SysFont("Arial", self.font_size)
        text_surface = font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        # Makes a "border" by offsetting the text by 15px
        surface.blit(text_surface, (15, 15))
        # Draw the "cursor" when selected
        if self.selected:
            pygame.draw.rect(surface, (0, 0, 0), (15 + text_rect.right, 15, 10, text_rect.height))
        self.image = surface
