class Customer:
    def __init__(self):
        self.name = ''
        self.address = ''
        self.phone = ''

    def new_customer(self):
        self.name = input ('Enter Yous Name :  ')
        self.address = input ('Enter Yous address :  ')
        self.phone = input ('Enter Yous phone :  ')

    def customer_info(self):
        return f'\nYous Name : {self.name} \nYous address : {self.address}\nYous phone : {self.phone}'


