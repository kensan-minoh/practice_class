import pygame
import random

# difine classed
class Game():
    def __init__(self, knight_group, monster_group):
        self.knight_group = knight_group
        self.monster_group = monster_group

    def update(self):
        self.check_collisions()

    def check_collisions(self):
        pygame.sprite.groupcollide(self.knight_group, self.monster_group, False, True)

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

my_monster_group = pygame.sprite.Group()
my_knight_group = pygame.sprite.Group()

my_game = Game(my_knight_group, my_monster_group)

for i in range(10):
    x = i * 65
    y = 10
    monster = Monster(x, y)
    my_monster_group.add(monster)
    knight = Knight(x, WINDOW_HEIGHT-80)
    knight.add(my_knight_group)
    

# main game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the background
    display_surface.fill('black')

    # blit monsters and knights
    my_game.update()

    my_monster_group.update()
    my_knight_group.update()
    my_monster_group.draw(display_surface)
    my_knight_group.draw(display_surface)

    pygame.display.update()

    clock.tick(FPS)

# end the game
pygame.quit()

