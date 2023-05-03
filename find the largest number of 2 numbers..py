#WAP to enter two numbers and print the largest number.
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
large = n1
if(large<n2):
    large = n2
print("The largest number is: ",large)
