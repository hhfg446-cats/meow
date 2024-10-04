import pygame
import sys

pygame.init()

meow_sound = pygame.mixer.Sound("meow.wav")

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("meow")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            meow_sound.play()