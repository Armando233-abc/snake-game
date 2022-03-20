import game
import pygame

snake_x_change = 0
snake_y_change = 0

gioco = game.Game(800, 800)

running = True

while running:
    
    gioco.screen_fill()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -0.3

            if event.key == pygame.K_RIGHT:
                snake_x_change = 0.3

            if event.key == pygame.K_UP:
                snake_y_change = -0.3

            if event.key == pygame.K_DOWN:
                snake_y_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                snake_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                snake_y_change = 0

    gioco.move_snake(snake_x_change, snake_y_change)
    gioco.update_screen()