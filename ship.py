import pygame 

class Ship:
    # A class to manage the ship.
    def __init__(self,ai_game, scale_factor = 0.15):
        # Initialize the ship and set its starting position. 
        self.screen = ai_game.screen 
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect. 
        # original_image = pygame.image.load('PROJECTS/ALIEN_INVASION/IMAGES/ship.bmp')
        original_image = pygame.image.load('IMAGES/ship.bmp')

        # Resize the image based on the scale_factor.
        width = int(original_image.get_width()*scale_factor)
        height = int(original_image.get_height()*scale_factor)
        self.image = pygame.transform.scale(original_image,(width,height))

        self.rect = self.image.get_rect() 
        # Start each new ship at the bottom center of the screen. 
        self.rect.midbottom = self.screen_rect.midbottom 

        #Store a decimal value for the ship's horizontal position 
        self.x = float(self.rect.x)        #because it takes by default integer values
        
        # movement flag 
        self.moving_right = False 
        self.moving_left = False

    def update(self):
        # Update the ship's position based on the movement flag. 
        if self.moving_right and self.rect.right < self.screen_rect.right:
                self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
                self.x -= self.settings.ship_speed

        self.rect.x = int(self.x)     # Here casted to int bcz float can't be assigned to int.

    def blitme(self):
        # Draw the ship at its current location.
        self.screen.blit(self.image,self.rect)
    
    def center_ship(self):
         """Center the ship on the screen"""
         self.rect.midbottom = self.screen_rect.midbottom
         self.x = float(self.rect.x)