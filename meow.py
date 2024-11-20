import pygame
import sys

# Инициализация Pygame
pygame.init()

# Загрузка звука мяуканья
meow_sound = pygame.mixer.Sound("meow.wav")

# Создание окна
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("meow")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # Если нажата клавиша
            meow_sound.play()  # Воспроизводим звук мяуканья