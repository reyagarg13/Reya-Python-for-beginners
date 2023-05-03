"""
input gender  m/f
input age

"""
gender = input("Enter your gender : ")
age = int(input("Enter your age : "))
if gender == "male" and age >= 21 :
    print("Hello Sir, Eligible to marry!")
elif gender == "female" and age >= 18 :
    print("Hello Madam, Eligible to marry!")
else :
    if gender == "male":
        print("Hello Sir,Not eligible to marry!")
    elif gender == "female":
        print("Hello Madam,Not eligible to marry!")
    else:
        print("invalid gender!")
