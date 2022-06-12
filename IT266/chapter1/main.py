#นายสราวุธ ด่านกลาง   644708020018
#นายปรัชญา  สารทิม    644708020019

PI=3.14
def circle_area(r=1):
    area = PI * r ** 2
    return area

def circle_line(r=1):
    line = 2 * PI * r
    return line

def main () :
    list_items = []
    while True :
        item = input("Enter list item: ")
        if item == "done":
            break
        list_items.append(float(item))

    list_circle_area=[]
    list_circle_line=[]

    for idx in list_items:
        list_circle_area.append(float("%.2f" % circle_area(idx)))
        list_circle_line.append(float("%.2f" % circle_line(idx)))
        average1 = sum(list_circle_area)/len(list_circle_area)
        average2 = sum(list_circle_line)/len(list_circle_line)
    print (f"ผลลัพท์พื้นที่วงกลม คือ =  {list_circle_area}")
    print("ค่า min พื้นที่วงกลม คือ =", min(list_circle_area))
    print ("ค่า max พื้นที่วงกลม คือ =", max(list_circle_area))
    print(f"ค่าเฉลี่ย พื้นที่วงกลม คือ = {average1}")
    print (f"ผลลัพท์ความยาวเส้นรอบวง คือ = {list_circle_line}")
    print("ค่า min เส้นรอบวง คือ =", min(list_circle_line))
    print ("ค่า max เส้นรอบวง คือ =", max(list_circle_line))
    print(f"ค่าเฉลี่ย เส้นรอบวง คือ = {average2}")

if __name__ == "__main__":
    main()