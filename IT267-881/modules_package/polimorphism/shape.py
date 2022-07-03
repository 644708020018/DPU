class Shape:
    def __init__(self,shape,area):
        self.__shape = shape
        self.__area = 0

    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def sheape(self,shape):
        self.shape = shape

    @property
    def area(self):
        return self.__area

    def area(self,area):
        self.area = area

    def compute_area(self):
        pass

    