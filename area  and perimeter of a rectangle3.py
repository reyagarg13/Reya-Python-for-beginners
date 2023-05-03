"""
user inputs length and breadth
1.area
2.perimeter
"""
l = int(input("Enter length of a rectangle : "))
b = int(input("Enter breadth of a rectangle : "))
print("1.Area")
print("2.Perimeter")
print("3.Area and Perimeter")
choice = int(input("Enter your choice [1,2]: "))
if choice == 1 :
    area = l*b
    print("Area = ",area)
elif choice == 2 :
    perimeter = 2*(l+b)
    print("Perimeter = ",perimeter)
elif choice == 3 :
    area = l*b
    print("Area = ",area)
    perimeter = 2*(l+b)
    print("Perimeter = ",perimeter)
else :
    print("invalid choice")
