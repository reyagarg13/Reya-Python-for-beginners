""" input 2 variables a and b, check whether
a is greater than b
a is less than b
a equal to b
"""
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
if a > b :
    print(a,"is greater than",b)
    print(b,"is less than",a)
elif a < b :
    print(a,"is less than",b)
    print(b,"is greater than",a)
elif a == b :
    print(a,"is equal to",b)
    
    
