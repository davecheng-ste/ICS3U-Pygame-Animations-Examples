"""
File: main.py
Author: YOUR NAME
Date: YYYY-MM-DD
Description: Description of your program here.
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Animation")

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TEAL = (93, 138, 168)

# Define main loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw graphics
    # --(YOUR CODE STARTS HERE)-----------------------------------------------
    screen.fill(TEAL)







    # --(YOUR CODE ENDS HERE)-------------------------------------------------

    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()
