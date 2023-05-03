"""
Check whether the given character is logical,arithmetic operaters or upper case or lower case
or number or not.
"""
ch = input("Enter any single character : ")
if ch == "and" or ch == "or" :
    print(ch,"is an logical operater.")
elif ch >= "A" and ch <= "Z" :
    print(ch,"is a capital letter.")
elif ch >= "a" and ch <= "z" :
    print(ch,"is a small letter.")
elif ch >= "0" and ch <= "9" :
    print(ch,"is a number.")
elif ch == "+" or ch == "-" or ch == "*" or ch == "/" or ch == "%" or ch == "**" or ch == "//" :
    print(ch,"is an arithmetic operater")
else :
    print(ch,"is a special/invalid character.")
