#WAP to input a string and replace 'is'with 'are'.
s1    = str(input("Enter a string: "))
ch    = str(input("Enter a character: "))
newch = str(input("Enter a replacing character : "))
s2    = s1.replace(ch, newch)
print("Original String:  ", s1)
print("Modified String:  ", s2)
