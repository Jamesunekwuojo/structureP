# Write a pseudocode and code in Python that finds the largest of three numbers
# using if…. else if statement.


"""
step 1: Start

step 2: Declare three variables num1, num2, num3 and let them accept inputs for the three variables.

step 3: If num1 == num2 == num3 then print "All numbers are equal" and go to Step 7.

step 4: If num1 > num2 and num1 > num3 then print "num1 is the largest number".
elif num2 > num1 and num2 > num3 then print "num2 is the largest number".
else print "num3 is the largest number".

step 5: If num1 == num2 and num1 > num3 then print "num1 and num2 are the largest numbers".
elif num1 == num3 and num1 > num2 then print "num1 and num3 are the largest numbers".
elif num2 == num3 and num2 > num1 then print "num2 and num3 are the largest numbers".

step 6: If inputs are not valid numbers, then print "Invalid input. Please enter numeric values."

step 7: Stop

"""

def find_largest():
    try:
        # To Accept inputs for the three variables
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))

        # To Check if all numbers are equal
        if num1 == num2 == num3:
            print("All numbers are equal.")
            return

        # To Compare the numbers to find the largest
        if num1 > num2 and num1 > num3:
            print(f"{num1} is the largest number.")
        elif num2 > num1 and num2 > num3:
            print(f"{num2} is the largest number.")
        else:
            print(f"{num3} is the largest number.")

        # To Check for ties in pairs
        if num1 == num2 and num1 > num3:
            print(f"{num1} and {num2} are the largest numbers.")
        elif num1 == num3 and num1 > num2:
            print(f"{num1} and {num3} are the largest numbers.")
        elif num2 == num3 and num2 > num1:
            print(f"{num2} and {num3} are the largest numbers.")

    except ValueError:
        # To Handle invalid inputs
        print("Invalid input. Please enter numeric values.")

# To Call the function
find_largest()
