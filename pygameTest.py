import pygame
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Test Window")
 
done = False

#refresh rate 
clock = pygame.time.Clock()
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    for i in range(200):
        radians_x = i / 20
        radians_y = i / 6
        x = int(75 * math.sin(radians_x)) + 200
        y = int(75 * math.cos(radians_y)) + 200
        pygame.draw.line(screen, BLACK, [x,y], [x+5,y], 5)

    for x_offset in range(30, 300, 30):
        pygame.draw.line(screen,BLACK,[x_offset,100],[x_offset-10,90],2)
        pygame.draw.line(screen,BLACK,[x_offset,90],[x_offset-10,100],2)

    pygame.draw.rect(screen,BLACK,[20,20,250,100],2)

    pygame.display.flip()
 
    #60 fps
    clock.tick(60)

pygame.quit()


