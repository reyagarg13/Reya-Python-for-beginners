mylist = []
print("Enter 5 elements of the list: ")
for i in range(5):
    val = int(input())
    mylist.append(val)

print("Enter an element to be searched: ")
elem = int(input())

for i in range(5):
    if elem == mylist[i]:
        print("\nElement found at Index:", i)
        print("Element found at Position:", i+1)
