class Car:
    # default constructor
    def __init__(self):
        self.brand = "Toyota"

    # method
    def printBrand(self):
        print(f"Brand: {self.brand}")
   

# create object
myCar = Car()
myCar.printBrand()