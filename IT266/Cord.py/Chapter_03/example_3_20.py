import math

def circle(radius):
    area = math.pi * radius**2
    circumfarence = 2 * math.pi * radius
    return area, circumfarence

def square(h):
    area = h**2
    circumference = h * 4
    return area, circumference

def main() :
    r = int(input("Enter radius : "))
    area_of_circle, circum_of_circle = circle(r)
    print (area_of_circle)
    print (circle_of_circle)

    h = int (input ("Enter side:"))
    area_of_square

if__name__=="__main__":
    main()
