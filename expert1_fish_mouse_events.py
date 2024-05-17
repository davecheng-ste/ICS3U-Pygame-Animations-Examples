"""
Author: D. Cheng
Date: 2024-05-16
Description: Moving fish animation with mouse-click event 
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

# Load background image
ocean_background = pygame.image.load("images/water_background.png")
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

# Define main loop
running = True
clock = pygame.time.Clock()  # Create a Clock object for controlling frame rate

# Define direction multiplier, -1 for left-moving, 1 for right-moving
direction = -1

# Store the falling fish food positions and radii in a list
# List format: [x-position, y-position, radius]
fish_food_list = []

while running:
    # Handle events
    for event in pygame.event.get():
        # If left mouse button clicked, create a circle at current mouse position
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Get x, y of mouse-click from event handler
                x, y = event.pos
                # Add new instance to fish food list
                fish_food_list.append([x, y, 7])  # Format: [x-position, y-position, radius]
        # On window quit, end loop
        elif event.type == pygame.QUIT:
            running = False
    
    # Move sprite horizontally
    dory.x += 5 * direction
    
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
    
    # Draw background
    screen.blit(ocean_background, (0, 0))
    
    # Draw sprite image
    screen.blit(fish_sprite, dory)
    
    # DEBUG: Output list of all tracked food
    print(f"fish_food_list at {fish_food_list}")
    
    # Update and draw fish food, iterating through list of all food
    for single_food in fish_food_list:
        # Unpack each and assign x, y, radius
        x, y, radius = single_food
        pygame.draw.circle(screen, WHITE, (x, y), radius)
        # Move food position down (falling)
        single_food[1] += 5 
        # If food reaches the bottom, remove it from the list
        if y >= HEIGHT:
            fish_food_list.remove(single_food)
    
    # Update display
    pygame.display.flip()
    
    # Limit frame rate to 30 fps
    clock.tick(30)

# Quit Pygame   
pygame.quit()
sys.exit()
