"""
step1 : start
step2: Input student age
step3: IF student age is greater than 16
THEN  print student can be admitted
ELSE student is cannot be admitted
step4: stop
"""

def student_admission():
    age = int(input("Enter student age: "))
    if age >= 16:
        print("Student can be admitted")
    else :
        print("Student cannot be admitted")

student_admission()
