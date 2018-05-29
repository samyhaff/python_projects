import pygame
from pygame.locals import *
 
pygame.init()
 
fenetre = pygame.display.set_mode((1366, 768))
 
font=pygame.font.Font(None, 24)
text = font.render(Texte,1,(255,255,255))
 
continuer = 1
 
while continuer:
 
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
 
    fenetre.blit(text, (300, 300))
 
    pygame.display.flip()
 
pygame.quit()
