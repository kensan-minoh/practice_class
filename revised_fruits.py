import pygame
import random








class Fruits(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load("fruits.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(random.randint(0, WINDOW_WIDTH-64),random.randint(0, WINDOW_HEIGHT-64)))

class Lemon(Fruits):
    def __init__(self,groups):
        super().__init__(groups)
        self.image = pygame.image.load("lemon64.png")


pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

fruits_group = pygame.sprite.Group()
lemon_group = pygame.sprite.Group()
        

for i in range(5):
    # #method 1+++++++++++++++++++++++++
    # fruit = Fruits(fruits_group)

    # #+++++++++++++++++++++++++++++++++
    #method 2+++++++++++++++++++++++++
    Fruits(fruits_group)

    #+++++++++++++++++++++++++++++++++

 

    print(len(fruits_group))

for i in range(3):
    Lemon([lemon_group, fruits_group])

    print(len(fruits_group))
    print(len(lemon_group))

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
