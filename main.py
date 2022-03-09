import pygame
pygame.init()

screen = pygame.display.set_mode([800, 800])


snake = pygame.image.load("square.png")
snake = pygame.transform.scale(snake, (50, 50))
snake_X_change = 0
snake_Y_change = 0

def left_right(x, y):
    screen.blit(snake, (x, y))

running = True
while running:
    screen.fill((0, 255, 0))

    # background image
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_X_change -= 50

            if event.key == pygame.K_RIGHT:
                snake_X_change += 50

            if event.key == pygame.K_UP:
                snake_Y_change -= 50

            if event.key == pygame.K_DOWN:
                snake_Y_change += 50

    if snake_X_change <= 0:
        snake_X_change = 750

    elif snake_X_change >= 800:
        snake_X_change = 0.1

    if snake_Y_change <= 0:
        snake_Y_change = 750

    elif snake_Y_change >= 800:
        snake_Y_change = 0.1

    left_right(snake_X_change, snake_Y_change)
    pygame.display.update()

