# type casting

otp = 781234
otp = str(otp)  # it will directly convert the int into string it is called as type casting
print("Your otp is  " + str(otp))  # str indicate that int is temporarly converted into string and then the python will print
print(type(otp))

count = "20"
# print(count + 1) this will give error instead
print(int(count)+1)
