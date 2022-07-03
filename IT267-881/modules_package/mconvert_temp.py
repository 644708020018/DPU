from secrets import choice
from measure import measure

if __name__ == '__main__':
    mobj = measure()
    choice = input ('Choose menu (1: inch, 2:cm): ')
    number = float(input('Enter number'))
    
    if choice == 1:
        print(f'{number} cm = {mobj.cm_inch(number):.2f} inch')
    elif choice == '2':
        print(f'{number} inch = {mobj.inch_cm(number):.2f} cm')
    else:
        print('Chose wrong menu')