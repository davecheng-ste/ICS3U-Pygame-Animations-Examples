"""
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
SKY_BLUE = (135, 206, 234)

# Load sprites and background
grass = pygame.image.load("images/grass.png")
grass = pygame.transform.scale(grass, (WIDTH, HEIGHT))

sun = pygame.image.load("images/sun.png")

# Create and initialize Rect object for sun sprite
sun_rect = sun.get_rect()
sun_rect.x = 300
sun_rect.y = 400

# Define main loop
running = True
clock = pygame.time.Clock()  # Create a clock object to limit frame rate


while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw graphics
    # --(YOUR CODE STARTS HERE)-----------------------------------------------
    
    if not sun_rect.top <= 0:
        sun_rect.y -= 5
        
    # Draw everything
    screen.fill(SKY_BLUE)
    screen.blit(sun, sun_rect)
    screen.blit(grass, (0, 0))


    # DEBUG: Output position of sun
    print(f"sun position {sun_rect.x}, {sun_rect.y}")
    
    # --(YOUR CODE ENDS HERE)-------------------------------------------------

    # Update display
    pygame.display.flip()
    clock.tick(30)  # Limit to 30 fps

# Quit Pygame   
pygame.quit()
sys.exit()
