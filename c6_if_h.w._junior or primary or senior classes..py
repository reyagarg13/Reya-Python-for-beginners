#user inputs class primary,junior,senior and if or elif program.
ch = int(input("Enter your class : "))
if ch <=12 and ch >=9 :
    print("You belong to senior classes!")
elif ch >=4 and ch <=8 :
    print("You belong to primary classes!")
elif ch >=1 and ch <=3 :
    print("You belong to junior classes!")
else :
    print("You entered invalid class!")
