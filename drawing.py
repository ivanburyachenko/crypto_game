import pygame
import rectangles
import draw_lines

def drawing(window, currency=None, points_list=None):
    window.fill((50, 50, 50))
    rectangles.draw_rectangle(window, (155,155,155), rectangles.grafic_tab, False, with_frame=True, frame_color=(105,105,105), frame_size=3)
    draw_lines.generate_lines(window, points_list)

    rectangles.draw_rectangle(window, (50,50,50), rectangles.rect1, False)
    rectangles.draw_rectangle(window, (50,50,50), rectangles.rect2, False)
    rectangles.draw_rectangle(window, (50,50,50), rectangles.rect3, False)
    rectangles.draw_rectangle(window, (50,50,50), rectangles.rect4, False)

    rectangles.draw_rectangle(window, (20,255,100), rectangles.buy_button, True, (40, 8), "BUY", None, 40, (0,0,0), True, (100,150,100), 3)
    rectangles.draw_rectangle(window, (100, 100, 100), rectangles.currency_tab, True, (30, 10), f"CURRENCY             {currency}", None, 35, (0,0,0))
    rectangles.draw_rectangle(window, (100, 100, 100), rectangles.summa_tab, False)
    rectangles.draw_rectangle(window, (100, 100, 100), rectangles.coefficient_tab, False)
    rectangles.draw_rectangle(window, (150, 150, 150), rectangles.wait_15, True, (0, 3), "15s", None, 23, (0,0,0), True, (80, 80, 80), 3)
    rectangles.draw_rectangle(window, (150, 150, 150), rectangles.wait_1m, True, (0, 3), "1m", None, 25, (0,0,0), True, (80, 80, 80), 3)
    rectangles.draw_rectangle(window, (100, 100, 100), rectangles.history_tab, False)    
    rectangles.draw_rectangle(window, (100, 100, 100), rectangles.trade_tab, False)
    for element in rectangles.frames_list:
        pygame.draw.rect(element[0], element[1], element[2], element[3])
        
