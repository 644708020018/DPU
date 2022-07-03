import re
from time import timezone


class Geographic:
    def setcordinate(self,lat,long):
        self.latitude = lat
        self.longitude = long

    def getcordinate(self):
        return f'Latitude: {self.latitude}\nLongitude: {self.longitude}'

    def gettimezone(self):
        timezone = round(self.longitude/12 -1)
        if timezone > 0:
            return f'Timezone+{timezone}' #timezone +7
        else:
            return f'Timezone{timezone}' #timezone -12
    
    def gatclimate(self):
        if self.latitude <= -66.5 or self.latitude >= 66.5:
            return 'Polar Zone'
        elif self.latitude <= -23.5 or self.latitude >= 23.5:
            return 'Temperate Zone'
        else:
            return 'Tropical Zone'
            