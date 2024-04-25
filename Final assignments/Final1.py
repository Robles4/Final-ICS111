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
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    pygame.draw.line(canvas, (0, 0, 0), (event.pos[0], event.pos[1]), (event.pos[0], event.pos[1]), 1)

        window.fill((255, 255, 255))
        window.blit(canvas, (0, 0))
        pygame.display.flip()

        clock.tick(60)
        
if __name__ == "__main__":
    main()  