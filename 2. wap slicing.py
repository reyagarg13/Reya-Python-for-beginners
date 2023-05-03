ln = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
s1 = ln[5:11:2]
sum = 0
print("Elements of 1st slice:" , s1)
for i in s1:
    sum += i
print("Sum of elements of the 1st slice:" , sum)

s2 = ln[::4]
sum = avg = 0
length = len(s2)
print("Elements of 2nd slice:" , s2)
for x in s2:
    sum += x
avg = sum/length
print("Average of elements of 2nd slice:" , avg)
