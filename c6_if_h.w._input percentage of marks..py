#input percentage of marks,if and elif program.
marks = int(input("Enter your percentage of marks : "))
if marks >=75 and marks <=100 :
    print("Your marks is at distinction level!")
elif marks >=60 and marks <75 :
    print("Your marks is first class!")
elif marks >=50 and marks <60 :
    print("Your marks is second class!")
elif marks >=35 and marks <50 :
    print("You are just passed!")
elif marks <35 and marks >=0 :
    print("You are failed!")
else :
    print("INVALID INPUT!")
