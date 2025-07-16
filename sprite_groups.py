import pygame
import random

# initialize pygame
pygame.init()

# creating display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('sprite groups')

# set FPS and the clock
FPS = 60
clock = pygame.time.Clock()

# difine classes
class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, groups):
        super().__init__(groups)
        self.image = pygame.image.load('blue_monster64.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

        self.velocity = random.randint(1, 5)

    def update(self):
        self.rect.y += self.velocity

# create a monster group and add 10 monsters
monster_group = pygame.sprite.Group()
 
for i in range(10):
    x = random.randint(0, WINDOW_WIDTH-64) 
    y = 20
    Monster(x, y, monster_group)

# main game loop
running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # fill the background
    display_surface.fill('black')

    # draw the assets
    monster_group.update()
    # for sprite in monster_group.sprites():  下の方がよりシンプル
    for sprite in monster_group:
        if sprite.rect.y > WINDOW_HEIGHT-100:
            #sprite.remove(monster_group)　　   これら３行は結果的に同じ働き
            #monster_group.remove(sprite)
            sprite.kill()
            #sprite.remove()                    これはダメ。group名が必要
            x = random.randint(0, WINDOW_WIDTH-64) 
            y = 20
            Monster(x, y, monster_group)

    monster_group.draw(display_surface)
    pygame.display.update()

    clock.tick(FPS)

# end the game
pygame.quit()
