def intro():
    print("Java Coffee Discount Calculator")
    print("Please follow the on screen instructions")
    print()
    print("Rate of discount based on the following")
intro()
def table():
    print()
    print("Number of bags\t\t\tDiscount rate")
    print()
    print("Less than 25\t\t\t0%")
    print("25 - 49\t\t\t\t5%")
    print("50 - 99\t\t\t\t10%")
    print("100 or more\t\t\t20%")
    print()
table()
def passwordenter():
   word="lesscount"
   entry=input("Enter the password:" )
   if entry==word:
       print("Password accepted")
   else:
       print("You have entered an incorrect password")
       print(passwordenter())
passwordenter()
def calculations():
    bags=int(input("Number of bags purchased:"))
    if bags>=25:
        discount=0.05
        perc="5%"
    elif bags>=50<=99:
        discount=0.1
        perc="10%"
    elif bags>=100:
        discount=0.2
        perc="20%"
    else:
        discount=0
        perc="0%"
    cost=5.50
    grosscost=bags*cost
    discountdeduct=discount*grosscost
    print()
    print("The rate of discount is", perc)
    print()
    print("Price:", grosscost)
    discountdeduct=discount*grosscost
    print("Discount Received:", discountdeduct)
    total=grosscost-discountdeduct
    print("Total Amount Due:", total)
    print()
    print("Program End")
calculations()

        
                 
    
