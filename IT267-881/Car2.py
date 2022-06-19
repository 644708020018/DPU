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

    @staticmethod
    def get_static_method():
        text = "static"
        print(f"IN {text} Method")


    @classmethod  #ต้องมี cls เสมอ
    def get_class_method(cls):
        my_text = "class"
        print(f"This is {my_text} Method")


    def __del__(self):
        print("object was destroyed")

if __name__ == "__main__":
    my_car = Car("cross", "white", 2022, 1200000)
    my_car.printcardetail()

    Car.get_static_method()
    my_car.get_static_method()

    Car.get_class_method()
    my_car.get_class_method()
