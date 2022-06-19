#animal.py
class Animal:
    animal = "Dog"

    def newAnimal (self, name, breed, colour, age):
        self.name = name
        self.breed = breed
        self.colour = colour
        self.age = age

    def printDetail(self):
        print(f"Breed = {self.breed}\nColour = {self.colour}\nAge = {self.age} year(s)")

ula = Animal()

print(f"Accessing class variable using class name: {Animal.animal}")
ula.newAnimal("Ula","Scottish Fold","Pure white", 1)
print (f"{ula.name} is a {ula.animal}")
ula.printDetail()