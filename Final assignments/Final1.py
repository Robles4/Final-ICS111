import pygame
import random

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("MS Paint Challenge")
active_size = 0
active_color = 'white'

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Objects to draw
OBJECTS = ["circle", "square", "triangle", "paddle", "star", "heart", "moon", 
           "earth", "hunky Hawai3ian man", "santa", "snowflake", "rainbow",
           "a bee", "octagon", "Hawaii island", "a laptop", "heart"]


# Define the main game loop
def main():
    # Game loop variables
    running = True
    drawing = False
    canvas = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    canvas.fill(WHITE)
    clock = pygame.time.Clock()
    time_remaining = 1000  # Initial time limit (in seconds)
    current_object = random.choice(OBJECTS)  # Choose a random object to draw
    selected_color = random.choice([RED, GREEN, BLUE, BLACK])  # Choose a random color
   
    # Font for displaying text
    font = pygame.font.Font(None, 36)
   
    # Main game loop
    while running:
        # Handle events
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
                    pygame.draw.circle(canvas, selected_color, (x, y), 5)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: 
                    canvas.fill(WHITE)
                elif event.key == pygame.K_c: 
                    selected_color = random.choice([BLACK, RED, GREEN, BLUE])
       
        window.fill(WHITE)
        window.blit(canvas, (0, 0))
       
        timer_text = font.render("Time: {}s".format(time_remaining), True, BLACK)
        window.blit(timer_text, (10, 10))
       
        object_text = font.render("Draw {}".format(current_object), True, BLACK)
        window.blit(object_text, (10, 50))
       
        color_text = font.render("Color: {}".format(selected_color), True, selected_color)
        window.blit(color_text, (10, 90))
       
        pygame.display.flip()
       
        # Update timer
        if time_remaining > 0:
            time_remaining -= 1
        else:
            # Time's up, reset the timer and choose a new object to draw
            time_remaining = 5000
            current_object = random.choice(OBJECTS)
            canvas.fill(WHITE)
       
        # Cap the frame rate
        clock.tick(1000)

    pygame.display.flip()

# Run the game
if __name__ == "__main__":
    main()