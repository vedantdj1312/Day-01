#                                               ______________________
x = int(1)   # x will be 1                                           |
y = int(2.8) # y will be 2                                           |
z = int("3") # z will be 3                                           |
#                                                                    | 
print(x+z)  #Ans will be 4 (bcz x & z are integers)                  |
#                                                                    |
a = float(1)     # a will be 1.0                                     |
b = float(2.8)   # b will be 2.8                                     |
c = float("3")   # c will be 3.0                                     |
d = float("4.2") # d will be 4.2                                     |
#
print(x+b)  #Ans will be 3.8 (bcz x is int & b is float)
#
m = str("hello") # m will be "hello"
n = str(2)    # n will be "2"
o = str(3)  # o will be "3"
#
print(n+o)  #Ans will be 23 not 5(bcz n & o are strings not integers)

