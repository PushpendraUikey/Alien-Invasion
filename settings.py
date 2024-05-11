class Settings:
    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        # Ship settings 
        self.ship_speed = 1.5
        self.ship_limit = 2

        # Bullet Settings 
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15 
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right, while -1 represents left.
        self.fleet_direction = 1
        # Change the different settings to check the functionality of the codes.

        self.speedup_scale = 1.1        # how quickly game speeds up
        self.score_scale = 1.5         # how fast alien point scales up
        self.initialize_dynamic_settings()          # We can call a non-helper method from __init__ method but other method can call only helper method

    def initialize_dynamic_settings(self):
        # Initialize settings that change throughout the game
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 1.0
        self.fleet_drop_speed = 5

        self.fleet_direction = 1 # Represents, right direction 
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        # increases the speed of all the elements
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)  # Increasing the alien points.
