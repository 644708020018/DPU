a = "My name is John, I am "

age = 36
txt = "We are the\\  so-called \"Vikings\" from the north."
  
print(a.upper())
print(a.lower())
print(a.strip())
print(txt.format(age))

quantity = ''
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)