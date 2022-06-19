class Coffee_order:
    def __init__(self, menu:str, total:float, customer_name:str, num:int = 1, size:str = 'R', price:float = 0):
        self.menu = menu
        self.total = total
        self.customer_name = customer_name
        self.num = num
        self.size = size
        self.price = price
    def __del__(self):
        print("object was destroyed")