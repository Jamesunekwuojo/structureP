
def calculate_BMI():
    print("Hello, Welcome to BMI calculator app")
    
    weight = float(input("Enter weight:"))
    
    height = float(input("Enter height"))
    
    BMI = weight / (height * height)
    
    print(f"The BMI is equal to {BMI}")
    
    return BMI


def main():
    
    loop_choice = True
    
    
    while loop_choice:
        calculate_BMI()
        choice = int(input("Want to repeat another calculation? \n Yes -  press 1 \n No - press 2 \n"))
    

    
        if choice ==1:
            loop_choice = True
        elif choice ==0:
            loop_choice = False
        else:
            print("Invalid choice! enter 1 for yes or 0 for no")
            break
    
main()      
    
    
