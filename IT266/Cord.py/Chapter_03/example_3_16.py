number = int(input("Enter a number"))
even = 0
odd = 0
for i in range(number):
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i
print(f"Sum of Even numbers are {even} and Odd numbers are {odd}")





#def bubble_sort(list_items):
#    for i in range(len(list_items)):
#        for j in range(len(list_items)-i-1):
#            if list_items[j] > list_items[j+1]:
#               temp = list_items[j]
#                list_items[j] = list_items[j+1]
#                list_items[j+1] = temp
#    print(f"The sorted list using Bubble Sort is {list_items}")

def circle_area(r=1):
    area = 3.14 * r * r
    return area

def circle_line(r=1):
    line = 2 * 3.14 * r
    return line

def main () :
    list_items = []
    for i in range(100):
        item = input("Enter list item: ")
        if item == "done":
            break
        list_items.append(float(item))
    print(f"List items are {list_items}")
    print(list_items)
    
    list_circle_area=[]
    list_circle_line=[]

    #ist_circle_area.append(circle_area(list_items))
    #list_circle_line.append(circle_line(list_items))
    

    for idx in list_items:
        list_circle_area.append(float("%.2f" % circle_area(idx)))
        list_circle_line.append(float("%.2f" % circle_line(idx)))
    print (f"{list_circle_area}")
    print (f"{list_circle_line}")
    print (list_circle_area)
    







    

def splitData (ls) :
    ls1 = []
    ls2 = []
    for i in range (len(ls)) :
        if ls [i] & 1 == 0 :
            ls1.append (ls1[1])
        else ls2.append (ls1[i])
    return ls1, ls2
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ans1, ans2 = splitData(a)
print (ans1)
print (ans2)

ตอบ2.6
ตอบ2.7

def manipData(ls) :
    for i in range(len(ls)) :
        _____your code_____
            _____your code_____
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
manipData(a)

ตอบ2.8
ตอบ2.9
ตอบ2.10