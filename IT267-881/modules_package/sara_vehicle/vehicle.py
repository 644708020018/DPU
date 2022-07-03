class Vehicle:
    def __init__(self,name,wheels,max,vin):
        self.name = name
        self.wheels = wheels
        self._maxspeed = max
        self.__vin = vin

    def set_vin(self,vin):
        self.__vin = vin

    def v_detail(self):
        print('===============================')
        print(f"Name : {self.name}")
        print('===============================')
        print(f"Wheels : {self.wheels}")
        print(f"Max Speed : {self._maxspeed}")
        print(f"Vin : {self.__vin}")
