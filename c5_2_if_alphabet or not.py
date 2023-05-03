# Check whether given character is a Alphabet or not
ch = input("Enter any character : ")
if ch >= "A" and ch <= "Z" :
    print(ch,"is a capital letter.")
elif ch >= "a" and ch <= "z" :
    print(ch,"is a small letter.")
else :
    print(ch,"is not an alphabet.")
    
op = input("Enter any operater: ")
if op == "+" or op == "-" or op == "*" or op == "/" or op == "%" or op == "**" or op == "//" :
    print(op,"is an arithmetic operater")
else :
    print(op,"is not an arithmetic operater")
