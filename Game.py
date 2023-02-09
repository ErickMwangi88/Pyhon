# This is a simple guessing game
import random
var = random.randint(0, 100)

num = int(input("Enter your lucky number: "))
# The lucky number should be between 0 and 100
if num == var:
    print("Congratulations,YOU WIN")
elif num < var:
    print("The number is too high")
elif num > var:
    print("The number is too low")
else:
    print("TRY AGAIN,You are unlucky")

print("The lucky number is:", var)
