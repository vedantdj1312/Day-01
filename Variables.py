#   Assign multiple values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#   Assigning same value to multiple varialbles

x = y = z = "Orange"
print(x)
print(y)
print(z)

#  Unpacking(assigning values to variables from a list or tuple)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
 
   #            RULES FOR NAMING A VARIABLE
"""    1) A variable name must start with a letter or the underscore character
       2) A variable name cannot start with a number
       3) A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
       4)Variable names are case-sensitive (age, Age and AGE are three different variables)
       5)A variable name cannot be any of the Python keywords.                           """