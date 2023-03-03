# input from user
name = input("Enter your name : ")
height = float(input("Enter your height : "))
height_inches = "{:.2f}".format(height/2.54)
print(" Hello " + name)
print("Your height is : " + str(height) + " CM")
print("Your height in inches : " + height_inches + " inches tall")