def area_of_shapes():
    print("Program to find area of shapes")
    
    print(""" 
          Enter 1 - rectangle 
          2 - circle 
          3 - trianlgle
          """)
    choice = int(input("Enter your choice: "))
    
    def rectangle():
        length = float(input("Enter length of rectangle: "))
        
        breadth = float(input("Enter breadth of rectangle: "))
        
        area = length * breadth
        
        return area
    
    def circle():
        radius = float(input("Enter radius of circle: "))
        
        area = 22/7 * radius * radius
        
        return area
    
    def triangle():
        base = float(input("Enter base of triangle: "))
        
        height = float(input("Enter height of triangle: "))
        
        area = 1/2 * base * height
        
        return area
    
    if choice == 1:
        print("Area of rectangle is: ", rectangle())
    elif choice == 2:
        print(" Area of circle is:", circle())
    elif choice == 3:
        print("Area of triangle is: ", triangle())
    else:
        print("Invalid option, please choose a valid option")
        
area_of_shapes()      
    
        
        
        
    

        
        
    
    