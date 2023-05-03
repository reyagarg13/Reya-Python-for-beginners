n = eval(input("Enter the numbers: "))
s = 0
for i in n:
    s = s + i
mean = s/len(n)
print("Calculated mean:" , mean , "is the mean of the entered numbers.")
