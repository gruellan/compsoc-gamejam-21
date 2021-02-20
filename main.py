import pygame

HEIGHT = 700
WIDTH = 500


def run():
    pygame.init()
    pygame.display.set_caption("LETS GO")
    pygame.display.set_mode((WIDTH, HEIGHT))
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.display.flip()


if __name__ == '__main__':
    run()
