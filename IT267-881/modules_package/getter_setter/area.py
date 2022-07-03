class Area:
    def __init__(self,base=1,high=1):
        self.__base = base
        self.__high = high
        
    @property #getter ของ base
    def base(self):
        return self.__base

    #setter ของ base
    @base.setter
    def base(self,value):
        self.__base = value
        
    #getter ของ high
    @base.setter
    def high(self,value):
        self.__high = value #self.hihg = value
        
    def compute_area(self):
        return 0.5 * self.base * self.high