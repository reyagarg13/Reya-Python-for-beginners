"""
student name
s1,s2,s3
total,avg
"""
name = input("Enter your name         : ")
s1 = int(input("Enter subject 1 marks : "))
s2 = int(input("Enter subject 2 marks : "))
s3 = int(input("Enter subject 3 marks : "))
total = (s1 + s2 + s3)
average = total / 3
print("====================================")
print("NAME        = ",name)
print("S1 MARKS    = ",s1)
print("S2 MARKS    = ",s2)
print("S3 MARKS    = ",s3)
print("====================================")
print("TOTAL MARKS = ",total)
print("AVERAGE     = ",average)
print("====================================")
