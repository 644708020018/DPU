# person.py
class Person:
    # parameterized constructor
    def __init__(self, name, gender, profession):
        # data members (instance attributes)
        self.name = name
        self.gender = gender
        self.profession = profession

    # Behavior (instance methods)
    def show(self):
        print(f'Name: {self.name} Sex: {self.gender} Profession: {self.profession}')

    # Behavior (instance methods)
    def work(self):
        print(f'{self.name} working as a {self.profession}')
   
    # Deconstructor
    def __del__(self):
        print("Object was destroyed")

# create the object of a Person class
jessa = Person('Jessa', 'Female', 'Software Engineer')
jessa.show()
jessa.work()