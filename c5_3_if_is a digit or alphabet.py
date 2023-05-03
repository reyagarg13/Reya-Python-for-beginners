# Check whether given character is a Alphabet or not
ch = input("Enter any single character : ")
if ch >= "A" and ch <= "Z" :
    print(ch,"is a capital letter.")
elif ch >= "a" and ch <= "z" :
    print(ch,"is a small letter.")
elif ch >= "0" and ch <= "9" :
    print(ch,"is a digit.")
else :
    print(ch,"is a special character.")
