import pygame
import binance_api
import rectangles
import settings
import graph

def events(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            mouse_position = pygame.mouse.get_pos()
            if rectangles.buy_button.collidepoint(mouse_position):
                print("button_buy")
                # print(binance_api.make_request())
            if rectangles.button_sell.collidepoint(mouse_position):
                print("button_sell")
            
