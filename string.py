# string
message = "his son's book"
name = 'Ram'
quote = '"good"'

print(quote)
print(name.upper())  # we want to call a method using dot symbols to invoking a method
print(message + " " + name)
print(name.lower())
print(message.title())
mgs1 = message + name
print(len(message))
print(message.find("k"))  # initial value will print when we have same value in string
print(message.count("o")) # counts how many letters in the string using count method
print(message.replace("son's", "new"))

