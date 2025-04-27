from color import YELLOW
from finishObject import FinishObject
from polarizer import Polarizer
from mirror import Mirror
from wall import Wall
from math import cos, radians

class Ray:
    
    def __init__(this, start=(0, 0), v_vector=(1,1), width=5, color=YELLOW, I=1):  
        this.start = start
        this.points = [start]
        this.color = color
        this.width = width
        this.v_x, this.v_y = v_vector
        this.finish = False
        this.nextIntensiv_and_angle = None
        this.intensiv_and_angle = [(I, -1)]


    def collision(this, object, screen):
        width, height = screen.get_width(), screen.get_height()
        x, y = this.points[-1]
        if x < 0 or y < 0 or x > width or y > height: # колизия лучей и стен
            this.finish = True
            return 0
        if isinstance(object, Polarizer):
            x, y = this.points[-1]
            x_obj, y_obj = object.x, object.y
            w_obj = object.width
            if x_obj - w_obj < x < x_obj + w_obj and y_obj - w_obj < y < y_obj + w_obj:
                old_intensiv, old_angle = this.intensiv_and_angle[-1]
                new_angle = object.angle
                if old_angle == -1:
                    this.nextIntensiv_and_angle = (old_intensiv / 2, new_angle)    
                else:
                    this.nextIntensiv_and_angle = (old_intensiv * cos(radians(new_angle-old_angle))**2, new_angle)
        if isinstance(object, Mirror):
            dist = object.calculateDistance(this.points[-1])
            if dist < this.width:
                line_vec = (object.x2 - object.x1, object.y2 - object.y1)
                point_vec = (this.points[-1][0] - object.x1, this.points[-1][1] - object.y1)
                line_length = object.length
                proj = (point_vec[0]*line_vec[0] + point_vec[1]*line_vec[1]) / line_length
                if 0 <= proj <= line_length:
                    dot = this.v_x * object.normal[0] + this.v_y * object.normal[1]
                    this.v_x = this.v_x - 2 * dot * object.normal[0]
                    this.v_y = this.v_y - 2 * dot * object.normal[1]
        if isinstance(object, Wall):
            if isinstance(object, Wall):
                x, y = this.points[-1]  # Получаем координаты мячика
                wall_x, wall_y = object.x, object.y  # Получаем координаты верхнего левого угла стены
                wall_w, wall_h = object.w, object.h  # Получаем ширину и высоту стены
                # Проверяем, находится ли мячик внутри стены
                if wall_x <= x <= wall_x + wall_w and wall_y <= y <= wall_y + wall_h:
                    this.finish = True
                    return -1
                
        if isinstance(object, FinishObject):
            x_obj, y_obj = object.x, object.y
            width_obj, height_obj = object.width, object.height
            if x_obj < x < x_obj + width_obj and y_obj < y < y_obj + height_obj:
                this.finish = True
                return 1
                    
                

            
    def tick(this):
        x_now, y_now = this.points[-1]
        this.points.append((x_now+this.v_x, y_now+this.v_y))
        if this.nextIntensiv_and_angle:
            this.intensiv_and_angle.append(this.nextIntensiv_and_angle)
            this.nextIntensiv_and_angle = None
        else:
            this.intensiv_and_angle.append(this.intensiv_and_angle[-1])
        