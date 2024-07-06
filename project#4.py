#TEXT CALCULATOR
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "ERROR !! Your denominator is zero"
    return x / y
    

while True:
    operation = int(input("Enter any operation you want to do..\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n"))
    
    x = int(input("Enter the first number: "))
    y = int(input("Enter the other number: "))
    
    if operation == 1:
        print(f"{x} + {y} = {add(x, y)}")
    elif operation == 2:
        print(f"{x} - {y} = {subtract(x, y)}")
    elif operation == 3:
        print(f"{x} * {y} = {multiply(x, y)}")
    elif operation == 4:
        print(f"{x} / {y} = {divide(x, y)}")
    else:
        print("Invalid operation")
        continue
    
    more_calc = input("Do you want to continue calculating? (yes/no): ")
    if more_calc.lower() != "yes":
        break

print("Thank You!!..")
