import pygame
import os
from pygame.locals import *
import random

pygame.init()
W, H = 800, 437
win = pygame.display.set_mode((W, H))

bg = pygame.image.load(os.path.join('game', 'bg.png')).convert()

clock = pygame.time.Clock()

hitSound = pygame.mixer.Sound("game\hit.wav")

music = pygame.mixer.music.load("game\dbackground.mp3")

pygame.mixer.music.play(-1)

class player(object):
    run = [pygame.image.load(os.path.join('game', str(x) + '.png')) for x in range(8, 16)]
    jump = [pygame.image.load(os.path.join('game', str(x) + '.png')) for x in range(1, 8)]
    slide = [pygame.image.load(os.path.join('game', 'S1.png')), pygame.image.load(os.path.join('game', 'S2.png')),
             pygame.image.load(os.path.join('game', 'S2.png')), pygame.image.load(os.path.join('game', 'S2.png')),
             pygame.image.load(os.path.join('game', 'S2.png')), pygame.image.load(os.path.join('game', 'S2.png')),
             pygame.image.load(os.path.join('game', 'S2.png')), pygame.image.load(os.path.join('game', 'S2.png')),
             pygame.image.load(os.path.join('game', 'S3.png')), pygame.image.load(os.path.join('game', 'S4.png')),
             pygame.image.load(os.path.join('game', 'S5.png'))]
    fall = pygame.image.load(os.path.join('game', '0.png'))
    jumpList = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
                4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1,
                -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,
                -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.slideUp = False

    def draw(self, win):
        if self.jumping:
            self.y -= self.jumpList[self.jumpCount] * 1.3
            win.blit(self.jump[self.jumpCount // 18], (self.x, self.y))
            self.jumpCount += 1
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
            self.hitbox = (self.x + 4, self.y, self.width - 24, self.height - 10)  # NEW
        elif self.sliding or self.slideUp:
            if self.slideCount < 20:
                self.y += 1
                self.hitbox = (self.x + 4, self.y, self.width - 24, self.height - 10)  # NEW
            elif self.slideCount == 80:
                self.y -= 19
                self.sliding = False
                self.slideUp = True
            # NEW ELIF STATEMENT
            elif self.slideCount > 20 and self.slideCount < 80:  # NEW
                self.hitbox = (self.x, self.y + 3, self.width - 8, self.height - 35)  # NEW

            if self.slideCount >= 110:
                self.slideCount = 0
                self.runCount = 0
                self.slideUp = False
                self.hitbox = (self.x + 4, self.y, self.width - 24, self.height - 10)  # NEW
            win.blit(self.slide[self.slideCount // 10], (self.x, self.y))
            self.slideCount += 1

        else:
            if self.runCount > 42:
                self.runCount = 0
            win.blit(self.run[self.runCount // 6], (self.x, self.y))
            self.runCount += 1
            self.hitbox = (self.x + 4, self.y, self.width - 24, self.height - 13)  # NEW

        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)  # NEW - Draws hitbox

class saw(object):

    rotate = [pygame.image.load(os.path.join('game', 'SAW0.PNG'))
        ,pygame.image.load(os.path.join('game', 'SAW1.PNG'))
        ,pygame.image.load(os.path.join('game', 'SAW2.PNG'))
        ,pygame.image.load(os.path.join('game', 'SAW3.PNG'))]

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x,y,width,height)
        self.count = 0



    def draw(self,win):
        self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

        if self.count >= 4:
            self.count = 0
        win.blit(pygame.transform.scale(self.rotate[self.count], (64,64)), (self.x,self.y))  # scales our image down to 64x64 before drawing
        self.count += 1

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

class spike(saw):  # We are inheriting from saw
    img = pygame.image.load(os.path.join('game', 'spike.png'))


    def draw(self,win):
        self.hitbox = (self.x + 10, self.y, 28,315)  # defines the hitbox
        win.blit(self.img, (self.x, self.y))
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] < self.hitbox[3]:
                return True
        return False

def redrawWindow():
    win.blit(bg, (bgX, 0))  # draws our first bg image
    win.blit(bg, (bgX2, 0))  # draws the seconf bg image
    runner.draw(win)  # NEW

#    spikee.draw(win)
#    saww.draw(win)                                           ##

    for obstacle in obstacles:
        obstacle.draw(win)

    pygame.display.update()  # updates the screen

pygame.time.set_timer(USEREVENT+1, 50) # Sets the timer

pygame.time.set_timer(USEREVENT+2, random.randrange(2000, 3500)) # Will trigger every 2 - 2.5 seconds

runner = player(200, 313, 64, 64)


bgX = 0
bgX2 = bg.get_width()
run = True
speed = 30  # NEW

#spikee = spike(600,0,48,320)
#saww = saw(300,305,64,64)                                   ###

obstacles = []

while run:
    redrawWindow()

    for obstacle in obstacles:
        if obstacle.collide(runner.hitbox):
            print("hit")
            hitSound.play()

    for obstacle in obstacles:
        obstacle.x -= 1.4

        if obstacle.x < -200:
            obstacles.pop(obstacles.index(obstacle))

#    spikee.x -= 1
#    saww.x -= 1

#    if spikee.x < -200 :
#        spikee.x = 1000

#    if saww.x < -300 :
#        saww.x = 900

    bgX -= 1  # Move both background images back
    bgX2 -= 1

    if bgX < bg.get_width() * -1:  # If our bg is at the -width then reset its position
        bgX = bg.get_width()

    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if event.type == USEREVENT + 1:  # Checks if timer goes off
            speed += 1  # Increases speed

        if event.type == USEREVENT + 2:
            r = random.randrange(0, 2)
            if r == 0:
                obstacles.append(saw(810, 310, 64, 64))
            elif r == 1:
                obstacles.append(spike(810, 0, 48, 310))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if not (runner.jumping):
            runner.jumping = True

    if keys[pygame.K_DOWN]:
        if not (runner.sliding):
            runner.sliding = True
    clock.tick(speed)

