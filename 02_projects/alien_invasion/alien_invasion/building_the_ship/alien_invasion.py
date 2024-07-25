# starting the game project
# creating a pygame window and responding to user input
# we're stating with creating an empty pygame window
import sys

# pygame module contains functionality we need to make a game
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        # initializing the background settings
        pygame.init()
        
        # creating a display window 
        # to draw the games graphical elements on
        self.screen = pygame.display.set_mode((1200, 800)) # tuple defines dimensions
        # object we assign to self.screen is called surface
        # once the game's animation loop is activated the surface will be redrawn
        # on every pass through the loop

        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        # that's the method that controls the game
        # while loop contains event loop and code for screen updates
        while True:
            # nested for loop is an event loop
            # watch the keyboard and mouse events
            # we're accessing events with pygame.event.get()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # make the most recent drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()

    

    