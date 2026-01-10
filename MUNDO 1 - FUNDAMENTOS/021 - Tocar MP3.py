import pygame
pygame.init()
try:
    pygame.mixer.music.load('MP3')
    pygame.mixer.music.play()
    input("Tocando... Aperte Enter para parar.")
except pygame.error as e:
    print(f"Ocorreu um erro ao tentar tocar: {e}")
