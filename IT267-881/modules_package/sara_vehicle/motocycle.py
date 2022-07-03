from vehicle import Vehicle
class Motocycle(Vehicle):
    def __init__(self, name, wheels, max, vin):
        Vehicle.__init__(self, name, wheels, max, vin)

    def set_cc(self,cc):
        self.cc = cc

    def bike_detail(self):
        self.v_detail()s
        print(f'CC : {self.cc}')

    