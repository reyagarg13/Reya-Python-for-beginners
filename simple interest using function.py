def SI(P,R,T):

   SI = (P * R * T) / 100
   
   return SI

P = int(input("Enter the principal: "))

R = 10

T = 2

print("Simple interest is", SI(P,R,T))
