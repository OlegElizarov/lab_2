# coding=utf-8
from shape import Shape
import math
from color import FigureColor

class Circle(Shape):
    FIGURE_TYPE = "Круг"

    @classmethod
    def get__type(cls):
        return cls.FIGURE_TYPE


    def __init__(self,color_param,rad):
        self.fc=FigureColor()
        self.fc.ColorProperty=color_param
        self.r=rad

    def s(self):
        return math.pi*self.r*self.r

    def __str__(self):
        return '{} {} цвета со радиусом {} площадью {}.'.format(
            Circle.get__type(),
            self.fc.ColorProperty,
            self.r,
            self.s()
        )