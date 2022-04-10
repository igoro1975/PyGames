import pygame
import os

pygame.font.init()

HAPPY_FONT = pygame.font.SysFont('comicsans', 50)
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 1200, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# frames per second
FPS = 60
SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'bg1.jpg')), (WIDTH, HEIGHT))


# explanation https://coderslegacy.com/python/pygame-scrolling-background/
class Background(object):
    def __init__(self):
        self.bgimage = pygame.image.load(os.path.join('Assets', 'bg1.jpg'))
        self.rectBGimg = self.bgimage.get_rect()

        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = 0
        self.bgX2 = self.rectBGimg.width

        self.moving_speed = 3

    def update(self):
        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width

    def render(self):
        WIN.blit(self.bgimage, (self.bgX1, self.bgY1))
        WIN.blit(self.bgimage, (self.bgX2, self.bgY2))


pygame.display.set_caption("TBD Game's name")
PLAYER_WIDTH, PLAYER_HEIGHT = 55, 40
VEL = 5
people = []


def draw_window(hero, background):
    background.update()
    background.render()

    # WIN.blit(SPACE, (0, 0))
    WIN.blit(hero.box, (hero.x, hero.y))
    hero.draw(WIN)

    for poor in people:
        poor.draw(WIN)

    pygame.display.update()


class man(object):
    def __init__(self, x, y):
        self.image = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
        self.box = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.x = x
        self.y = y

    def draw(self, win):
        WIN.blit(self.box, (self.x, self.y))


class player(object):
    def __init__(self, x, y):
        self.image = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
        self.box = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.x = x
        self.y = y

    def draw(self, win):
        WIN.blit(self.box, (self.x, self.y))

    def handle_movement(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT] and self.x - VEL > 0:  # LEFT
            self.x -= VEL
        if keys_pressed[pygame.K_RIGHT] and self.x + VEL + self.box.get_width() < WIDTH:  # RIGHT
            self.x += VEL
        if keys_pressed[pygame.K_UP] and self.y - VEL > 0:  # UP
            self.y -= VEL
        if keys_pressed[pygame.K_DOWN] and self.y + VEL + self.box.get_height() < HEIGHT:  # DOWN
            self.y += VEL

        self.rect = pygame.Rect(self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT)

        for poor in people:
            if self.rect.colliderect(poor.rect):
                people.remove(poor)


def main():
    hero = player(10, 10)
    poor1 = man(100, 100)
    poor2 = man(200, 200)
    people.append(poor1)
    people.append(poor2)
    clock = pygame.time.Clock()
    background = Background()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()
        hero.handle_movement(keys_pressed)

        draw_window(hero, background)


if __name__ == "__main__":
    main()
