
def calculate_BMI():
    print("Hello, Welcome to BMI calculator app")
    
    weight = float(input("Enter weight:"))
    
    height = float(input("Enter height"))
    
    BMI = weight / (height * height)
    
    return BMI


def main():
    choice = int(input("Want to repeat another calculation? \n"))
