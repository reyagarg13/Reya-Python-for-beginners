#Checks whether the given character is a Relational operater or not.
#   == , > , < , >= , <= , != these are relational operators
op = input("Enter any operater: ")
if op == "==" or op == "<" or op == ">" or op == "<=" or op == ">=" or op == "!=" :
    print(op,"is an relational operater")
else :
    print(op,"is not an relational operater")
