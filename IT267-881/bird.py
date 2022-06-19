class Bird:  
    global bird_type #ถ้าไม่ใส่ Global จะกลายเป้น Class class variable 
    bird_type = "parrot"
    bird_name = "lola"

    def __init__(self,color):
        self.color = color
        name = "Peter"
        print(f'{name} in init')

if __name__ == "__main__":
    my_bird = Bird('Green, Blue')

#call Instance variable
    print(my_bird.color)
#เรียกใช้ Class Variable
    print(my_bird.bird_name)
#เรียกใช้ Globle
    print(bird_type)