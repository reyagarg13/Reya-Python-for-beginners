def arrsum(arr,size):
    if(size == 0):
        return 0
    else:
        return arr[size-1] + arrsum(arr,size-1)

n   = int(input("Enter the number of elements for list: "))
a   = []

for i in range(0,n):
    element=int(input("Enter element: "))
    a.append(element)
print("The list is:", a)

b = arrsum(a,n)
print("Sum of items in list: ", b)
