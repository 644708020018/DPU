from list1 import main


if __name__ == "__main__":
    main()

def main () :
    list_items = []
    for i in range(100):
        item = input("Enter list item: ")
        if item == "done":
            break
        list_items.append(float(item))

    list_circle_area=[]
    list_circle_line=[]

    for idx in list_items:
        list_circle_area.append(float("%.2f" % circle_area(idx)))
        list_circle_line.append(float("%.2f" % circle_line(idx)))
    print (f"ผลลัพท์พื้นที่วงกลม คือ =  {list_circle_area}")
    print (f"ผลลัพท์ความยาวเส้นรอบวง คือ = {list_circle_line}")

if __name__ == "__main__":
    main()