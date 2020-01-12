# coding=utf-8
from rect import Rectange

class Square(Rectange):
    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get__type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, side_param):
        """
        Класс должен содержать конструктор по параметрам «сторона» и «цвет».
        """
        self.side = side_param
        super().__init__(color_param, self.side, self.side)

    def __str__(self):
        return '{} {} цвета со стороной {} площадью {}.'.format(
            Square.get_type(),
            self.fc.colorproperty,
            self.side,
            self.s()
        )