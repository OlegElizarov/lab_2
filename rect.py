# coding=utf-8
from shape import Shape
from color import FigureColor

class Rectange(Shape):
    FIGURE_TYPE = "Прямоугольник "

    @classmethod
    def get_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self,color_param,width_param,height_param):
        self.width = width_param
        self.height = height_param
        self.fc = FigureColor()
        self.fc.colorproperty = color_param

    def s(self):
        return self.width*self.height

    def __str__(self):
        return '{}{} цвета шириной {} и высотой {} площадью {}.'.format(
            Rectange.get_type(),
            self.fc.colorproperty,
            self.width,
            self.height,
            self.s()
        )