import pygame
import random
from PIL import Image, ImageDraw

# Define palette size and base color
width = 500
height = 200
base_color = (255, 255, 255)  # White

# Create image object
img = Image.new('RGB', (width, height), base_color)
draw = ImageDraw.Draw(img)

# Define well size and spacing
well_width = 50
well_height = 30
padding = 10

# Loop to draw colored rectangles for wells (replace colors with your choices)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
x = padding
y = padding
for color in colors:
    draw.rectangle([(x, y), (x + well_width, y + well_height)], fill=color)
    x += well_width + padding

# Display or save the image
img.show()  # This will display the image on your screen
# img.save("palette.png")  # This will save the image as palette.png


# Making canvas
screen = pygame.display.set_mode((900, 700))

# Setting Title
pygame.display.set_caption('Creative / Paint')


draw_on = False
last_pos = (0, 0)


# Color of the Brush
# Radius of the Brush
radius = 10


def roundline(canvas, color, start, end, radius=1):
	Xaxis = end[0]-start[0]
	Yaxis = end[1]-start[1]
	dist = max(abs(Xaxis), abs(Yaxis))
	for i in range(dist):
		x = int(start[0]+float(i)/dist*Xaxis)
		y = int(start[1]+float(i)/dist*Yaxis)
		pygame.draw.circle(canvas, color, (x, y), radius)

try:
	while True:
		e = pygame.event.wait()
		
		if e.type == pygame.QUIT:
			raise StopIteration
			
		if e.type == pygame.MOUSEBUTTONDOWN:		 
			# Selecting random Color Code
			color = (random.randrange(256), random.randrange(
				256), random.randrange(256))
			# Draw a single circle wheneven mouse is clicked down.
			pygame.draw.circle(screen, color, e.pos, radius)
			draw_on = True
		# When mouse button released it will stop drawing 
		if e.type == pygame.MOUSEBUTTONUP:
			draw_on = False
			last_pos = e.pos 
		# It will draw a continuous circle with the help of roundline function. 
		if e.type == pygame.MOUSEMOTION:
			if draw_on:
				pygame.draw.circle(screen, color, e.pos, radius)
				roundline(screen, color, e.pos, last_pos, radius)
			last_pos = e.pos
		pygame.display.flip()

except StopIteration:
	pass

# Quit
pygame.quit()
