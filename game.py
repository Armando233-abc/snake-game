import pygame
import random


class Game:
    __screen = None
    __circle = None
    __circle_x = None
    __circle_y = None

    __snake = None
    __snake_x = 0
    __snake_y = 0

    def __init__(self, x, y):  
        pygame.init()
        self.__screen = pygame.display.set_mode([x, y])
        self.__create_snake()
        self.__create_circle()
    
    def __create_circle(self):
        self.__circle = pygame.image.load("circle.png")
        self.__circle = pygame.transform.scale(self.__circle, (20, 20))
        self.__circle_x = random.randint(50, 750)
        self.__circle_y = random.randint(50, 750)
        
    def __create_snake(self):
        self.__snake = pygame.image.load("square.png")
        self.__snake = pygame.transform.scale(self.__snake, (30, 30))

    def __controll_snake_position(self):
        if self.__snake_x < 0:
            self.__snake_x = 750

        elif self.__snake_x >= 800:
            self.__snake_x = 0.1

        if self.__snake_y <= 0:
            self.__snake_y = 750

        elif self.__snake_y >= 800:
            self.__snake_y = 0.1

    
    def __control_eat(self):
        distance = ((self.__circle_x - self.__snake_x)**2 + (self.__circle_y - self.__snake_y )**2) ** 0.5 
    
        if distance >= 0 and distance <= 20:
            self.__circle_x = random.randint(50, 750)
            self.__circle_y = random.randint(50, 750)


    def move_snake(self, x_change, y_change):
        self.__screen.blit(self.__snake, (self.__snake_x, self.__snake_y))
        self.__snake_x += x_change
        self.__snake_y += y_change
        self.__controll_snake_position()
        self.__control_eat()
        self.__screen.blit(self.__circle, (self.__circle_x, self.__circle_y))

    def update_screen(self):
        pygame.display.update()

    def screen_fill(self):
        self.__screen.fill((0, 255, 0))

