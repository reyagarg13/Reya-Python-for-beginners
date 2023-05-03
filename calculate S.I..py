"""
print(),input(),type()
int,float,str
"""
# calculate simple interest, given p,t,r

p = int(input("Enter principal amount : "))
t = int(input("Enter time duration: "))
r = int(input("Enter percentage of rate : "))
si = (p * t * r) / 100
print("principal = ",p)
print("time = ",t)
print("rate = ",r)
print("simple interest = ",si)

