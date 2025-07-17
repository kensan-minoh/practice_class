import pygame
import random

# difine classed
class Game():
    def __init__(self):
        pass

    def update(self, group1, group2):
        self.check_collisions(group1, group2)

    def check_collisions(self, group1, group2):
        pygame.sprite.groupcollide(group1, group2, False, True)







class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('blue_monster64.png')
        self.rect = self.image.get_rect(topleft=(x,y))
        self.velocity = random.randint(1, 5)

    def update(self):
        self.rect.y += self.velocity

class Knight(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('knight64.png')
        self.rect = self.image.get_rect(topleft=(x,y))
        self.velocity = random.randint(1, 5)

    def update(self):
        self.rect.y -= self.velocity

# initialize pygame
pygame.init()





# create a display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Group Collide')

# set FPS and the clock
FPS = 60
clock = pygame.time.Clock()

monster_group = pygame.sprite.Group()
knight_group = pygame.sprite.Group()

my_game = Game()

for i in range(10):
    x = i * 65
    y = 10
    monster = Monster(x, y)
    monster_group.add(monster)
    knight = Knight(x, WINDOW_HEIGHT-80)
    knight.add(knight_group)
    

# main game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the background
    display_surface.fill('black')

    # blit monsters and knights
    my_game.update(knight_group, monster_group)

    monster_group.update()
    knight_group.update()
    monster_group.draw(display_surface)
    knight_group.draw(display_surface)

    pygame.display.update()

    clock.tick(FPS)

# end the game
pygame.quit()

