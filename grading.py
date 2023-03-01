#grading system
calculus = int(input("Enter your calculus marks:"))
programming = int(input("Enter your programming marks:"))
database = int(input("Enter your database marks:"))

average = float(calculus + programming + database)/3

if (average >= 70 and average <= 100):
    print("The grade is: A")
elif (average >= 60 and average <= 69):
    print("The grade is: B")
elif (average >= 50 and average <= 59):
    print("The grade is: C")
elif (average >= 40 and average <= 49):
    print("The grade is: D")
else:
    print("You have FAILED")
               
               