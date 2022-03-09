# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([800, 600])

# Run until the user asks to quit
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((0, 255, 0))

    pygame.draw.rect(screen, 'red', (300, 200, 50, 50))

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 20)
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()