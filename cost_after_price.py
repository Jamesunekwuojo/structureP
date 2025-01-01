"""
pseudocode

step 1: define 'main()' module function

step 2: Define user define function 'def cost_after_tax(price, tax):' 

step 3: return Price * ( 1 + tax / 100 )

step 4: Declare  variables price and tax  and dynamically assign values to them

step 5: call by value the 'cost_after_price' function with arguments price and tax
"""

# Python code implementation of the above steps
def cost_after_tax(price, tax):

    return price * (1 + tax / 100)

   

def main():
    
    price = float(input("Enter price:"))
    
    tax = float(input("Enter tax for price:"))

    cost = cost_after_tax(price, tax);
    
    print(f"The cost after applying {tax}% tax is {cost:.2f}")

main()