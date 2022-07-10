class Horse:
    max_height = 200
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def run(self):
        return self.name + "is running"

    def show_name(self):
        return self.name

    def show_info(self):
        print(f"Name : {self.name}")
        print(f"Color : {self.color}")
        print(f"Max Height : {self.max_height}")

