from math_operation import addittion, subtraction, multiplication, division

def main():
    choice = int(input("Enter choice 1- Addittion , 2- Subtraction, 3- Multiplication, 4- Division: "))
    
    x = float(input("Enter value for first number"))
    
    y = float(input("Enter value for second number"))
    
    if choice == 1:
        print(f"Result of {x} + {y} = {addittion(x,y)}")
    elif choice == 2:
        print(f"Result of {x} - {y} = {subtraction(x,y)}")
    elif choice == 3:
        print(f"Result of {x} * {y} = {multiplication(x,y)}")
    elif choice == 4:
        print(f"Result of {x} / {y} = {division(x,y)}")
    else:
        print("Invalid choice")

main()

    
    
    