import pygame
import rectangles
import events
import binance_api
import drawing
import draw_lines
import settings
import graph

pygame.init()

window = pygame.display.set_mode((832, 532), vsync=True)
pygame.display.set_caption("Crypto Simulator")

time_game = pygame.time.Clock()


currency = binance_api.make_request()
timer_15 = settings.settings["wait_time"]

points_list = []


graph.restart_list(points_list, currency)

run = True
while run:
    timer_15 -= 1
    if timer_15 <= 0:
        currency = binance_api.make_request()
        old_currency = points_list[-1]["currency"]
        cur_difference = currency - old_currency
        next_point = {
            "x" : points_list[-1]["x"] + settings.settings["p_x"],
            "y" : points_list[-1]["y"] - cur_difference * settings.settings["p_y"],
            "currency" : currency,
            "cur_difference": cur_difference
        }        
        points_list.append(next_point)
        print(f"Точка создана | Количество точек: {len(points_list)} | Скачок с прошлым: {cur_difference} | Денежные показатели: {old_currency, currency} | Координаты точки: {next_point['x'], next_point['y']}")
        timer_15 = settings.settings["wait_time"]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_position = pygame.mouse.get_pos()
                if rectangles.wait_15.collidepoint(mouse_position):
                    settings.settings["wait_time"] = 900
                    settings.settings["p_x"] = 20
                    settings.settings["p_y"] = 4
                    graph.restart_list(points_list, currency)
                    print(settings.settings)
                if rectangles.wait_1m.collidepoint(mouse_position):
                    settings.settings["wait_time"] = 3600
                    settings.settings["p_x"] = 10
                    settings.settings["p_y"] = 2
                    graph.restart_list(points_list, currency)
                    print(settings.settings)
        events.events(event)

    drawing.drawing(window, currency, points_list)

    pygame.display.flip()
    time_game.tick(60)
