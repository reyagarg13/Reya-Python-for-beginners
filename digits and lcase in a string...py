"""
WAP to input a string and find the number of digits and lower case
characters in the string.
"""
s = str(input("Enter a word: "))
digits,lcase = 0,0
for ch in s:
    if ch.isdigit():
        digits += 1
    elif ch. isalpha():
        lcase += 1
        
print("No. of digits: ",digits)
print("No. of small letters: ",lcase)
