from cafe_modules import Desserts
from cafe_modules import Drinks
#samble_1
desserts = Desserts()
print('เมนูอาหาร')
print (desserts.show_desserts())
print('\n')

#samble_2
from cafe_modules import Desserts,Drinks
drinks = Drinks()
print('เมนูเครื่องดื่ม')
print (drinks.show_drinks())
drinks.add_drinks('สมุทตี้')

print (drinks.show_drinks())
drinks.add_drinks('น้ำส้ม')

print (drinks.show_drinks())
drinks.add_drinks('กาแฟ')