NumList = []
Number = int(input("Please enter the no. of elements in this list: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the value of Element %d: " %i))
    NumList.append(value)
 
print("The Minimum element in this list is : ", min(NumList))
print("The Maximum element in this list is : ", max(NumList))
