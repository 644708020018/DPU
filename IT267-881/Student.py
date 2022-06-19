class Student:
    def __init__(self, id:int, name:str, major:str):
        self.id = id
        self.name = name
        self.major = major

    def display_detail(self):
        print(f"id  : {self.id}")
        print(f"name  : {self.name}")
        print(f"major  : {self.major}")

    def __del__(self):
        print("object was destroyed")

if __name__ == "__main__":
    my_student = Student(111, "Jessica", "IT")
    my_student.display_detail()

    my_student = Student(112, "John", "MKT")
    my_student.display_detail()
