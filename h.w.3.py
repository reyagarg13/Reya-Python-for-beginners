"""
user inputs in centimeters
245
2 meters and 45 centimeters
1 meter = 100 cms

-------------------------------------------------

1 foot --- 12 inches ---- 30cms
1 inch --- 2.5cms
foot and inches

"""
length = int(input("Enter length in centimeters : "))
print(length // 100,"meters")
print(length % 100,"centimeters")
"""
-------------------------------------------------
"""
length = int(input("Enter length in inches : "))
print(length // 12,"foot")
print(length % 12,"inches")
