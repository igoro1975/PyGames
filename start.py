import pygame
import os

WIDTH, HEIGHT = 1200, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# frames per second
FPS = 60
SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

pygame.display.set_caption("TBD Game's name")
PLAYER_WIDTH, PLAYER_HEIGHT = 55, 40
VEL = 5


def draw_window(hero):
    WIN.blit(SPACE, (0, 0))
    WIN.blit(hero.box, (hero.x, hero.y))
    hero.draw(WIN)

    pygame.display.update()


class player(object):
    def __init__(self, x, y):
        self.image = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
        self.box = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.x = x
        self.y = y

    def draw(self, win):
        WIN.blit(self.box, (self.x, self.y))

    def handle_movement(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT]:  # LEFT
            self.x -= VEL
        if keys_pressed[pygame.K_RIGHT]:  # RIGHT
            self.x += VEL
        if keys_pressed[pygame.K_UP]:  # UP
            self.y -= VEL
        if keys_pressed[pygame.K_DOWN]:  # DOWN
            self.y += VEL


def main():
    hero = player(10, 10)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()
        hero.handle_movement(keys_pressed)

        draw_window(hero)


if __name__ == "__main__":
    main()
