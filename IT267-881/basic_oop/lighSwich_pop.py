switch_status = False #ฟังก์ชั่นปิดไฟ

def turnOn():
    global switch_status
    switch_status = True
    print ("เปิดไฟ")

def turnOff():
    global switch_status
    switch_status = False
    print ("ปิดไฟ")

if __name__ == "__main__":
    print (f'สถานะไฟ : {switch_status}')
    turnOn()
    turnOff()
    turnOff()
    turnOff()