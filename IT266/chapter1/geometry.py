PI = 3.14

def circle_area(r=1):
    # print(r)
    radius = (input("Enter the radius of a circle (defualt = 1): "))
    if radius != '':
        r = float(radius)
    area = PI * r * r
    print(f"ผลลัพท์พื้นที่วงกลม คือ = {area}")
    print("\n==========================================")


def circle_line(r=1):
    radius = (input("Enter the radius of a circle (defualt = 1): "))
    if radius != '':
        r = float(radius)
    line = 2 * PI * r
    print(f"ผลลัพท์ความยาวเส้นรอบวง คือ = {line}")
    print("\n==========================================")


def rectangle_area(width=1, length=1):
    side_a = (input("Enter the width (defualt = 1): "))
    side_b = (input("Enter the length (defualt = 1): "))
    if side_a != '' :
        width = float(side_a)
    if side_b != '':
        length = float(side_b) 
    area = width * length
    print(f"ผลลัพท์พื้นที่รูปสี่เหลี่ยม คือ = {area}")
    print("\n==========================================")


def rectangle_line(width=1, length=1):
    side_a = (input("Enter the width (defualt = 1): "))
    side_b = (input("Enter the length (defualt = 1): "))
    if side_a != ''  :
        width = float(side_a)
    if side_b != '':  
        length = float(side_b)
    line = 2 * (width + length)
    print(f"ผลลัพท์ความยาวรอบรูปสี่เหลี่ยม คือ = {line}")
    print("\n==========================================")

def triangle_area(width=1, height=1, base=1):
    side_a = (input("Enter the width (defualt = 1): "))
    side_b = (input("Enter the height (defualt = 1): "))
    side_c = (input("Enter the base (defualt = 1): "))
    if side_a != '' :
        width = float(side_a)
    if side_b != '' :
        height = float(side_b)
    if side_c != '':
        base = float(side_c)
    area = 1/2 * (base + height)
    print(f"ผลลัพท์พื้นที่สามเหลี่ยม คือ = {area}")
    print("\n==========================================")

def triangle_line(width=1, height=1, base=1):
    side_a = (input("Enter the width (defualt = 1): "))
    side_b = (input("Enter the height (defualt = 1): "))
    side_c = (input("Enter the base (defualt = 1): "))
    if side_a != '' :
        width = float(side_a)
    if side_b != '' :
        height = float(side_b)
    if side_c != '':
        base = float(side_c)
    line = (base + height + width)
    print(f"ผลลัพท์ความยาวรอบรูปสามเหลี่ยม คือ = {line}")
    print("\n==========================================")

def math () :
    while True :
        user_input = input("==========================================\n  ออกจากโปรแกรม กด = 0 \n  หาพื้นที่วงกลม กด = 1 \n  หาความยาวเส้นรอบวง กด = 2 \n  หาพื้นที่รูปสี่เหลี่ยม กด = 3 \n  หาความยาวรอบรูปสี่เหลี่ยม กด = 4 \n  หาพื้นที่สามเหลี่ยม กด = 5 \n  หาความยาวรอบรูปสามเหลี่ยม กด = 6 \n==========================================\n  โปรดเลือกหมายเลขฟังก์ชั่นการใช้งาน : ")
        if user_input == "":
            break
        if int (user_input) == 0 :
            break
        elif int (user_input) == 1 :
            print ("Input radius to calcula")
            circle_area ()
        elif int (user_input )== 2 :
            circle_line ()
        elif int (user_input )== 3 :
            rectangle_area ()
        elif int (user_input )== 4 :
            rectangle_line ()
        elif int (user_input )== 5 :
            triangle_area ()
        elif int (user_input )== 6 :
            triangle_line ()
        else :
            print ("เลือกหมายเลขฟังก์ชั่นการใช้งานไม่ถูกต้อง โปรดเลือกอีกครั้ง")

