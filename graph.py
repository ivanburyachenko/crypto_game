import pygame

def restart_list(points_list, currency):
    points_list.clear()
    point_start = {
        "x" : 15,
        "y" : 202,
        "currency" : currency,
        "cur_difference": 0
    }
    points_list.append(point_start)
    return points_list