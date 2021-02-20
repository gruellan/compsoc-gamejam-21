import pygame

HEIGHT = 700
WIDTH = 500


class Sprite(pygame.sprite.Sprite):
    FALL_SPEED = 5
    RISE_SPEED = 10
    time_left_to_rise = 0
    x, y = 120, 50

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("alex.png").convert_alpha()

    def jump(self):
        self.time_left_to_rise = 10

    def update(self):
        if self.time_left_to_rise > 0:
            self.y -= self.RISE_SPEED
            self.time_left_to_rise -= 1
        else:
            self.y += self.FALL_SPEED


def run():
    pygame.init()
    pygame.display.set_caption("LETS GO")
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    done = False
    sprite = Sprite()

    while not done:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sprite.jump()

        sprite.update()
        display.fill((0, 0, 0))
        display.blit(sprite.image, (sprite.x, sprite.y))
        pygame.display.update()


if __name__ == '__main__':
    run()
