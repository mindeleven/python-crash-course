# starting the game project
# creating a pygame window and responding to user input
# we're stating with creating an empty pygame window
import sys

# pygame module contains functionality we need to make a game
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        # initializing the background settings
        pygame.init()

        # controlling the frame rate by setting up a clock
        # creating an instance of the class Clock from the pygame.time module
        self.clock = pygame.time.Clock()
        # accessing the settings
        self.settings = Settings()
        
        # creating a display window 
        # to draw the games graphical elements on
        self.screen = pygame.display.set_mode((
            self.settings.screen_width,
            self.settings.screen_height
        )) # tuple defines dimensions
        # object we assign to self.screen is called surface
        # once the game's animation loop is activated the surface will be redrawn
        # on every pass through the loop

        pygame.display.set_caption("Alien Invasion")

        # now lets get the ship and make an instance
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        # that's the method that controls the game
        # while loop contains event loop and code for screen updates
        while True:
            # nested for loop is an event loop
            # watch the keyboard and mouse events
            # isolating the event loop and moving it to a helper method
            self._check_events()

            # updating the screen
            self._update_screen_self()

            # making the clock tick
            self.clock.tick(60) # argument is frame rate for the game
            # here we tell pygame to do its best so that the loop will 
            # run 60 times per second

    def _check_events(self):
        """Respond to keypress and mouse events."""
        # we're accessing events with pygame.event.get()
        for event in pygame.event.get():
            # checking whether the player has clicked to close the window
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen_self(self):
        """Update images on the screen and flip to a new screen"""
        # filling the screen with the background color
        self.screen.fill(self.settings.bg_color)
        # position the ship
        self.ship.blitme()

        # make the most recent drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()

    

    