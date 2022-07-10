class Donkey:
    def __init__(self,age:str,weight):
        self.age = age
        self.weight = weight

    def sound(self):
        print (f"Donkey makes eeyore sound")

    def show_info(self):
        print(f"Age : {self.age}")
        print(f"Weight : {self.weight}")

