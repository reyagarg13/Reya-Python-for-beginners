#WAP to enter the number and the check whether its palindrome or not.
num = int(input("Enter a number: "))
rev = 0
num1 = num
while(num1 != 0):
    digit = num1 % 10;
    num1 = num1//10
    rev = rev*10+digit
if rev == num:
    print(num, "is a palindrome number.")
else:
    print(num, "is not a palindrome number.")
