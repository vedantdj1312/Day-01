"""No need to declare the data type of the variable
   after assigning the value system will automatically assign the 
   variable appropriate data type based on the value assigned to the variable"""

a=54             
b=32           
c="Hello"
d="e"
e=3.24
f=2.23

"""Arithematic Operations will only be applicable to Variables with same data type"""

print(a+b)
print(a-b)

print(c+d)        #strings can only be added by this method(Substraction not possible)
                  #                                 __
print(a+e)        # (int) +/-/*// (float) =(float)    |
print(a*e)        # (int) +/-/*// (int) =(int)        |---->  IMPLICIT TYPECASTING
print(a-e)        # (float) +/-/*// (float) =(float)__|
print(a/e)

""" TO KNOW THE DATA TYPE OF A VARIABLE"""

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
""" ARITHEMATIC OPERATION BETWEEN NUMBR=ERS AND STRINGS"""

print(a*c)
print(c*e)
