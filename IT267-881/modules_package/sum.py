class Sum:
    def sum(self,a,b,c = 0):
        s = a + b + c
        return s


sobj = Sum()
#calling method with 2 args
sum = sobj.sum(2,3)
print(f"Sum = {sum}")

#calling method with 3 args
sum = sobj.sum(2,3,5)
print(f"Sum = {sum}")