"""
pseudocode

step 1: define 'main()' f=module function

step 2: Define user define function 'def cost_after_price(price, tax):' 

step 3: Declare varibale for cost = Price * ( 1 + tax / 100 )

step 4: return cost in the 'cost_after_price' function

step 5: call by value the 'cost_after_price' function with arguments 100 and 10
"""

# Python code implementation of the above steps
def cost_after_tax(price, tax):

    return price * (1 + tax / 100)

    # print(f"cost after after tax is {cost}")

    # return cost

def main():
    
    price = float(input("Enter price:"))
    
    tax = float(input("Enter tax for price:"))

    cost = cost_after_tax(price, tax);
    
    print(f"The cost after applying {tax}% tax is {cost:.2f}")

main()