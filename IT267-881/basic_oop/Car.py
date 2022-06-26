class Car:
    brand = "Toyota"

    def __init__(self, model:str, calor:str, year:int, price:int):
        self.model = model
        self.calor = calor
        self.year = year
        self.price = price

    def printcardetail(self):
        print(f"ยี่ห้อ  : {self.brand}")
        print(f"รุ่น  : {self.model}")
        print(f"สี  : {self.calor}")
        print(f"ปี : {self.year}")
        print(f"ราคา  : {self.price:.2f}")

    def __del__(self):
        print("object was destroyed")

if __name__ == "__main__":
    my_car = Car("cross", "white", 2022, 1200000)
    my_car.printcardetail()