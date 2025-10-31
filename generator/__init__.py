from random import randint, normalvariate, uniform
import numpy as np
from wall import Wall


class Generator:
    def __init__(this, width, height, level=6):
        this.heigth = height
        this.width = width
        this.level = level
    
    def generate_mirror_point(this):
        if randint(1, 1000) % 17 == 0:
            this.level = 10    
        this.level = randint(2, 4) 
        points = np.linspace(0, this.width, this.level)
        sigma = this.width / ((4 * (this.level - 1))*2)
        x_points = [normalvariate(p, sigma) for p in points]
        y_points = [uniform(0, this.heigth) for _ in range(this.level)]

        rez = []
        for x, y in zip(x_points[1:-1], y_points[1:-1]):
            if 0 <= x <= this.width and 0 <= y <= this.heigth:
                rez.append( (x,y) ) 
        return rez
    
    def generate_walls(this):
        points = this.generate_mirror_point()
        walls = []
        for point in points:
            wall_width = uniform(10, 30)
            delata = normalvariate(200, 30)
            walls.append( Wall(point[0], 0, wall_width, point[1] - delata) )
            walls.append( Wall(point[0], point[1]+(delata), wall_width, this.heigth) )
        if len(walls) <= 2:
            print(walls)
            return this.generate_walls()
        return walls, (randint(1, 3), randint(1, 2))