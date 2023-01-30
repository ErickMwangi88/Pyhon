#Assign a discount of 5%  amount exceeds sh.1000
amount = float(input("Enter the price of the item: "))
if (amount >= 1000):
    print("Discount is offered: ",amount*0.05)
else:
    print("Discount is not offered")
print("Total amount to be paid is: ",amount + (amount*0.05))