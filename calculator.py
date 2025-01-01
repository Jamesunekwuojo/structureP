

"""
pseudocode

step 1: Define a function to  declare two variables a and b and  allow dynamic input by uses


step 2: Create functions called: addittion, multiplication, division, and subtraction  to perform any of the arithmetic operation

step 3: Crete a memo and ask user to choose operation to perform.

1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division

step 4 : Print out result

step 5: Create variable 'repeat_operation' and assign it a boolean value of 'false'

step 6: Create another variable named controller_operation  and dynamically assign a value of '1' or '0', Asking "Do you want to perform another operation? (yes/no) yes- press 1, No- press 0"

step 7: if controller_operation is equal to 1 then repeat_operation is set to true, 

ELSE IF repeat_operation is set to false
ELSE print "Enter a valid number " and end the program

step 8: while repeat_operation is equal to true repeat the following steps; 1 to 4.

step 9: while repeat_operation is equal to false print "Thank you for using our calculator" and end the program

"""



# Python code to implement the above pseudocode

# Variable declaration function
def variable_declaration():
    global a, b
    a = int(input("Enter first integer: "))
    b = int(input("Enter second integer: "))

# Functions for arithemetic operation
def addition():
    sum = a + b
    print(f"Sum of {a} and {b} is {sum}")
    return sum

def subtraction():
    difference = a - b
    print(f"Difference of {a} and {b} is {difference}")
    return difference

def multiplication():
    product = a * b
    print(f"Product of {a} and {b} is {product}")
    return product

def division():
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    result = a / b
    print(f"Division of {a} and {b} is {result}")
    return result


# Function to choose operation
def choose_operation():
    print("Operations to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice (1, 2, 3, 4): "))

    if choice == 1:
        addition()
    elif choice == 2:
        subtraction()
    elif choice == 3:
        multiplication()
    elif choice == 4:
        division()
    else:
        print("Invalid choice")

# Where Main program starts from
print("Welcome to AUL Calculator App!")
repeat_operation = True

# For loop to repeat the operation
while repeat_operation:
    variable_declaration()
    choose_operation()
    controller_operation = int(input("Do you want to perform another operation? (yes/no) YES - press 1, NO - press 0: "))
    if controller_operation == 1:
        repeat_operation = True
    elif controller_operation == 0:
        repeat_operation = False
    else:
        print("Invalid choice. Exiting.")
        break

print("Thank you for using our calculator!")




    

