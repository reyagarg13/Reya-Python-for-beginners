"""
Input monthly sale of employee and give bonus of
10% if sale is more than 50000 otherwise bonus
will be 0.
"""
bonus = 0
sale = int(input("Enter Monthly Sales: "))
if sale>50000:
    bonus = sale*10/100
print("Bonus = " + str(bonus))
