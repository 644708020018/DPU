print("Only ''stop'' argument value specified in range function")
for i in range(3):
    print(f"{i}")
print("Both ''start'' and ''stop'' argument values specified in range function")
for i in range(2, 5):
    print(f"{i}")
print("All three arguments ''start'', ''stop'' and ''step'' specified in range function")
for i in range(1, 6, 3):
    print(f"{i}")


number = int(input("Enter a number"))
even = 0
odd = 0
for i in range(number):
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i
print(f"Sum of Even numbers are {even} and Odd numbers are {odd}")

