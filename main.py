import game
import pygame

gioco = game.Game(800, 800)
change = 0
movement = ''
running = True

while running:
    
    gioco.screen_fill()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change = -0.3
                movement = 'snake_x'
                
                
            elif event.key == pygame.K_RIGHT:
                change = 0.3
                movement = 'snake_x'
                
                
            elif event.key == pygame.K_UP:
                change = -0.3
                movement = 'snake_y'
                

            elif event.key == pygame.K_DOWN:
                change = 0.3
                movement = 'snake_y'
                

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                change = 0
                
                
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                change = 0
                

    
    
    gioco.move_snake([movement, change])

    gioco.update_screen()