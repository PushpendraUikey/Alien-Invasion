import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the screen."""

    def __init__(self, ai_game):
        """ Initialize the alien and sets its initial postion."""
        super().__init__()
        self.screen = ai_game.screen

        #Load the alien image and set its rect attributes.
        self.image = pygame.image.load('IMAGES/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # strore the alien's exact horizontal postion.
        self.x = float(self.rect.x)