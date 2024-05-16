"""
File: example1.py
Author: D. Cheng
Date: 2024-05-16
Description: Example Pygame animation - continuous white circle falling vertically.
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Example Animations")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TEAL = (93, 138, 168)

# Define circle properties
circle_radius = 50
circle_x = WIDTH // 2
circle_y = -circle_radius  # Start above the screen
circle_speed = 5

# Define main loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update circle position
    circle_y += circle_speed
    
    # Reset position if circle goes off the bottom
    if circle_y - circle_radius > HEIGHT:
        circle_y = -circle_radius
    
    # Draw graphics
    screen.fill(TEAL)
    pygame.draw.circle(screen, WHITE, (circle_x, circle_y), circle_radius)
    
    # Update display
    pygame.display.flip()
    pygame.time.delay(30)  # Add a slight delay for smoother animation

# Quit Pygame   
pygame.quit()
sys.exit()
