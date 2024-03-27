import sys
import pygame
from Settings import settings
from ship import Ship 
# from key_print import Print


class AlienInvasion:
    """Overall class to manage game assets and behaviour."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height 
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Alien Invasion")
                                                   # Set the background color.
                                                   # self.bg_color = (230,230,230)
        self.ship = Ship(self)                     # self arg refers to the current
                                                   # instance of AlienInvasion
        
    def run_game(self):
        """Start the main loop of the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
    
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
          
    def _check_keyup_events(self,event): 
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 

    def _update_screen(self):
           # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

