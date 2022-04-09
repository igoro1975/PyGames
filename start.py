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
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

pygame.display.set_caption("TBD Game's name")
PLAYER_WIDTH, PLAYER_HEIGHT = 55, 40
VEL = 5
people = []


def draw_window(hero):
    WIN.blit(SPACE, (0, 0))
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
                draw_text = HAPPY_FONT.render("I am happy now!", 1, WHITE)
                WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() /
                                     2, HEIGHT / 2 - draw_text.get_height() / 2))
                pygame.display.update()


def main():
    hero = player(10, 10)
    poor = man(300, 300)
    people.append(poor)
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
