#print ("Hello word")
#from xmlrpc.client import Boolean
#if Boolean_Expression
#    statemant (s)
#number_1 = int (input("Enter the first Namber"))
#number_2 = int (input("Enter the second Namber"))
#if number_1 > number_2:
#    print (f"{number_1} is greater than {number_2}")
#else:
#    print (f"{number_2} is greater than {number_1}")

score = float(input("Enter your score"))
if score < 0 or score > 100:
    print('Wrong Input')
elif score >= 80:
    print('Your Grade is "A" ')
elif score >= 70:
    print('Your Grade is "B" ') 
elif score >= 60:
    print('Your Grade is "C" ')
elif score >= 50:
    print('Your Grade is "D" ')
else:
    print('Your Grade is "F" ')

