class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.area = 0

    def computber_area(self):
        self.area = self.width * self.length

    def print_area(self):
        print (f'Rectangle area = {self.area}')
#rec = Restart()

if __name__ == "__main__":
    rec = Rectangle(2,5)
    rec.computber_area()
    rec.print_area()

