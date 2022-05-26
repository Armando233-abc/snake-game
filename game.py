import pygame
import random


class Game:
    __screen = None
    __circle = None
    __circle_x = None
    __circle_y = None

    __snakes = []
    __changes = None

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
        
        if(len(self.__snakes) == 0):
            self.__snakes.append({
                "snake": pygame.image.load("square.png"),
                "snake_x": 0,
                "snake_y": 0
            })

            self.__snakes[0]["snake"] = pygame.transform.scale(self.__snakes[0]["snake"], (30, 30))
        else:
            cordinate = self.get_cordinate_change()
            self.__snakes.append({
                "snake": pygame.image.load("square.png"),
                "snake_x": self.__snakes[len(self.__snakes) - 1]["snake_x"] + cordinate[0],
                "snake_y": self.__snakes[len(self.__snakes) - 1]["snake_y"] + cordinate[1]
            })

            self.__snakes[len(self.__snakes) - 1]["snake"] = pygame.transform.scale(self.__snakes[0]["snake"], (30, 30))
        
    
    def get_cordinate_change(self):
        snake_x = 0
        snake_y = 0
        if(self.__changes[0] == 'snake_x' and self.__changes[1] < 0):
            snake_x = 30
        elif(self.__changes[0] == 'snake_x' and self.__changes[1] > 0):
            snake_x = -30
        elif(self.__changes[0] == 'snake_y' and self.__changes[1] < 0):
            snake_y = 30
        elif(self.__changes[0] == 'snake_y' and self.__changes[1] > 0):
            snake_y = -30
        return [snake_x, snake_y]

    def __controll_snake_position(self, snake):
        if snake['snake_x'] < 0:
            snake['snake_x'] = 750

        elif snake['snake_x'] >= 800:
            snake['snake_x'] = 0.1

        if snake['snake_y'] <= 0:
            snake['snake_y'] = 750

        elif snake['snake_y'] >= 800:
            snake['snake_y'] = 0.1


    def __control_eat(self):
        head_snake = self.__snakes[0]
        distance = ((self.__circle_x - head_snake['snake_x'])**2 +
                    (self.__circle_y - head_snake['snake_y'])**2) ** 0.5

        if distance >= 0 and distance <= 20:
            self.__create_snake()
            self.__circle_x = random.randint(50, 750)
            self.__circle_y = random.randint(50, 750)


    def move_snake(self, changes):
        if(changes[0] == ''):
            return 0
        for snake in self.__snakes:
            self.__changes = changes
            self.__screen.blit(
                snake['snake'], (snake['snake_x'], snake['snake_y']))
            

            snake[changes[0]] += changes[1]
            
            self.__controll_snake_position(snake)
            self.__control_eat()
            self.__screen.blit(
                self.__circle, (self.__circle_x, self.__circle_y))

    def update_screen(self):
        pygame.display.update()

    def screen_fill(self):
        self.__screen.fill((0, 255, 0))
