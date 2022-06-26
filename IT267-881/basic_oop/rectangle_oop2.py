from turtle import width


class Rectangle:
    def __init__(self):
        self.width = 0
        self.length = 0
        self.area = 0

    def get_data(self):
        self.width = float(input('Enter width: '))
        self.length = float(input('Enter length: '))
        #self.area = input (int('area: '))

    def computber_area(self):
        self.area = self.width * self.length

    def print_area(self):
        print (f'Rectangle area = {self.area}')
#rec = Restart()

if __name__ == "__main__":
    rec = Rectangle()
    rec.get_data()
    rec.computber_area()
    rec.print_area()