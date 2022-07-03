import re
from sunau import Au_read
from unicodedata import name
from geographic import Geographic
from temperature import Temperature

class Country(Geographic,Temperature):
    def __init__(self,name,area,pop):
        super().__init__()
        Geographic.__init__(self)
        Temperature.__init__(self)
        self.name = name
        self.area = area
        self.population = pop

def getpopulation_density(self):
    return self.population / self.area

def show_detail(self):
    print (f'Contry : {self.name}')
    print (self.getcordinate())
    print(f'Area: {self.area}')
    print(f'Population: {self.population} Million')
    print(f'Density: {self.getpopulation_density()}')
    
    #Time Zone,
    print (f'Time Zone: {self.gettimezone()}')
    print (f'Climate: {self.gatclimate()}')
    print (f'Temperature(C): {self.celsius}')
    print (f'Temperature(F): {self.getfahrenheit()}')
    print (f'Weather: {self.getweather()}')

