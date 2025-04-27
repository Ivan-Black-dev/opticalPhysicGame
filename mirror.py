import math
import color

class Mirror:
    def __init__(this, x1, y1, x2, y2, color=color.WHITE):
        this.x1, this.y1 = x1, y1
        this.x2, this.y2 = x2, y2
        this.length = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        this.color = color
        
        # Вычисляем нормаль (перпендикуляр)
        dx, dy = x2 - x1, y2 - y1
        this.normal = (-dy, dx)  # Перпендикулярный вектор
        # Нормализуем нормаль
        norm_length = math.sqrt(this.normal[0]**2 + this.normal[1]**2)
        this.normal = (this.normal[0]/norm_length, this.normal[1]/norm_length)

    def calculateDistance(this, point):
        x, y = point
        A = this.y2 - this.y1
        B = this.x1 - this.x2
        C = this.x2 * this.y1 - this.x1 * this.y2
        return abs(A*x + B*y + C) / math.sqrt(A**2 + B**2)