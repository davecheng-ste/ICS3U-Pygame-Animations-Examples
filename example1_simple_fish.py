"""
Author: D. Cheng
Date: 2024-05-16
Description: Example Pygame animation - simplified fish sprite on background
             image with additional documentation.
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
# NOTE: You can change the display width and height if your background
#       image calls for other proportions or sizes.
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Example Animations")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load background image
# NOTE: More than just a variable name, we are technically creating an 
#       object called 'ocean_background' that can be manipulated and 
#       displayed on screen.
ocean_background = pygame.image.load("water_background.png")

# Scale the background image to fill the entire screen
ocean_background = pygame.transform.scale(ocean_background, (WIDTH, HEIGHT))

# Load fish.png image into fish_sprite
fish_sprite = pygame.image.load("fish.png")

# Create a Rect object called dory, using fish_sprite.get_rect() to 
# set the Rect dimensions exactly to the size of the image loaded
# with fish_sprite 
dory = fish_sprite.get_rect()

# Set initial position of dory (top right corner) using .x and .y attributes
dory.x = 400
dory.y = 300

# Define main loop (leave this)
running = True
clock = pygame.time.Clock()  # Create a Clock object for controlling frame rate

while running:
    # Handle events (leave this)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move sprite horizontally 5px with every screen refresh
    dory.x -= 5
    
    # Reset position if sprite goes off the left
    if dory.right <= 0:
        dory.left = WIDTH
    
    # Draw background ocean_background at location (0, 0)
    screen.blit(ocean_background, (0, 0))
    
    # Draw sprite image fish_sprite at location of dory
    screen.blit(fish_sprite, dory)
    
    # DEBUG: Output dory (x, y) coordinates
    # print(f"dory position at ({dory.x}, {dory.y})", end="\r")

    # Update display
    pygame.display.flip()

    # Limit frame rate to 30 fps before refreshing loop
    clock.tick(30)

# Quit Pygame   
pygame.quit()
sys.exit()
