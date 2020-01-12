class FigureColor:

    def __init__(self):
        self._color=None

    @property
    def ColorProperty(self):
        return self._color

    @ColorProperty.setter
    def ColorProperty(self,val):
        self._color=val
