import pygame

class Ship:
    """A class to manage the ship."""
    
    # takes an instance to the current instance of the AlienInvasion class as a parameter
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        # screen gets assigned to an attribute of ship
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp') # returns surface repr. ship
        # accessing the ships rect attribute
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center to the screen
        # ship image gets centered horizontally and aligned to the bottom
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

