"""
User inputs weight in grams
convert to kgs and grams
2450 grams
output :  2 kgs 450 grams

1kg ---> 1000 grams
"""
weight = int(input("Enter weight in grams : "))
print(weight // 1000,"kgs")
print(weight % 1000,"grams")

