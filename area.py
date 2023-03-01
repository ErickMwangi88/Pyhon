#Area of a circle using inbuilt functions
#Area = pi*radius*radius
pi = 3.142
radius  = int(input("Enter the radius of the circle: "))
def area(radius):
    total = pi * radius * radius
    print("The area of the circle is: ",total)
    
area(radius)