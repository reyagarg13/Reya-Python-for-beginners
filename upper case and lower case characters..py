"""
WAP to enter a string and find the number of upper case and lower case characters.
"""
s = str(input("Enter a word: "))
ucase,lcase = 0,0
for ch in s:
    if ch>= 'A' and ch<= 'Z':
        ucase += 1
    if ch>= 'a' and ch<= 'z':
        lcase += 1
        
print("No. of capital letters: ",ucase)
print("No. of small letters: ",lcase)
