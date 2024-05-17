"""
File: rising_sun.py
Author: D. Cheng
Date: 2024-05-16
Description: Example Pygame animation.
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Example Animations")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 235)


# Load sprites
grass = pygame.image.load("grass.png")
grass = pygame.transform.scale(grass, (WIDTH, HEIGHT))

sun = pygame.image.load("sun.png")

# Create a Rect object for sprite and set initial position
moving_sun = sun.get_rect()

moving_sun.x = 400
moving_sun.bottom = HEIGHT

# Define main loop
running = True
clock = pygame.time.Clock()  # Create a Clock object for controlling frame rate

while running:
    # Handle events (leave this)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move sprite vertically
    if moving_sun.top >= 50:
        moving_sun.y -= 2
    
    # Draw graphics
    screen.fill(BLUE)
    screen.blit(sun, moving_sun)
    screen.blit(grass, (0, 0))
    
    # Update display
    pygame.display.flip()

    # Limit frame rate to 30 fps before refreshing loop
    clock.tick(30)

# Quit Pygame   
pygame.quit()
sys.exit()
