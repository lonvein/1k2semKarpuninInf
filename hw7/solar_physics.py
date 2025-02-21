from random import randint
import numpy as np
gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""

class Star():
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    type = "star"
    """Признак объекта звезды"""

    m = 0
    """Масса звезды"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус звезды"""

    color = "red"
    """Цвет звезды"""

    image = None
    """Изображение звезды"""


class Planet():
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    m = 0
    """Масса планеты"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус планеты"""

    color = "green"
    """Цвет планеты"""

    image = None
    """Изображение планеты"""
    
    
def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """
    xx = 0
    yy = 0
    body.Fx = 0
    body.Fy = 0
    for i in space_objects:
        if body!=i:
            xx = body.x - i.x 
            yy = body.y - i.y
            R = np.sqrt(xx*xx + yy*yy)
            F = body.m * i.m * gravitational_constant / (R*R)
            try:
                ug = np.arctan(yy/xx)
                body.Fx += -(xx /abs(xx)) * F * abs(np.cos(ug))
                body.Fy += -(yy/abs(yy)) * F * abs(np.sin(ug))
            except:
                if yy == 0:
                    if xx > 0:
                        body.Fx += -F
                    elif xx < 0:
                        body.Fx += F
                if xx == 0:
                    if yy > 0:
                        body.Fy += -F
                    elif yy < 0:
                        body.Fy += F
            w = np.sqrt(body.Vx ** 2 + body.Vy ** 2) / R #угловая скорость
            
            
            
    

def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx/body.m
    body.x += body.Vx*dt + ((dt**2)*ax)/2
    body.Vx += ax*dt
    ay = body.Fy/body.m
    body.y += body.Vy*dt + ((dt**2)*ay)/2
    body.Vy += ay*dt
    
    


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")