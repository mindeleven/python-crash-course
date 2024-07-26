import pygame

class Ship:
    """A class to manage the ship."""
    
    # takes an instance to the current instance of the AlienInvasion class as a parameter
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # screen gets assigned to an attribute of ship
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp') # returns surface repr. ship
        # accessing the ships rect attribute
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center to the screen
        # ship image gets centered horizontally and aligned to the bottom
        self.rect.midbottom = self.screen_rect.midbottom

        # store a float for the ships exact horizontal position
        # converting the value of self.rect.x to a float
        self.x = float(self.rect.x)

        # movement flag; start with a ship that's not moving
        self.moving_right = False # ship will be motionless
        self.moving_left = False

    def update(self):
        """Update the ships position based on the movement flag."""
        # moves the ship to the right if moving_right is True
        if self.moving_right:
            # self.rect.x += 1
            # update the ships x value, not the rect
            self.x += self.settings.ship_speed
        # moves the ship to the left if moving_left is True
        if self.moving_left:
            # self.rect.x -= 1
            # update the ships x value, not the rect
            self.x -= self.settings.ship_speed
        
        # update rect object from self.x
        # only the integer position will be assigned to self.rect.x
        self.rect.x = self.x


    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

