import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the screen."""

    def __init__(self, ai_game):
        """ Initialize the alien and sets its initial postion."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load the alien image and set its rect attributes.
        self.image = pygame.image.load('IMAGES/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # strore the alien's exact horizontal postion.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return true if the alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x