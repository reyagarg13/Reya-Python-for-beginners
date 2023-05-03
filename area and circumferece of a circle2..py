# area and circumferece of a circle.
pi = float(input("Enter value of a pie of a circle : "))
r  = int(input("Enter radius of a circle : "))
print("1.Area")
print("2.Circumference")
print("3.Area and Circumference")
choice = int(input("Enter your choice [1,2,3]: "))
if choice == 1 :
     area  =  pi * r**2
     print("Area = ",area)
elif choice == 2 :
     circumference = 2 * pi * r
     print("Circumference = ",circumference)
elif choice == 3 :
     area  =  pi * r**2
     print("Area = ",area)
     circumference = 2 * pi * r
     print("Circumference = ",circumference)
else :
     print("Invalid choice") 
