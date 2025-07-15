import pygame
import random

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

fruits_group = pygame.sprite.Group()
lemon_group = pygame.sprite.Group()



class Fruits(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("fruits.png")
        self.rect = self.image.get_rect(topleft=(random.randint(0, WINDOW_WIDTH-64),random.randint(0, WINDOW_HEIGHT-64)))

class Lemon(Fruits):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lemon64.png")

        

for i in range(5):
    #method 1+++++++++++++++++++++++++
    # fruit = Fruits()
    # fruits_group.add(fruit)
    #+++++++++++++++++++++++++++++++++

    #method 2*************************
    #fruits_group.add(Fruits())
    #*********************************

    #metho 3 =========================
    #Fruits().add(fruits_group)
    #=================================

    #method 4+++++++++++++++++++++++++
    fruit = Fruits()
    fruit.add(fruits_group)
    #+++++++++++++++++++++++++++++++++

    print(len(fruits_group))

for i in range(3):
    Lemon().add(lemon_group, fruits_group)

    print(len(fruits_group))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    # fill the display
    display_surface.fill('black')


    fruits_group.draw(display_surface)
    lemon_group.draw(display_surface)

    pygame.display.update()
