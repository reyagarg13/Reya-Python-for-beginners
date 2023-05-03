#WAP to input a number and find the entered number is Armstrong number or not.
num = int(input("Enter a number: "))
s = 0
temp = num
while temp>0:
    digit = temp%10
    s    += digit**3
    temp//= 10
if num == s:
    print(num,"is an Armstrong number.")
else:
    print(num,"is not an Armstrong number.")
