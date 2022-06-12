class Switch():
    def __init__(self):
        self.switch_status = False

    def turnOn(self):
        self.switch_status = True

    def turnOff(self):
        self.switch_status = False

    def show_status(self):
        if (self.switch_status):
            print ("ไฟเปิด")
        else:
            print ("ไฟปิด")
sobj = Switch()

if __name__ == "__main__":
    sobj.show_status()
    sobj.turnOn()
    sobj.show_status()
    sobj.turnOff()
    sobj.show_status()
    sobj.turnOff()
    sobj.show_status()
    sobj.turnOff()
    sobj.show_status()
    sobj.turnOff()
    sobj.show_status()