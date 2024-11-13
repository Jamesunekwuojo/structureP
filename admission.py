# NAME : ABAH JAMES UNEKWUOJO
# MATRIC. NO: AUL/CMP/22/090

# Pseudocode to only admit student whoose whoose age  is up to 16
# step 1: Start
# step 2: Ask for student's age and store it in a variable.  That's input student age

# step 3: If student age is greater or equal to 16
# THEN
#    print "admitted" , 'your age is {student age}'
# else 
#   print "admission request rejected, age is less than 16", 'your age is {student age}'

# step 4: stop




# main python code
def student_admission():
   student_age = int(input("Enter your age: "))
   if student_age >= 16:
       print(f"Congratulations! Admitted. Your age is, {student_age}")
   else:
       print(f'Admission rejected, age is less than 16. Your age is {student_age}')   


student_admission()