"""
File: example2.py
Author: D. Cheng
Date: 2024-05-16
Description: Example Pygame animation - moving sprite on background image.
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Example Animations")

# Load background image
ocean_background = pygame.image.load("water_background.png").convert()

# Scale the background image to fill the entire screen
ocean_background = pygame.transform.scale(ocean_background, (WIDTH, HEIGHT))

# Load fish.png into sprite_image
fish_sprite = pygame.image.load("fish.png").convert_alpha()

# Create a rect object around sprite_image, defining the rect's midpoint on the right 
# side of its bounding rectangle, placing it at (800, 300) or the far right-side
fish_rect = fish_sprite.get_rect(midright=(WIDTH, HEIGHT // 2))  

# Define main loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move sprite horizontally
    fish_rect.x -= 5
    
    # Reset position if sprite goes off the left
    if fish_rect.right <= 0:
        fish_rect.left = WIDTH
    
    # Draw background at location (0, 0)
    screen.blit(ocean_background, (0, 0))
    
    # Draw fish_sprite at location fish_rect
    screen.blit(fish_sprite, fish_rect)
    
    # Update display
    pygame.display.flip()
    pygame.time.delay(30)  # Add a slight delay for smoother animation

# Quit Pygame   
pygame.quit()
sys.exit()
