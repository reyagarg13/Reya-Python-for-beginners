#WAP to enter a string and find the entered string is palindrome or not.
s = str(input("Please enter your own string: "))
if (s == s[:: - 1]):
    print("Yes,it is a palindrome string.")
else:
    print("No,it is not a palindrome string.")
