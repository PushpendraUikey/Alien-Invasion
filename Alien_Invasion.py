# from operator import ne
import sys
from matplotlib.style import available
import pygame
from pyparsing import null_debug_action
from settings import Settings
from ship import Ship 
from bullet import Bullet
from alien import Alien
# from key_print import Print


class AlienInvasion:
    """Overall class to manage game assets and behaviour."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height 
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Alien Invasion")
                                                   # Set the background color.
                                                   # self.bg_color = (230,230,230)
        self.ship = Ship(self)                     # self arg refers to the current
                                                   # instance of AlienInvasion
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        
    def run_game(self):
        """Start the main loop of the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
    
    def _update_bullets(self):
        '''update postions of bullet and get rid of old bullets.'''
            # update bullet positions.
        self.bullets.update()
            # Get rid of the bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_events(self):                   # A single leading underscore indicates a helper method.
            # Watch the keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:      # User clicked X in the window to close the game 
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                    """printit = Print(event)     # Here printing the events that occured in the game
                    printit.print()"""          # Since right now I can't open two pygame simultaneously.

                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
         
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:  # The right arrow key is represented by pygame.K_RIGHT
            self.ship.moving_right = True 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:     # ends the game if player presses the "q"
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()           # ready to fire bullets

    def _check_keyup_events(self,event): 
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) <= self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _create_fleet(self):
        """create the fleet of aliens"""
        # create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2*alien_width)

        # determine number of rows of aliens that fit into the screen.
        ship_height = self.ship.rect.height

        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # create full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                #create an alien and place it in the row.
                self._create_alien(alien_number, row_number)
        
    def _create_alien(self,alien_number, row_number):
        """Create alien and place it in a row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + (2 * alien_width * alien_number)
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number)
        self.aliens.add(alien)

    def _update_screen(self):
           # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets:
                bullet.draw_bullet()
            self.aliens.draw(self.screen)
            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


