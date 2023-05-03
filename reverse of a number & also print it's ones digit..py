#WAP to input a number & print the reverse of a number & also print it's ones digit.
num = int(input("Enter a number: "))
rev = 0
while(num>0):
  rem = num % 10
  rev = (rev * 10) + rem
  num = num//10
a = rev%10  
print("The reverse number is : ",rev)
print("It's ones digit is : ",a)
