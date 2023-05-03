#Checks whether the given character is a arithmetic operater or not.
op = input("Enter any operater: ")
if op == "+" or op == "-" or op == "*" or op == "/" or op == "%" or op == "**" or op == "//" :
    print(op,"is an arithmetic operater")
else :
    print(op,"is not an arithmetic operater")
