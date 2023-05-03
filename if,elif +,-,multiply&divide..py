# if,elif +,-,*&/.
a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice = int(input("Enter your choice [1,2,3,4]: "))
if choice == 1 :
    c = a + b
    print(a," + " ,b,"=" ,c)
    # 20 + 10 = 30
elif choice == 2 :
    c = a - b
    print(a,"-",b, "=",c)
elif choice == 3 :
    c = a * b
    print(a, "*",b, "=",c)
elif choice == 4 :
    c = a / b
    print(a,"/",b,"=",c)
else :
    print("Invalid choice")
