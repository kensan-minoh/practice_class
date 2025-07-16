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

class Knight(pygame.sprite.Sprite):
    def __init__(self, x, y, monster_group, groups):
        super().__init__(groups)
        self.image = pygame.image.load('knight64.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(x,y))
        self.monster_group = monster_group
        self.velocity = 5

    def update(self):
        self.move()
        self.check_collisions()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y += -self.velocity
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocity
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        if keys[pygame.K_LEFT]:
            self.rect.x += -self.velocity

    def check_collisions(self):
        
        if pygame.sprite.spritecollide(self, self.monster_group, True):
            print(len(self.monster_group))

        # for sprite in self.monster_group:
        #     if pygame.sprite.collide_rect(self, sprite):
        #         print('collided!')
        #         sprite.kill()
    
# create a monster group and add 10 monsters
my_monster_group = pygame.sprite.Group()
 
for i in range(10):
    x = i * 70
    y = 20
    Monster(x, y, my_monster_group)

# create  a group class and a knight
knight_group = pygame.sprite.Group()
x = WINDOW_WIDTH // 2
y = WINDOW_HEIGHT // 2
knight = Knight(x, y, my_monster_group, knight_group)


# main game loop
running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # fill the background
    display_surface.fill('black')

    # draw the assets

    my_monster_group.update()
    knight_group.update()

 
    my_monster_group.draw(display_surface)
    knight_group.draw(display_surface)

    pygame.display.update()

    clock.tick(FPS)

# end the game
pygame.quit()
