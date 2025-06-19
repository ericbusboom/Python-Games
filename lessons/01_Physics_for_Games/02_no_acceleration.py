"""
Move a square, with no acceleration
"""
import pygame

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
SQUARE_SIZE = 50
SQUARE_COLOR = (255, 0, 0)  # Red
SQUARE_SPEED = 5

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Red Square")

# Square starting position
x_pos = 0
y_pos = (SCREEN_HEIGHT - SQUARE_SIZE) // 2

# Movement direction: 1 for right, -1 for left
direction = 1

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the square, a bit each frame
    x_pos += SQUARE_SPEED * direction

    # Check for screen bounds and reverse direction if necessary
    if x_pos + SQUARE_SIZE > SCREEN_WIDTH:
        direction = -1  # Move left
    elif x_pos < 0:
        direction = 1  # Move right

    # Fill the screen with black (clears previous frame)
    screen.fill((0, 0, 0))

    # Draw the red square
    pygame.draw.rect(screen, SQUARE_COLOR, (x_pos, y_pos, SQUARE_SIZE, SQUARE_SIZE))

    # Update the display
    pygame.display.flip()

    # Frame rate control
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
