"""
Author: D. Cheng
Date: 2024-05-16
Description: Animation of fish flipping directions at screen edges. Additional
             options to mirror sprite image, and add vertical oscillation to
             the fish movement.
"""

import pygame
import sys
import math  # Only necessary for sine function

# Initialize Pygame
pygame.init()

# Set up the display
# NOTE: You can change the display width and height if your background
#       image calls for other proportions or sizes.
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Example Animations")

# Load background image
# NOTE: More than just a variable name, we are technically creating an 
#       object called 'ocean_background' that can be manipulated and 
#       displayed on screen.
ocean_background = pygame.image.load("images/water_background.png")

# Scale the background image to fill the entire screen
ocean_background = pygame.transform.scale(ocean_background, (WIDTH, HEIGHT))

# Load fish.png image into fish_sprite, facing left (default)
fish_sprite = pygame.image.load("images/fish.png")

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

# Define direction multiplier, -1 for left-moving, 1 for right-moving
direction = -1

# Define parameters for sinusoidal oscillation
amplitude = 50  # Movement is 100 pixels peak-to-peak
frequency = 0.02  # Speed of oscillation


while running:
    # Handle events (leave this)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle change in position 
    dory.x += 5 * direction  # Move sprite horizontally 5px
    dory.y = 300 + amplitude * math.sin(frequency * dory.x)  # y-pos based on x-pos
 
    # Manage screen edge contact
    if dory.left == 0:
        # Change direction to right-moving
        direction = 1
        # Flip sprite image horizontally
        fish_sprite = pygame.transform.flip(fish_sprite, True, False)
    elif dory.right == WIDTH:
        # Change direction to left-moving
        direction = -1
        # Flip sprite image horizontally
        fish_sprite = pygame.transform.flip(fish_sprite, True, False)
    
    # Draw background ocean_background at location (0, 0)
    screen.blit(ocean_background, (0, 0))
    
    # Draw sprite image fish_sprite at location of dory
    screen.blit(fish_sprite, dory)
    
    # DEBUG: Output dory (x, y) coordinates
    print(f"dory position at ({dory.x}, {dory.y})", end="\r")

    # Update display
    pygame.display.flip()

    # Limit frame rate to 30 fps before refreshing loop
    clock.tick(30)

# Quit Pygame   
pygame.quit()
sys.exit()
