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

# Load background image and scale to fit window
road_background = pygame.image.load("images/road.png")
road_background = pygame.transform.scale(road_background, (WIDTH, HEIGHT))

# Load police car sprite
police_car = pygame.image.load("images/police_car.png")

# Create a Rect object to set the Rect dimensions exactly to the size
# of the police_car sprite
police_car_rect = police_car.get_rect()

# Set initial position of police car
police_car_rect.x = 400
police_car_rect.y = 500

# Define main loop
running = True
clock = pygame.time.Clock()  # Create a clock object to control frame rate

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # --(YOUR CODE STARTS HERE)-----------------------------------------------
    
    # Move police car
    police_car_rect.y -= 5

    # Reset police car position when it reaches the top
    if police_car_rect.bottom <= 0:
        police_car_rect.y = HEIGHT

    # Draw all elements
    screen.blit(road_background, (0, 0))
    screen.blit(police_car, police_car_rect)


    # --(YOUR CODE ENDS HERE)-------------------------------------------------

    # Update display
    pygame.display.flip()

    # Limit frame rate to 30 fps
    clock.tick(30)

# Quit Pygame   
pygame.quit()
sys.exit()
