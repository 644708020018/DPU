class Person:
    def __init__(self, name, gender, profession):
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study = 0

    def work(self):
        print(f'{self.name} working as a {self.profession}')

    def study(self,hours):
        self.study = hours

    def show(self):
        print(f'Name: {self.name} Gender: {self.gender} profession: {self.profession} study: {self.study}')

    #person1
jessa = Person('Jessa', 'Female', 'Software Engineer')
jessa.show()
jessa.work()