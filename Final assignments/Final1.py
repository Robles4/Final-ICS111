import pygame
import random

pygame.init()

window_height = 800
window_width = 800
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Paint Rush // Racing mode / Paint")

def main():
    running = True
    drawing = False
    canvas = pygame.Surface((window_width, window_height))
    canvas.fill((255, 255, 255))
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
            elif event.type == pygame.MOUSEMOTION:
                if drawing:
                    x, y = event.pos
                    pygame.draw.circle(canvas, (0, 0, 0), (x, y), 5)

        window.fill((255, 255, 255))
        window.blit(canvas, (0, 0))
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()  