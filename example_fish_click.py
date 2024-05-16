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
ocean_background = pygame.image.load("water_background.png")
ocean_background = pygame.transform.scale(ocean_background, (WIDTH, HEIGHT))

# Load fish.png image into fish_sprite, facing left (default)
fish_sprite = pygame.image.load("fish.png")

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

# Store the falling circles' positions and radii in a list
falling_circles = []

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # If left mouse button clicked, create a falling circle at mouse position
            if event.button == 1:
                x, y = event.pos
                falling_circles.append([x, y, 10])  # [x, y, radius]
    
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
    
    # Update and draw falling circles
    for circle in falling_circles:
        x, y, radius = circle
        pygame.draw.circle(screen, WHITE, (x, y), radius)
        # Update falling circle's position (move it down)
        circle[1] += 5 # Increment y-coordinate
        # If falling circle reaches the bottom, remove it from the list
        if y + radius >= HEIGHT:
            falling_circles.remove(circle)
    
    # Collision detection between dory and falling circles
    for circle in falling_circles:
        circle_rect = pygame.Rect(circle[0] - circle[2], circle[1] - circle[2], circle[2] * 2, circle[2] * 2)
        if dory.colliderect(circle_rect):
            # Flip direction
            if direction == -1:
                direction = 1
                fish_sprite = pygame.transform.flip(fish_sprite, True, False)
            elif direction == 1:
                direction = -1
                fish_sprite = pygame.transform.flip(fish_sprite, True, False)
            # Remove the collided circle
            falling_circles.remove(circle)

    # Update display
    pygame.display.flip()
    
    # Limit frame rate to 30 fps
    clock.tick(30)

# Quit Pygame   
pygame.quit()
sys.exit()
