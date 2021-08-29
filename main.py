import pygame
import math
import random

# GLOBALS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PXSIZE = 4
WIDTH, HEIGHT = 320 * PXSIZE, 240 * PXSIZE

# INITIALISE PYGAME
pygame.init()
pygame.display.set_caption('Pong!')
pygame.display.set_icon(pygame.image.load('media/icon.png'))
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# font = pygame.font.SysFont('Jetbrains Mono', 30)
random.seed()


class Ball:
    def __init__(self):
        self.img = pygame.image.load('media/ball.png')
        self.img = pygame.transform.scale(self.img, (self.img.get_width() * PXSIZE, self.img.get_height() * PXSIZE))
        self.rect = self.img.get_rect()
        self.dir = math.radians(random.uniform(165, 196))
        # self.dir = math.radians(170)
        self.speed = 8*PXSIZE
        self.rect.center = ((WIDTH - self.rect.width)//2, (HEIGHT - self.rect.height)//2)
        self.truepos = [self.rect.x, self.rect.y]

    def reset_ball(self):

        if random.randint(0, 1):
            self.dir = math.radians(random.uniform(150, 170))
        else:
            self.dir = math.radians(random.uniform(180, 220))

        print(math.degrees(self.dir))
        self.rect.center = ((WIDTH - self.rect.width)//2, (HEIGHT - self.rect.height)//2)
        self.truepos = [self.rect.x, self.rect.y]

    def update(self, p1, p2):
        win.blit(self.img, self.rect)

        dx = self.speed * math.cos(self.dir)
        dy = self.speed * math.sin(self.dir)

        steps = int(abs(dx) + abs(dy))
        for _ in range(0, steps, PXSIZE):
            self.truepos[0] += self.speed * math.cos(self.dir)/steps
            self.truepos[1] -= self.speed * math.sin(self.dir)/steps
            self.rect.topleft = self.truepos[0], self.truepos[1]
            self.bounce(p1, p2)

        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.reset_ball()

    def bounce(self, p1, p2):
        # top and bottom
        if self.rect.y < 0 or self.rect.y > HEIGHT - self.rect.height:
            self.dir *= -1

        # paddles
        if pygame.Rect.colliderect(self.rect, p1.rect) or pygame.Rect.colliderect(self.rect, p2.rect):
            self.dir = math.radians(180) - self.dir

        # if pygame.Rect.colliderect(self.rect, p1.rect):
        #     dy = self.rect.centery - p1.rect.centery
        #     dx = p1.rect.centerx - self.rect.centerx
        #     self.dir = math.atan2(dy, dx)
        #     self.dir += math.radians(180)
        #
        # if pygame.Rect.colliderect(self.rect, p2.rect):
        #     dy = self.rect.centery - p2.rect.centery
        #     dx = p2.rect.centerx - self.rect.centerx
        #     self.dir = math.atan2(dy, dx)
        #     self.dir += math.radians(180)


class Paddle:
    def __init__(self, x):
        self.img = pygame.image.load('media/paddle.png')
        self.img = pygame.transform.scale(self.img, (self.img.get_width() * PXSIZE, self.img.get_height() * PXSIZE))
        self.rect = self.img.get_rect()
        self.speed = 4*PXSIZE
        self.rect.center = (x, HEIGHT//2)

    def update(self, dy):
        win.blit(self.img, self.rect)

        dy = self.speed*dy
        steps = abs(dy)
        for _ in range(0, steps, PXSIZE):
            if 0 < self.rect.y - dy/steps < HEIGHT - self.rect.height:
                self.rect.y -= dy/steps


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
        ball.update(pl_1, pl_2)

        pygame.display.update()

        clock.tick(30)


if __name__ == '__main__':
    main()
