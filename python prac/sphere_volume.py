#volume of a sphere = 4/3 * pi * radius^3
 
from math import pi

radius = int(input("Enter the radius of the sphere: "))
def volume_of_sphere(radius):
    volume = 4/3 * pi * radius * radius * radius
    print("The volume of the sphere is ",volume)

volume_of_sphere(radius)