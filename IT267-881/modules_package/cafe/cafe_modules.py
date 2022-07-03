from hmac import new


class Desserts:
    def __init__(self):
        self.desserts = ['ข้าวเหนียวมะม่วง','ข้าวเหนียวทุเรียน','ไอศครีม']

    def show_desserts(self):
        return f'Desserts Menu: {self.desserts}'

class Drinks:
    def __init__(self):
        self.drinks = ['ชา','กาแฟ','น้ำอััดลม','ไวน์']
    
    def add_drinks(self,new_drinks):
        self.drinks.append(new_drinks)
    
    def show_drinks(self):
        return f'drinks Menu: {self.drinks}'


    
