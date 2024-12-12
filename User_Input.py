#      TAKING INTEGER OR FLOAT INPUT
x = input("enter the number : ")
print("the number enterd is :",x)

#      TAKING STRING INPUT
x = input("enter the string : ")
print("the string enterd is :",x)

#PROBLEM
x = input("enter the number : ")  #lets say x is 21
y = input("enter the number : ")  #lets say y is 3
print(x+y)               #Ans will be 213 and not 24 (bcz x & y entered as  strings)       

#SOLTUION 1
x = input("enter the number : ")  #lets say x is 21
y = input("enter the number : ")  #lets say y is 3
print(int(x)+int(y))       #Ans will be 24 (bcz by typecasting we made x & y integers while printing )          

#SOLTUION 2
x = int(input("enter the number : "))  #lets say x is 21
y = int(input("enter the number : ") ) #lets say y is 3
print(x+y)       #Ans will be 24 (bcz we made x & y integers while taking input)

