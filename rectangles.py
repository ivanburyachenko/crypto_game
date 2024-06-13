import pygame
import texts
import os

frames_list = []

grafic_tab = pygame.Rect(13,13,587,377)

rect1 = pygame.Rect(0,0,832, 10)
rect2 = pygame.Rect(0,0,10, 532)
rect3 = pygame.Rect(0,390,800, 800)
rect4 = pygame.Rect(600, 5, 800, 800)

wait_15 = pygame.Rect(572,459,27,27)
wait_1m = pygame.Rect(572,493,27,27)

buy_button = pygame.Rect(13,403,148,40)
currency_tab = pygame.Rect(170,400,430,43)
summa_tab = pygame.Rect(10,455,294,65)
coefficient_tab = pygame.Rect(315,455,285,65)
history_tab = pygame.Rect(610,10,210,210)
trade_tab = pygame.Rect(610,230,210,290)

button_sell = pygame.Rect(100,180,100,50)

def draw_rectangle(window, color, rectangle, with_text=None, text_space=None, text=None, font=None, font_size=None, text_color=None, with_frame=None, frame_color=None, frame_size=None):
    pygame.draw.rect(window, color, rectangle)
    if with_frame == True:
        if [window, frame_color, (rectangle.left-int(frame_size), rectangle.top-int(frame_size), rectangle.width+int(frame_size), rectangle.height+int(frame_size)), int(frame_size)] in frames_list:
            pass
        else:
            frames_list.append([window, frame_color, (rectangle.left-int(frame_size), rectangle.top-int(frame_size), rectangle.width+int(frame_size), rectangle.height+int(frame_size)), int(frame_size)])
            print(frames_list)
    if with_text == True:
        text_font = pygame.font.Font(font, int(font_size))
        texts.addText(window, (rectangle.x + text_space[0], rectangle.y + text_space[1]), text, text_color, text_font)