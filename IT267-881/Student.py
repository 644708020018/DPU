from xml.etree.ElementInclude import default_loader


class Student:
    def __init__(self, id:int, name:str, major:str):
        self.id = id
        self.name = name
        self.major = major

    def display_detail(self):
        print(f"id  : {self.id}")
        print(f"name  : {self.name}")
        print(f"major  : {self.major} \n")

    #def __del__(self):
        #print("object was destroyed")

if __name__ == "__main__":
    Jessica = Student(111, "Jessica", "IT")
    Jessica.display_detail()

    john = Student(112, "John", "MKT")
    john.display_detail()

    jame = Student(113, "jame", "acc")
    jame.display_detail()