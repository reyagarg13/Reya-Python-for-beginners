"""
input gender  m/f
input age

"""
gender = input("Enter your gender : ")
age = int(input("Enter your age : "))
if gender == "male" and age >= 21 :
    print("Eligible to marry!")
elif gender == "female" and age >= 18 :
    print("Eligible to marry!")
else :
    print("Not eligible to marry!")
    
