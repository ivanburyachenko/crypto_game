import pygame

pygame.init()

font40 = pygame.font.Font(None, 40)
font60 = pygame.font.Font(None, 60)

def addText(screen, spacer, text, color, font):
    text_render = font.render(text, True, color)
    screen.blit(text_render, spacer)