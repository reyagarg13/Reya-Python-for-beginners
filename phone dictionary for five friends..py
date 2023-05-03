n = int(input("Enter how many contacts you need to save: "))
Friends = {}
for i in range(n):
    Name = input("Enter name: ")
    Phone_no = int(input("Enter Phone Number: "))
    Friends[Name] = Phone_no

print(Friends)    
