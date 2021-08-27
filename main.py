import pygame
import math

# GLOBALS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PXSIZE = 2
WIDTH, HEIGHT = 512 * PXSIZE, 256 * PXSIZE

# INITIALISE PYGAME
pygame.init()
pygame.display.set_caption('Pong!')
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Jetbrains Mono', 30)


class Ball:
    def __init__(self):
        self.img = pygame.image.load('media/ball.png')
        self.img = pygame.transform.scale(self.img, (self.img.get_width() * PXSIZE, self.img.get_height() * PXSIZE))
        self.dir = math.radians(120)
        self.speed = 4*PXSIZE
        self.x, self.y = WIDTH//2 + 200, HEIGHT//2

    def update(self):
        win.blit(self.img, (self.x, self.y))
        self.x += self.speed * math.cos(self.dir)
        self.y -= self.speed * math.sin(self.dir)

    def bounce(self):
        if self.y <= 0 or self.y >= HEIGHT - self.img.get_height():
            self.dir *= -1

        # if self.x


class Paddle:
    def __init__(self, x):
        self.img = pygame.image.load('media/paddle.png')
        self.img = pygame.transform.scale(self.img, (self.img.get_width() * PXSIZE, self.img.get_height() * PXSIZE))
        self.speed = 4*PXSIZE
        self.x = x
        self.y = HEIGHT//2 + self.img.get_height()//2

    def update(self, dy):
        win.blit(self.img, (self.x, self.y))
        if 0 < self.y - self.speed*dy < HEIGHT - self.img.get_height():
            self.y -= self.speed*dy


def main():
    pl_1 = Paddle(32 * PXSIZE)
    pl_2 = Paddle(WIDTH-32 * PXSIZE)
    ball = Ball()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pressed = pygame.key.get_pressed()

        win.fill(BLACK)
        pl_1.update(pressed[pygame.K_w]-pressed[pygame.K_s])
        pl_2.update(pressed[pygame.K_UP]-pressed[pygame.K_DOWN])
        ball.bounce()
        ball.update()

        pygame.display.update()

        clock.tick(30)


if __name__ == '__main__':
    main()
