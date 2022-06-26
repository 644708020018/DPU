class Item:
    def __init__(self, name:str, price:float, quantity = 1 ):
        assert price > 0,f"price {price} Must greater than 0"
        assert quantity > 0,f"quantity {quantity} Must greater than 0"
       
        self.name = name
        self.price = price
        self.quantity = quantity

# จะเรียกใช้ Method นี้ได้จะต้องมีดารสร้าง object
    def total_price(self):
        return self.price * self.quantity

    def __del__(self):
        print("object was destroyed")

if __name__ == "__main__":
    item1 = Item("Monitor", 5000)
    item2 = Item("Mouse", 1500,2)
    print("=== Total price ==")
    print(f"{item1.name}  : {item1.total_price():.2f}")
    print(f"{item2.name}  : {item2.total_price():.2f}")



