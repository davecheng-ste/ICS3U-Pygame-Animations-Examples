"""
Author: D. Cheng
Date: 2024-05-17
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

# Load sprites

# Create a Rect object for sprite and set initial position

# Define main loop
running = True
clock = pygame.time.Clock()  # Create a Clock object for controlling frame rate

while running:
    # Handle events (leave this)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    



    # Draw graphics
    screen.fill(WHITE)
    
    # Update display
    pygame.display.flip()

    # Limit frame rate to 30 fps before refreshing loop
    clock.tick(30)

# Quit Pygame   
pygame.quit()
sys.exit()
