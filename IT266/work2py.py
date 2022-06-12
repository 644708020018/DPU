PI = 3.14

def circle_area(r=1):
    # print(r)
    radius = (input("Enter the radius of a circle (defualt = 1):"))
    if radius != '':
        r = float(radius)
    area = PI * r * r
    print("Area of a circle = %.2f" % area)


def circle_line(r=1):
    radius = (input("Enter the radius of a circle (defualt = 1):"))
    if radius != '':
        r = float(radius)
    line = 2 * PI * r
    print("Circumference of a circle = %.2f" % line)


def rectangle_area(width=1, length=1):
    side_a = (input("Enter the width (defualt = 1):"))
    side_b = (input("Enter the length (defualt = 1):"))
    if side_a != '' :
        width = float(side_a)
    if side_b != '':
        length = float(side_b) 
    area = width * length
    print("Area of a rectangle = %.2f" % area)


def rectangle_line(width=1, length=1):
    side_a = (input("Enter the width (defualt = 1):"))
    side_b = (input("Enter the length (defualt = 1):"))
    if side_a != ''  :
        width = float(side_a)
    if side_b != '':  
        length = float(side_b)
    line = 2 * (width + length)
    print("Perimeter of a rectangle = %.2f" % line)

def triangle_area(width=1, height=1, base=1):
    side_a = (input("Enter the width (defualt = 1):"))
    side_b = (input("Enter the height (defualt = 1):"))
    side_c = (input("Enter the base (defualt = 1):"))
    if side_a != '' :
        width = float(side_a)
    if side_b != '' :
        height = float(side_b)
    if side_c != '':
        base = float(side_c)
    area = 1/2 * (base + height)
    print("Area of a triangle = %.2f" % area)

def triangle_line(width=1, height=1, base=1):
    side_a = (input("Enter the width (defualt = 1):"))
    side_b = (input("Enter the height (defualt = 1):"))
    side_c = (input("Enter the base (defualt = 1):"))
    if side_a != '' :
        width = float(side_a)
    if side_b != '' :
        height = float(side_b)
    if side_c != '':
        base = float(side_c)
    line = (base + height + width)
    print("Perimeter of a triangle = %.2f" % line)

def main_p (c) :
    #while c<10 :
    if c < 10:
        user_input = int (input("โปรดเลือกหมายเลขฟังก์ชั่นการใช้งาน : "))
        if user_input == 0 :
            #break
            pass
        elif user_input == 1 :
            print ("Input radius to calcula")
            circle_area ()
        elif user_input == 2 :
            circle_line ()
        elif user_input == 3 :
            rectangle_area ()
        elif user_input == 4 :
            rectangle_line ()
        elif user_input == 5 :
            triangle_area ()
        elif user_input == 6 :
            triangle_line ()
        else :
            print ("Please Input function Number")


