# WAP to calculate Simple Interest & Compound Interest .
p = int(input("Enter principal amount : "))
t = int(input("Enter time duration: "))
r = int(input("Enter percentage of rate : "))
si = (p * t * r) / 100
ci = p * (pow((1 + r / 100), t))
print("principal = ",p)
print("time = ",t)
print("rate = ",r)
print("simple interest = ",si)
print("compound interest = ",ci)
