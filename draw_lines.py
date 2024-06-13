import pygame

def generate_lines(window, points_list):
    points_l = int(len(points_list))
    lines_amount = points_l-1
    if lines_amount > 0:    
        for i in range(lines_amount):
            start_pos = (points_list[i]["x"], points_list[i]["y"])
            end_pos = (points_list[i+1]["x"], points_list[i+1]["y"])

            
            if points_list[i+1]["y"] <= 10:
                for i in range(points_l):
                    points_list[i]["y"] += 100
            elif points_list[i+1]["y"] >= 377:
                for i in range(points_l):
                    points_list[i]["y"] -= 100
            elif points_list[i+1]["x"] >= 590:
                for i in range(points_l):
                    points_list[i]["x"] -= 100

            elif points_list[i+1]["cur_difference"] > 0:                
                draw_line(window, (0,255,0), start_pos, end_pos, 4)
            elif points_list[i+1]["cur_difference"] == 0:                
                draw_line(window, (149,255,128), start_pos, end_pos, 4)
            else:
                draw_line(window, (255,0,0), start_pos, end_pos, 4)

def draw_line(surface, color, start_pos, end_pos, width):
    pygame.draw.line(surface, color, start_pos, end_pos, width)